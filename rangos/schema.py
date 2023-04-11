import graphene
from graphene_django import DjangoObjectType

from .models import Rango


class RangoType(DjangoObjectType):
    class Meta:
        model = Rango


class Query(graphene.ObjectType):
    rangos = graphene.List(RangoType)

    def resolve_rangos(self, info, **kwargs):
        return Rango.objects.all()
    
    
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
        

    #3
    def mutate(self, info, faccion, raza,rango,caracteristicas,peligrosidad,representantes,origen,especialidad,antiguedad):
        rango = Rango(faccion=faccion,raza=raza,rango=rango,caracteristicas=caracteristicas,
                      peligrosidad=peligrosidad,representantes=representantes,origen=origen,
                      especialidad=especialidad,antiguedad=antiguedad)
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
        )


#4l
class Mutation(graphene.ObjectType):
    create_rango = CreateRango.Field()    

schema = graphene.Schema(query=Query, mutation=Mutation)    