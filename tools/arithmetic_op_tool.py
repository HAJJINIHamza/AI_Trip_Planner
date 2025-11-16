import os 
from dotenv import load_dotenv
load_dotenv()
from langchain.tools import tool
from langchain_community.utilities.alpha_vantage import AlphaVANTAGEapiwRAPPER


@tool
def multiply(a:int, b:int):
    """
    Mutliply two integers
    
    Args :
        a : int
        b : int
    Return :
        int: The product of a and b
    """
    return a*b

@tool
def add(a : int, b:int):
    """
    Add two integers 

    Args: 
        a : int
        b : int
    
    Return :
        int : the sum of a and b
    """
    return a + b

@tool
def currency_converter(from_curr: str, to_curr: str, value: float) -> float:
    os.environ["ALPHAVANTAGE_API_KEY"] = os.getenv("ALPHAVANTAGE_API_KEY")
    alpha_vantage = AlphaVANTAGEapiwRAPPER()
    exchange_rate_ = alpha_vantage._get_exchange_rate(from_curr, to_curr)
    exchange_rate = exchange_rate_["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    return value*float(exchange_rate)
