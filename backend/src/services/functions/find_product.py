from src.utils import get_retriever
import httpx
from llama_index.vector_stores.types import ExactMatchFilter, MetadataFilters, MetadataFilter, FilterOperator
from tenacity import retry, wait_random, stop_after_attempt

@retry(wait=wait_random(min=1, max=5), stop=stop_after_attempt(5))
async def find_product(
        CONFIG,
        name_of_product=None,
        quantity_of_product=None,
        brand_of_product=None,
        price=None,
        category=None,
        other_information=None,
):
    query = get_query(
        name_of_product=name_of_product,
        quantity_of_product=quantity_of_product,
        brand_of_product=brand_of_product,
        price=price,
        category=category,
        other_information=other_information,
    )
    #print("Generated Query:", query)

    retriever = get_retriever(
        index_name="foodproject",
        CONFIG=CONFIG,
        similarity_top_k=10,
        # Uncomment and adjust if needed
        # filters=filters
    )

    response = retriever.retrieve(query)

    processed_response = []
    for item in response:
        metadata = dict(dict(item)["node"])["metadata"]
        processed_response.append(metadata)

    return processed_response

def get_query(
        name_of_product: str = None,
        quantity_of_product: str = None,
        brand_of_product: str = None,
        price: list = None,
        category: str = None,
        other_information: str = None,
):
    """Helper function to build a query string based on product attributes."""
    name_of_product_query = f"Name: {name_of_product}" if name_of_product else ""
    quantity_query = f"Quantity: {quantity_of_product}" if quantity_of_product else ""
    brand_query = f"Brand: {brand_of_product}" if brand_of_product else ""
    price_query = f"Price: {price}" if price else ""
    category_query = f"Category: {category}" if category else ""
    other_information_query = f"Other information: {other_information}" if other_information else ""

    return f"""
    {name_of_product_query}
    {quantity_query}
    {brand_query}
    {price_query}
    {category_query}
    {other_information_query}
    """
