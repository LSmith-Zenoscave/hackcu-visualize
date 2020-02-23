from starlette.applications import Starlette
from starlette.routing import Route
from starlette.graphql import GraphQLApp
import graphene

from visual_attacks.schema import schema

routes = [
    Route('/', GraphQLApp(schema=schema))
]

app = Starlette(routes=routes)