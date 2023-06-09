import graphene
from graphene_django import DjangoObjectType
from .models import Usuario
from django.db.models import Q


class UsuarioType(DjangoObjectType):
    class Meta:
        model = Usuario


class Query(graphene.ObjectType):
    usuarios = graphene.List(UsuarioType, search= graphene.String())


    def resolve_usuarios(self, info, search=None, **kwargs):
        if search:
            filter = (
                Q(usuario__icontains=search) |
                Q(modelo__icontains=search) |
                Q(prompt__icontains=search) |
                Q(resultado__icontains=search) |
                Q(fecha__icontains=search) 
            )
            return Usuario.objects.filter(filter)

        return Usuario.objects.all()




        return Usuario.objects.all()
    

#empieza create user 
class CreateUsuario(graphene.Mutation):
    id = graphene.Int()
    usuario = graphene.String()
    modelo = graphene.String()
    prompt = graphene.String()
    resultado = graphene.String()
    fecha = graphene.String()
    
  

    #2
    class Arguments:
        usuario = graphene.String()
        modelo = graphene.String()
        prompt = graphene.String()
        resultado = graphene.String()
        fecha = graphene.String()
    

    #3
    def mutate(self, info, usuario,modelo,prompt,resultado,fecha):
        usuario = Usuario(usuario=usuario,modelo = modelo, prompt = prompt, resultado = resultado, fecha = fecha)
        usuario.save()

        return CreateUsuario(
            id=usuario.id,
            usuario = usuario.usuario,
            modelo=usuario.modelo,
            prompt =usuario.prompt,
            resultado =usuario.resultado,
            fecha =usuario.fecha,

        )


class Mutation(graphene.ObjectType):
    create_usuario = CreateUsuario.Field()