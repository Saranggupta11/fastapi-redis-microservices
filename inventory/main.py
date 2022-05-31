from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection,HashModel 

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

class Product(HashModel):
    name:str
    price:float
    quantity:int

    class Meta:
        database=redis

@app.get("/products")
def all():
    return Product.all_pks()


@app.post("/products")
def create(product:Product):
    return product.save()
