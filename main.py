from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from operations import add, subtract, multiply, divide
import logging

app = FastAPI(title="FastAPI Calculator")
logger = logging.getLogger(__name__)

@app.get("/", response_class=HTMLResponse)
def read_root():
    logger.info("Serving calculator web interface.")
    return """
    <!DOCTYPE html>
    <html>
    <head><title>FastAPI Calculator</title></head>
    <body>
        <h1>FastAPI Calculator App</h1>
        <p>Calculator is up and running successfully!</p>
    </body>
    </html>
    """

@app.get("/calculate")
def calculate(op: str, a: float, b: float):
    logger.info(f"API request received for operation '{op}' with inputs {a} and {b}")
    try:
        if op == "add":
            result = add(a, b)
        elif op == "subtract":
            result = subtract(a, b)
        elif op == "multiply":
            result = multiply(a, b)
        elif op == "divide":
            result = divide(a, b)
        else:
            raise HTTPException(status_code=400, detail="Invalid operation")
        return {"operation": op, "a": a, "b": b, "result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))