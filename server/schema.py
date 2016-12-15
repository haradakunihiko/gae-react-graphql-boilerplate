# -*- coding:utf-8 -*-
import graphene
from graphene import resolve_only_args
from graphene_gae import NdbObjectType

import models


class User(NdbObjectType):
    class Meta:
        model = models.User


class Query(graphene.ObjectType):
    user = graphene.Field(lambda: User, id=graphene.String())
    users = graphene.List(lambda: User)

    @resolve_only_args
    def resolve_user(self, id):
        return models.User.get_by_id(int(id))

    def resolve_users(self, args, context, info):
        return models.User.query()


schema = graphene.Schema(query=Query)
