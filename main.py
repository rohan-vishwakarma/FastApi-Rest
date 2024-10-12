import asyncio
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hejjjllo": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    print("Task Started")
    asyncio.sleep(5)
    print("Task Ended")
    return {"item_sid": item_id, "q": q}