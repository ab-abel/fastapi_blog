from fastapi import FastAPI
import uvicorn
from router import base
from core.config import settings
from db.base import Base
from db.session import engine


app = FastAPI()

def configuration():
    router_config()
    create_table()

def router_config():
    app.include_router(base.router)

def create_table():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    configuration()
    uvicorn.run(app, port=8000, host='127.0.0.1')
else:
    configuration()
    

@app.get("/")
async def hello():
    print()
    return {"Hello":"User"}
    