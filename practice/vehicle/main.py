from fastapi import FastAPI
import asyncio

# creates an instance of the FastAPI class
app = FastAPI()


@app.get("/")
async def read_root():
    """
    await = pauses execution of this function until asyncio.sleep(2)
    """
    await asyncio.sleep(2)
    return {"message": "Hello world"}
