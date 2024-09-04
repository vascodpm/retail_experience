# Env variables loader
import os
import dotenv
dotenv.load_dotenv(dotenv_path="../../.env")

# Data handlers
import pandas as pd
from sqlalchemy.orm import Session

# Utils
try:
    from data_utils import get_db, get_products
    from data_models import Products
    from database import SessionLocal
except:
    from .data_utils import get_db, get_products
    from .data_models import Products
    from .database import SessionLocal

# Llamaindex
from llama_index.vector_stores import PineconeVectorStore, SimpleVectorStore 
from llama_index.storage.storage_context import StorageContext
from llama_index import VectorStoreIndex, Document, ServiceContext
from llama_index.llms import OpenAI
from llama_index.storage.index_store import SimpleIndexStore
from llama_index.storage.docstore import SimpleDocumentStore
from llama_index import load_index_from_storage
from llama_index.retrievers import BM25Retriever, BaseRetriever
from llama_index.vector_stores.types import MetadataFilters, ExactMatchFilter

# VDBs
#import weaviate
import pinecone

ENVIRONMENT = "us-east-1"
INDEX_NAME = "foodproject"

def process_products():
    # Reading SQLite db
    db = SessionLocal()
    products = get_products(db)
   
    # Convert the data to a pandas DataFrame
    products_data = [{"id": r.id, "name": r.name, "brand": r.brand, "price":r.price, "category":r.category,} for r in products]
    df = pd.DataFrame(products_data)



    # # Merging
    # df = pd.merge(products_df, on="id")

    # # Groupby restaurant and creating text for embedding
    # df["food_text"] = "\n-"+df["food_name"] + "\n" + df["food_description"]

    # df = df.groupby("id").agg({"name": "first", "description": "first", "food_text": "sum"}).reset_index()
    
    # # Creating text for embedding
    # df["text"] = "```" + df["name"] + "\nRestaurant description: " + df["description"] + "\nFood available:" + df["food_text"] + "\n```"

    # Llamaindex
    documents = [
        Document(
            text=df_row[1]["name"],
            metadata={
                "search_type": "product",
                "product_id": df_row[1]["id"],
                "product_name": df_row[1]["name"],
                "product_brand": df_row[1]["brand"],
                "product_price": df_row[1]["price"],
                "product_category": df_row[1]["category"],
            }
        )
        for df_row in df.iterrows()
    ]

    vector_store = PineconeVectorStore(
        index_name=INDEX_NAME,
        environment=ENVIRONMENT,
    )

    storage_context = StorageContext.from_defaults(
        vector_store=vector_store,
    )

    llm = OpenAI(model="gpt-3.5-turbo")

    service_context = ServiceContext.from_defaults(chunk_size=512, llm=llm)

    nodes = service_context.node_parser.get_nodes_from_documents(documents)

    storage_context.docstore.add_documents(nodes)

    print("123")

    index = VectorStoreIndex.from_documents(
        documents=documents,
        #vector_store=vector_store,
        storage_context=storage_context,
        service_context=service_context,
    )


    print("456")

    return  index,nodes

def load_index():

    vector_store = PineconeVectorStore(
        index_name=INDEX_NAME,
        environment=ENVIRONMENT,
        # add_sparse_vector=True,
    )
    #print(vector_store)

    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    #print(storage_context)
    
    #loaded_index = VectorStoreIndex.from_vector_store(vector_store)
    index = VectorStoreIndex([], storage_context=storage_context,)

    return index

def main():
    # Testing it
    index, nodes = process_products()
    idx = load_index()

    # qe = idx.as_query_engine()
    ret = idx.as_retriever(similarity_top_k=5)
    ret2 = idx.as_retriever(
        similarity_top_k=5,
        filter=[ExactMatchFilter(key="search_type", value="product")]
    )
    bm25 = idx.as_retriever(similarity_top_k=5, vector_store_query_mode="hybrid", alpha=0.0)
    hret = idx.as_retriever(similarity_top_k=5, vector_store_query_mode="hybrid", alpha=0.75)
    hsnw = idx.as_retriever(similarity_top_k=5, vector_store_query_mode="hybrid", alpha=1.0)
    
    # Testing 
    answers = {
        "regular": [],
        "regular_filtered": [],
        "bm25": [],
        "hybrid_retriever": [],
        "hsnw": [],
    }
    query = "testing, I would like to filter by coca cola"
    for retriever in [
        (ret, "regular"),
        (ret2, "regular_filtered"),
        (bm25, "bm25"),
        (hret, "hybrid_retriever"),
        (hsnw, "hsnw")
    ]:
        ans = retriever[0].retrieve(query)
        for response in ans:
            answers[retriever[1]].append(
                (
                    response.node.metadata["product_name"],
                    response.score,
                    # response.node.text,
                )
            )
    # Printing in ordered by score for all the retrievers
    print("Query: ", query)
    for retriever in answers:
        print(f"Retriever: {retriever}")
        for ans in sorted(answers[retriever], key=lambda x: x[1], reverse=True):
            print(ans)
        print("\n\n")


if __name__ == "__main__":
    main()

