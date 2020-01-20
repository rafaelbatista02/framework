from rest_framework import serializers
from gatinho.models import Gatinho, Anuncio

class GatinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gatinho # nome da classe feita ai encima, no caso Contato
        fields = "__all__" # vai puchar todos os atributos da model , o (all) diz que estou trazendo todos o campos da model.


class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = "__all__"