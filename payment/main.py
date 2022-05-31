from urllib.request import Request
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection,HashModel 
from starlette.requests import Request
import requests

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

redis=get_redis_connection(
    host="redis-14973.c212.ap-south-1-1.ec2.cloud.redislabs.com",
    port=14973,
    password="hNEir3fZHVWN05fKt3Dzj8s4DhStZ81n",
    decode_responses=True
)

class Order(HashModel):
    product_id:str
    price:float
    fee:float
    toal:float
    quantity:int
    status:str

    class Meta:
        database=redis


@app.get("/orders")
async def create(request:Request):
    body=await request.body()

    req=requests.get('http://localhost:8000/products/%s' % body['id'])

    return req.json();




