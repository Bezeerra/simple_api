from dataclasses import dataclass

from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()


@dataclass
class CountNumber:
    number_a: int
    number_b: int


@app.get("/")
async def read_root():
    return JSONResponse(content={"message": "Hello, World"}, status_code=200)


@app.post("/add")
async def count_numbers(schema: CountNumber):
    return JSONResponse(content={"result": schema.number_a + schema.number_b}, status_code=200)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
