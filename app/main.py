from typing import Union
from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

class Param(BaseModel):
    weight: Optional[int] = None
    height: Optional[int] = None
    

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/bmi")
def bmi_caculator(request:Param):
    weight = request.weight
    height = request.height
    res = weight / (height / 100) ** 2
    valueFormat =  float(res)
    valueText = None
    if valueFormat >= 30:
        valueText = "อ้วนมาก"
    elif valueFormat >= 25 and valueFormat <= 29.9:
        valueText = "อ้วน"
    elif valueFormat >= 18.6 and valueFormat <= 24:
        valueText = "น้ำหนักปกติ เหมาะสม "
    elif valueFormat <= 18.5:
        valueText = "ผอมเกินไป "
    return {"value" : valueFormat ,"text" : valueText }