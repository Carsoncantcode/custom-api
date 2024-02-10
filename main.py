from fastapi import *
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials= True,
    allow_methods= ['*'],
    allow_headers = ['*']
)

@app.get('/')
def read_root():
    return{'Status': 'Active'}

@app.get('/test_endpoint')
def testEndpoint():
      return{'Test Status': 'Successful'}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)