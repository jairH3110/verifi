from graphene_django.utils.testing import GraphQLTestCase
from mixer.backend.django import mixer
import graphene
import json
import sys
sys.path.append("..")
from rangos.schema import schema 
from rangos.models import Rango

RANGOS_QUERY = '''
 {
   rangos{
    id
    faccion
    raza
    rango
    caracteristicas
    peligrosidad
    representantes
    origen
    especialidad
    antiguedad
  
  }
 }
 '''

CREATE_RANGO_MUTATION = '''
 mutation createRango($faccion: String ,$raza: String ,$rango: String ,$caracteristicas: String ,
  $peligrosidad: String , $representantes: String ,$origen: String ,$especialidad: String ,
  $antiguedad: String) {
     createRango(faccion: $faccion, raza: $raza , rango: $rango , caracteristicas: $caracteristicas , peligrosidad: $peligrosidad , representantes: $representantes , 
     origen: $origen , especialidad: $especialidad , antiguedad: $antiguedad) {
      
      faccion
      raza
      rango
      caracteristicas
      peligrosidad
      representantes
      origen
      especialidad
      antiguedad
     }
 }
'''

class LinkTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    def setUp(self):
        self.rango1 = mixer.blend(Rango)
        self.rango2 = mixer.blend(Rango)

    def test_links_query(self):
        response = self.query(
            RANGOS_QUERY,
        )


        content = json.loads(response.content)
        #print(content)
        # This validates the status code and if you get errores
        self.assertResponseNoErrors(response)
        print ("query rango results ")
        print (content)
        assert len(content['data']['rangos']) == 2


    def test_createRango_mutation(self):

        response = self.query(
            CREATE_RANGO_MUTATION,
            variables={'faccion':"covenant",'raza':"elites",'rango':"espada shangheli",'caracteristicas':"soldado elite",
  'peligrosidad':"alto",'representantes':"ladowir",'origen':"sanghelios",'especialidad':"ataques especiales",
  'antiguedad':"año 1300"}
        )
        print('mutation ')
        print(response)
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)
        self.assertDictEqual({"createRango": {'faccion':"covenant",'raza':"elites",'rango':"espada shangheli",'caracteristicas':"soldado elite",
  'peligrosidad':"alto",'representantes':"ladowir",'origen':"sanghelios",'especialidad':"ataques especiales",
  'antiguedad':"año 1300"}}, content['data'])

