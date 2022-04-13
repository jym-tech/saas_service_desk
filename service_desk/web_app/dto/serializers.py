from rest_framework import serializers
from web_app.models import Cat_Equipo, Cat_Cliente, Cat_Servicio, Cat_Producto, Opr_Solicitud

# Usando Core Arguments para mapear todas propiedades de la entidad OPR_SOLICITUD
class Opr_Solicitud_Serializado(serializers.ModelSerializer):
    class Meta:
        model = Opr_Solicitud
        fields = "__all__"

# Usando Core Arguments para mapear todas propiedades de la entidad CAT_PRODUCTO
class Cat_Producto_Serializado(serializers.ModelSerializer):
    class Meta:
        model = Cat_Producto
        fields = "__all__"

# Usando Core Arguments para mapear todas propiedades de la entidad CAT_SERVICIO
class Cat_Servicio_Serializado(serializers.ModelSerializer):
    class Meta:
        model = Cat_Servicio
        fields = "__all__"

# Usando Core Arguments para mapear todas propiedades de la entidad CAT_CLIENTE
class Cat_Cliente_Serializado(serializers.ModelSerializer):
    #idCliente = Opr_Solicitud_Serializado(many=True, read_only=True)
    idCliente = serializers.StringRelatedField(many=True)
    class Meta:
        model = Cat_Cliente
        fields = "__all__"

# Usando Core Arguments para mapear todas propiedades de la entidad CAT_EQUIPO
class Cat_Equipo_Serializado(serializers.ModelSerializer):
    #idEquipo = Opr_Solicitud_Serializado(many=True, read_only=True)
    idEquipo = serializers.StringRelatedField(many=True)

    class Meta:
        model = Cat_Equipo
        fields = "__all__"
        # fields = ['id', 'modelo', 'marca']
        # exclude = ['id']




# longitud_num_serie = serializers.SerializerMethodField()
# def get_longitud_num_serie(self, object):
#     cantidad_caracteres = len(object.num_serie)
#     return cantidad_caracteres
#
# def validate_num_serie(self, dato):
#     if len(dato) < 2:
#         raise  serializers.ValidationError("El numero de serie es muy corto")
#     else:
#         return dato

# # Metodo para validar la longitud de una propiedad
# def longitud_campo(dato):
#     if len(dato) < 2:
#         raise serializers.ValidationError(f'El dato {dato} es demasiado corto')
#
# # Mapeo de los campos de la entidad CAT_EQUIPO
# class Cat_Equipo_Serializado(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     modelo = serializers.CharField(validators=[longitud_campo])
#     marca = serializers.CharField(validators=[longitud_campo])
#     num_serie = serializers.CharField(validators=[longitud_campo])
#     num_parte = serializers.CharField(validators=[longitud_campo])
#     procesador = serializers.CharField()
#     ram = serializers.CharField()
#     disco = serializers.CharField()
#     comentario = serializers.CharField()
#
#     def create(self, validated_data):
#         return Cat_Equipo.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.modelo = validated_data.get('modelo', instance.modelo)
#         instance.marca = validated_data.get('marca', instance.marca)
#         instance.num_serie = validated_data.get('num_serie', instance.num_serie)
#         instance.num_parte = validated_data.get('num_parte', instance.num_parte)
#         instance.procesador = validated_data.get('procesador', instance.procesador)
#         instance.ram = validated_data.get('ram', instance.ram)
#         instance.disco = validated_data.get('disco', instance.disco)
#         instance.comentario = validated_data.get('comentario', instance.comentario)
#         instance.save()
#         return instance
