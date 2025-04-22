from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/wait")
async def wait_and_respond():
    await asyncio.sleep(3)  # Simulates a non-blocking delay (e.g., DB/API call)
    return {"message": "Waited for 3 seconds, but didn't block others!"}
