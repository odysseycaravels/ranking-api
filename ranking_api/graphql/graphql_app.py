import graphene
from starlette.graphql import GraphQLApp

# TODO: This is apparently depreacted since 0.15 - use other graphql provider (we might just skip
# graphql implementation for now).
# See: https://www.starlette.io/graphql/

from ranking_api.graphql.graphql_model import TournamentModel


class Query(graphene.ObjectType):
    tournaments = graphene.List(TournamentModel)

    def resolve_tournaments(self, info):
        query = TournamentModel.get_query(info)  # SQLAlchemy query
        return query.all()


schema = graphene.Schema(query=Query)
gql_app = GraphQLApp(schema=schema)
