from django.test import TestCase
from graphene_django.utils.testing import GraphQLTestCase
from mixer.backend.django import mixer
import graphene
import json

# Create your tests here.

from halo.schema import schema
from rangos.models import Rango

PRODUCCION_QUERY = '''{
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

class ProduccionTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    def setUp(self):
        self.rangos1 = mixer.blend(Rango)
        self.rangos2 = mixer.blend(Rango)
    
    def test_producciones_query(self):
        response = self.query(
            PRODUCCION_QUERY,
        )
        content = json.loads(response.content)
        #print(content)
        self.assertResponseNoErrors(response)
        print("query producciones results ")
        print(content)
        assert len(content['data']['rangos']) == 2