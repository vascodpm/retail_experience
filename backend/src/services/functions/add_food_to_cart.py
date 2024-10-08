from tenacity import retry, wait_random, stop_after_attempt

@retry(wait=wait_random(min=1, max=5), stop=stop_after_attempt(5))
async def add_food_to_cart(
        CONFIG,
        restaurant_uuid: str=None,
        product_id: str=None,
        product_quantity: int=1,
):
    return {
        "response": {
            "restaurant_uuid": 1,
            "product_id": str(product_id),
            "product_quantity": int(product_quantity)
        }
    }