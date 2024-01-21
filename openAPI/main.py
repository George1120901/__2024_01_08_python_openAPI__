from typing import Union
from fastapi import FastAPI
import redis
import os
from dotenv import load_dotenv

celsius=27
load_dotenv()
redis_conn = redis.Redis.from_url(os.environ.get('REDIS_HOST_PASSWORD'))
redis_conn.set('board:temp', celsius)

app = FastAPI()

@app.get("/")
def read_root():
    return {"pico_w": "temperture"}


@app.get("/temperature/{celsius}")
def counter(c: int):
    celsius = redis_conn.get('board:temp')
    return {"temperature": celsius}


@app.get("/counter/{c}")
def counter(c: int):
    counter = redis_conn.incr('test:increment', c)
    return {"Counter": counter}