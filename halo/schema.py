import graphene

import rangos.schema


class Query(rangos.schema.Query, graphene.ObjectType):
    pass



class Mutation(rangos.schema.Mutation, graphene.ObjectType):
    pass



schema = graphene.Schema(query=Query, mutation=Mutation)