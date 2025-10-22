from fastapi import FastAPI, HTTPException
import os
import json
from typing import Optional
import regex as re


with open("NutritionIndia.json") as file:
    foodList = json.load(file)

app = FastAPI(title="Carbon Footprint")


@app.get("/")
def read_root():
    return {"message": "Welcome to the the Carbon Footprint API"}


@app.get("/id/{item_id}")
def get_item(item_id:int):
    for item in foodList:
        if item["ID"] == item_id:
            return item
    raise HTTPException(status_code=400, detail="Item not found")

@app.get("/food/{Food}")
def get_food(Food:str): 
    result = [item for item in foodList if Food.lower() in item["Food"].lower()]
    if result:
        return result
    else:
        raise HTTPException(status_code=400, detail="Item not found")

@app.get("/region/{Region}")
def get_region(Region:str):
    #result = [item for item in foodList if all(Region.lower() in item["Region"].lower())]

    user_regions = set(r.strip().lower() for r in Region.split(","))
    result = [item for item in foodList
    if user_regions == set(ir.strip().lower() for ir in item["Region"].split(","))
    ]

    if result:
        return result
    else:
        raise HTTPException(status_code=400, detail="Item not found")

@app.get("/region/{Region}/food/{Food}")
def get_region_food(Region:str, Food:str):

    user_regions = set(r.strip().lower() for r in Region.split(","))
    result = [item for item in foodList
    if user_regions == set(ir.strip().lower() for ir in item["Region"].split(",")) and Food.lower() in item["Food"].lower()
    ]
    
    #result = [item for item in foodList if Region.lower() in item["Region"].lower() and Food.lower() in item["Food"].lower()]
    if result:
        return result
    else:
        raise HTTPException(status_code = 400, detail= "Item not found")
        

        


