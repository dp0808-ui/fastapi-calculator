import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def add(a: float, b: float) -> float:
    logger.info(f"Performing addition: {a} + {b}")
    return a + b

def subtract(a: float, b: float) -> float:
    logger.info(f"Performing subtraction: {a} - {b}")
    return a - b

def multiply(a: float, b: float) -> float:
    logger.info(f"Performing multiplication: {a} * {b}")
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        logger.error("Division by zero attempted.")
        raise ValueError("Cannot divide by zero.")
    logger.info(f"Performing division: {a} / {b}")
    return a / b