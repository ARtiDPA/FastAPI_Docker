from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/main')
def main_route():
    return {'message': 'hello world'}