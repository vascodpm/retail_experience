from src.utils import get_retriever
from llama_index.vector_stores.types import ExactMatchFilter
from tenacity import retry, wait_random, stop_after_attempt

@retry(wait=wait_random(min=1, max=5), stop=stop_after_attempt(5))
async def find_product(
        CONFIG,
        name_of_product = None,
        brand_of_product = None,
        price = None,
        category = None,
        other_information = None,
        quantity = 5,
    ):

    query = get_query(
        name_of_product = name_of_product,
        brand_of_product = brand_of_product,
        price = price,
        category = category,
        other_information = other_information,
    )

    retriever = get_retriever(
        index_name="foodproject",
        CONFIG=CONFIG,
        top_k=quantity,
        filter=[ExactMatchFilter(key="search_type", value="name")]
    )

    response = retriever.retrieve(query)
    
    # return dict(dict(response[0])["node"])["metadata"]
    for i in range(len(response)):
        response[i] = dict(dict(response[i])["node"])["metadata"]
    return response


def get_query(
        name_of_product: str=None,
        brand_of_product: str="",
        price: list=[],
        category: str="",
        other_information:str ="",
    ):
    """Returns the query for the find products"""
    name_of_product_query = f"""
    Name: {name_of_product}
    """ if name_of_product else ""

    brand_query = f"""
    Brand: {brand_of_product}
    """ if brand_of_product else ""

    price_query = f"""
    Price: {price}
    """ if price else ""

    category_query = f"""
    Category: {category}
    """ if category else ""   

    other_information_query = f"""
    Other information: {other_information}
    """ if other_information else ""

    return f"""
    {name_of_product_query}
    {brand_query}
    {price_query}
    {category_query}
    {other_information_query}
    """