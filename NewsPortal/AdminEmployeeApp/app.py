from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get('/getDummy')
async def list_products():
    print("Hello")
    await asyncio.sleep(5)
    print("Goodbye")
    return {"message": "Hi"}
