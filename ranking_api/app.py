from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from typing import List

from ranking_api.db import get_connection_str
from ranking_api.model import Tournament, TournamentSchema
from ranking_api.graphql.graphql_app import gql_app

app = FastAPI()
app.title = 'Odyssey Caravels - Ranking API'
app.add_middleware(DBSessionMiddleware, db_url=get_connection_str())


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.get('/api/tournaments', response_model=List[TournamentSchema])
async def api_tournaments():
    return db.session.query(Tournament).all()


app.add_route("/graphql", gql_app)
