from fastapi import FastAPI
import uvicorn
from router import router_v1

app = FastAPI()
app.include_router(router_v1)


@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)