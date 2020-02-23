from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.responses import JSONResponse
from starlette.graphql import GraphQLApp
from starlette.staticfiles import StaticFiles
import graphene
from geolite2 import geolite2

from visual_attacks.schema import schema


async def geoip(request):
    reader = geolite2.reader()
    latlons = []
    for ip in await request.json():
        info = reader.get(ip)
        if info and "location" in info:
            loc = info["location"]
            latlons.append({'lat': loc['latitude'], 'lng': loc['longitude']})
    return JSONResponse(latlons)

routes = [
    Route('/api', GraphQLApp(schema=schema, graphiql=True)),
    Route('/geoip', geoip, methods=["POST"]),
    Mount('/', app=StaticFiles(directory='visualization-frontend/dist',
                               html=True)),
]

app = Starlette(routes=routes)
