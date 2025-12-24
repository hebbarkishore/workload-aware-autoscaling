from fastapi import FastAPI
import time
import os

app = FastAPI()

WORK_UNITS = int(os.getenv("WORK_UNITS", 1_000_000))
SLEEP_MS = int(os.getenv("SLEEP_MS", 0))

@app.get("/compute")
def compute():
    start = time.time()

    total = 0
    for i in range(WORK_UNITS):
        total += i * i

    if SLEEP_MS > 0:
        time.sleep(SLEEP_MS / 1000)

    duration_ms = round((time.time() - start) * 1000, 2)

    return {
        "status": "ok",
        "work_units": WORK_UNITS,
        "duration_ms": duration_ms,
        "result": total
    }