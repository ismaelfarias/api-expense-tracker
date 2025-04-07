from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()
origins = [
    "http://localhost:3000",
]


@app.get("/")
def root():
    return JSONResponse(content={"message": "Hello World"}, status_code=200)

@app.get("/health")
def health():
    return JSONResponse(content={"status": "ok"}, status_code=200)