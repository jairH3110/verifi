import graphene
import users.schema
import rangos.schema
import usuarios.schema
import graphene
import graphql_jwt

class Query(users.schema.Query,rangos.schema.Query ,usuarios.schema.Query, graphene.ObjectType):
    pass



class Mutation(users.schema.Mutation,rangos.schema.Mutation,usuarios.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    pass



schema = graphene.Schema(query=Query, mutation=Mutation)