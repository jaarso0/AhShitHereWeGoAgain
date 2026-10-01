from dotenv import load_dotenv

from langchain.chat_models import init_chat_model

from langsmith import traceable
from langchain.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage

MAX_ITER = 10
MODEL = "qwen2:1.7b"

load_dotenv()

@tool 
def get_product_price(product: str) ->float:
    """Loop up the price of a product in the catalog"""
    print(f"     >> Executing get_product_price(product='{product}')")
    prices = {"laptop": 1299.99, "headphones":149.95, "keyboard": 89.50}
    return prices.get(product, 0.0)


@tool
def apply_discount(price: float, discount_tier: str) -> float:
    """Apply a discount tier to a price and return the final price.
    Available tiers: bronze, silver, gold"""
    print(f"     >> Executing apply_discount(price={price}, discount_tier={discount_tier})")
    discounts_percentage = {"bronze": 5, "silver": 12, "gold": 23}
    discount = discounts_percentage.get(discount_tier, 0)
    return round(price * (1 - discount / 100), 2)


@traceable(name="LangChain Agent Loop")
def run_agent(question: str):
    pass


if __name__ == "__main__":
    # load_dotenv()
    print("hello langchain agent (.blind_tools)!")
    result = run_agent("What is the price of a laptop with a gold discount?")
