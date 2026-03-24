from langchain.tools import tool

@tool
def get_product_price(product:str)->float:
    """Look up for product price."""
    print(f">> Executing price of product {product}")
    prices={"laptop":200,"keyboard":10,"mouse":15,"headphone":50}
    return prices.get(product,0)

@tool
def apply_discount(price:int,discout_tier:str)->float:
    """Applying discount on product with their tier."""
    discount_percentage={"gold":5,"diamond":7,"silver":4}
    discount=discount_percentage.get(discout_tier,0)
    final_price=price-(price*discount/100)
    return  round(final_price, 2)

