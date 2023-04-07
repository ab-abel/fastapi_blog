from fastapi import FastAPI
import uvicorn
from router import base

app = FastAPI()

@app.get("/")
async def hello():
    return {"Hello":"User"}
    

def configuration():
    router_config()
    pass

def router_config():
    app.include_router(base.router)


if __name__ == '__main__':
    configuration()
    uvicorn.run(app, port=8000, host='127.0.0.1')
else:
    configuration()
    


