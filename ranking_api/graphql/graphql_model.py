""" Model classes for GraphQL """
from graphene_sqlalchemy import SQLAlchemyObjectType

from ranking_api.model import Event


class TournamentModel(SQLAlchemyObjectType):
    class Meta:
        model = Event
