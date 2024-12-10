from fastapi import FastAPI
from sqlalchemy import create_engine
from models import Base


class PgSQL():
    def __init__(self):
        self.DSN = "postgresql://postgres:password@postgres:5432/postgres"

        self.engine = create_engine(self.DSN)

    def startup(self):
        Base.metadata.create_all(bind=self.engine)


pgsql = PgSQL()

app = FastAPI()


@app.get('/main')
def main_route():
    return {'message': 'he!o world'}


@app.get('/startup')
def start():
    pgsql.startup()
    return {'message': 'I AM WORKING'}
