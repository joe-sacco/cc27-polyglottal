from typing import Union
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import json


app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost:8000/scale/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Scale(BaseModel):
    scale: str

@app.post("/scale/") # receive dropdown scale selection from React
async def receive_scale(request: Request):
    scale_setting = await request.json()
    print(scale_setting["scale"])
    return scale_setting["scale"]

# If you want access the body as string, you can use request.body()

