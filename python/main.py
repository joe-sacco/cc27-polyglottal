from time import sleep
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

scale_setting = 'hello'

@app.post("/scale/") # receive dropdown scale selection from React
async def receive_scale(request: Request):
    scale_data = await request.json()
    global scale_setting
    scale_setting = scale_data["scale"]
    print('🔴🔴🔴', scale_setting)
    return scale_setting
 
# REFACTOR OBTAIN SCALE IN PROGRESS

# @app.get("/scale/")
# def read_scale_data():
#     return api.read_scale_data()

# while True:
#     sleep(2)
#     print('🟦🟦🟦', scale_setting)

# If you want access the body as string, you can use request.body()

####### ABOVE CODE WORKS ########


