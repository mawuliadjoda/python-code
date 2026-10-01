def add(a: float, b: float) -> float:
    """
    Adds two numbers.
    
    Args: 
        a (int or float): The first number.
        b (int or float): The second number.
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """
    Subtracts the second number from the first.
    
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    """
    return a - b

def multiply(a: float, b: float) -> float:
    """
    Multiplies two numbers.
    
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    """
    return a * b

def divide(a: float, b: float) -> float:
    """
    Divides the first number by the second.
    
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    
    Raises:
        ValueError: If the second number is zero.
    """
    if b == 0:
        raise ValueError("The second number cannot be zero.")
    return a / b