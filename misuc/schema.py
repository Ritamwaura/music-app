import graphene

import traditioapp.schema


class Query(traditioapp.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)