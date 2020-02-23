import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from sqlalchemy import inspect

from .models import (
    Connection as ConnectionModel,
    Credential as CredentialModel,
    ShellCommand as ShellCommandModel,
    HTTPCommand as HTTPCommandModel,
)


class Connection(SQLAlchemyObjectType):
    class Meta:
        model = ConnectionModel
        filter_fields = {
            'sourceIp': ['exact', 'icontains', 'istartswith'],
            'destinationPort': ['exact'],
        }
        interfaces = (relay.Node, )


class Credential(SQLAlchemyObjectType):
    class Meta:
        model = CredentialModel
        filter_fields = {
            'username': ['exact', 'icontains', 'istartswith'],
            'password': ['exact'],
        }
        interfaces = (relay.Node, )


class ShellCommand(SQLAlchemyObjectType):
    class Meta:
        model = ShellCommandModel
        filter_fields = {
            'command': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )


class HTTPCommand(SQLAlchemyObjectType):
    class Meta:
        model = HTTPCommandModel
        filter_fields = {
            'request': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    connection = relay.Node.Field(Connection)
    credential = relay.Node.Field(Credential)
    shell_command = relay.Node.Field(ShellCommand)
    http_command = relay.Node.Field(HTTPCommand)

    all_connections = SQLAlchemyConnectionField(Connection)
    all_credentials = SQLAlchemyConnectionField(Credential)
    all_shell_commands = SQLAlchemyConnectionField(ShellCommand)
    all_http_commands = SQLAlchemyConnectionField(HTTPCommand)


schema = graphene.Schema(query=Query)
