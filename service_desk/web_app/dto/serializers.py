from rest_framework import serializers
from web_app.models import Cat_Equipo


class Cat_Equipo_Serializado(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    modelo = serializers.CharField()
    marca = serializers.CharField()
    num_serie = serializers.CharField()
    num_parte = serializers.CharField()
    procesador = serializers.CharField()
    ram = serializers.CharField()
    disco = serializers.CharField()
    comentario = serializers.CharField()

    def create(self, validated_data):
        return Cat_Equipo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.modelo = validated_data.get('modelo', instance.modelo)
        instance.marca = validated_data.get('marca', instance.marca)
        instance.num_serie = validated_data.get('num_serie', instance.num_serie)
        instance.num_parte = validated_data.get('num_parte', instance.num_parte)
        instance.procesador = validated_data.get('procesador', instance.procesador)
        instance.ram = validated_data.get('ram', instance.ram)
        instance.disco = validated_data.get('disco', instance.disco)
        instance.comentario = validated_data.get('comentario', instance.comentario)
        instance.save()
        return instance