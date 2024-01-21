
from fastapi import FastAPI
import time
app = FastAPI()

@app.get("/compute")
def compute():
    s = 0
    for i in range(1000000):
        s += i*i
    return {"status": "ok", "value": s}
