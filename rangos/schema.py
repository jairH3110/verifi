import graphene
from graphene_django import DjangoObjectType
from users.schema import UserType
from .models import Rango, Vote
from graphql import GraphQLError
from django.db.models import Q

class RangoType(DjangoObjectType):
    class Meta:
        model = Rango

class VoteType(DjangoObjectType):
    class Meta:
        model = Vote


class Query(graphene.ObjectType):
    rangos = graphene.List(RangoType,search=graphene.String())
    votes = graphene.List(VoteType)

    def resolve_rangos(self, info , search=None, **kwargs):
        if search:
            filter = (
                Q(faccion__icontains=search) |
                Q(raza__icontains=search) |
                Q(rango__icontains=search) |
                Q(caracteristicas__icontains=search) |
                Q(peligrosidad__icontains=search) |
                Q(representantes__icontains=search) |
                Q(origen__icontains=search) |
                Q(especialidad__icontains=search) |
                Q(antiguedad__icontains=search) |
                Q(comentarios__icontains=search)  
            )
            return Rango.objects.filter(filter)


        return Rango.objects.all()
    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()
    
    
class CreateRango(graphene.Mutation):
    id = graphene.Int()
    faccion = graphene.String()
    raza = graphene.String()
    rango = graphene.String()
    caracteristicas = graphene.String()
    peligrosidad = graphene.String()
    representantes = graphene.String()
    origen = graphene.String()
    especialidad = graphene.String()
    antiguedad = graphene.String()
    comentarios = graphene.String()
    posted_by = graphene.Field(UserType)
   

    #2
    class Arguments:
            faccion = graphene.String()
            raza = graphene.String()
            rango = graphene.String()
            caracteristicas = graphene.String()
            peligrosidad = graphene.String()
            representantes = graphene.String()
            origen = graphene.String()
            especialidad = graphene.String()
            antiguedad = graphene.String()
            comentarios = graphene.String()
        

    #3
    def mutate(self, info, faccion, raza,rango,caracteristicas,peligrosidad,representantes,origen,especialidad,antiguedad,comentarios):
        user = info.context.user or None
        rango = Rango(faccion=faccion,raza=raza,rango=rango,caracteristicas=caracteristicas,
                      peligrosidad=peligrosidad,representantes=representantes,origen=origen,
                      especialidad=especialidad,antiguedad=antiguedad,comentarios=comentarios,posted_by=user,)
        
        rango.save()

        return CreateRango(
            id=rango.id,
            faccion=rango.faccion,
            raza=rango.raza,
            rango=rango.rango,
            caracteristicas=rango.caracteristicas,
            peligrosidad=rango.peligrosidad,
            representantes=rango.representantes,
            origen=rango.origen,
            especialidad=rango.especialidad,
            antiguedad=rango.antiguedad,
            comentarios=rango.comentarios,
            posted_by=rango.posted_by,
        )




class CreateVote(graphene.Mutation):
    user = graphene.Field(UserType)
    rango = graphene.Field(RangoType)

    class Arguments:
        rango_id = graphene.Int()

    def mutate(self, info, rango_id):
        user = info.context.user
        
        if user.is_anonymous:
            
            raise GraphQLError('You must be logged to vote!')


        rango = Rango.objects.filter(id=rango_id).first()
        if not rango:
            raise Exception('Invalid Link!')

        Vote.objects.create(
            user=user,
            rango=rango,
        )

        return CreateVote(user=user, rango=rango)



#4l
class Mutation(graphene.ObjectType):
    create_rango = CreateRango.Field()
    create_vote = CreateVote.Field()    

schema = graphene.Schema(query=Query, mutation=Mutation)    