from dataclasses import dataclass

from fastapi import FastAPI
from starlette.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


# Permitir todas as origens
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos
    allow_headers=["*"],  # Permite todos os cabeçalhos
)


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
