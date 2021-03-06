from django.db.models import Sum
from django.db.models.functions import Coalesce
from rest_framework import serializers

from web_app.models import Cat_Equipo, Cat_Cliente, Cat_Servicio, Cat_Producto, Opr_Solicitud, Opr_Cotizacion


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

# Usando Core Arguments para mapear todas propiedades de la entidad OPR_COTIZACION
class Opr_Cotizacion_Serializado(serializers.ModelSerializer):
    # productos_cotizacion = Cat_Producto_Serializado(many=True, read_only=False)
    # servicios_cotizacion = Cat_Servicio_Serializado(many=True, read_only=False)
    # productos_cotizacion = serializers.StringRelatedField(many=True)
    # servicios_cotizacion = serializers.StringRelatedField(many=True)
    # total = serializers.SerializerMethodField()
    total = serializers.FloatField(read_only=True)

    class Meta:
        model = Opr_Cotizacion
        fields = "__all__"
        # extra_kwargs = {'productos_cotizacion': {'required': False}, 'servicios_cotizacion': {'required': False}}

    # def create(self, validated_data):
    #     productos = validated_data.pop('productos_cotizacion')
    #     instancia = Opr_Cotizacion.objects.create(**validated_data)
    #     for producto in productos:
    #         instancia.productos.add(producto)
    #     return instancia

    # def update(self, instance, validated_data):
    #     productos_data = validated_data.pop('productos_cotizacion')
    #     instance = super(Opr_Cotizacion_Serializado, self).update(instance, validated_data)
    #
    #     for productos_data in productos_data:
    #         productos_qs = Cat_Producto.objects.filter(id__iexact=productos_data['id'])
    #
    #         if productos_qs.exist():
    #             productos_cotizacion = productos_qs.first()
    #         else:
    #             productos_cotizacion = Cat_Producto.objects.create(**productos_data)
    #
    #         instance.productos_cotizacion.add(productos_cotizacion)
    #     return instance

    # def get_total(self, object):
        # total_productos = Opr_Cotizacion.objects.filter(pk=object.pk).aggregate(
        #     total_productos=Sum('productos_cotizacion__costo_producto'))
        # total_servicios = Opr_Cotizacion.objects.filter(pk=object.pk).aggregate(
        #     total_servicios=Sum('servicios_cotizacion__costo_servicio'))
        # return total_productos, total_servicios
        # total = Opr_Cotizacion.objects.filter(pk=object.pk).aggregate(
        #     total_cotizacion=Sum(Coalesce('productos_cotizacion__costo_producto',
        #                                   'servicios_cotizacion__costo_servicio')))
        # return total


# Usando Core Arguments para mapear todas propiedades de la entidad CAT_CLIENTE
class Cat_Cliente_Serializado(serializers.HyperlinkedModelSerializer):
    # cliente_solicitud = Opr_Solicitud_Serializado(many=True, read_only=True)
    # cliente_solicitud = serializers.StringRelatedField(many=True)
    # cliente_solicitud = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    cliente_solicitud = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        lookup_field='id',
        view_name='solicitud-detail'
    )
    url = serializers.HyperlinkedIdentityField(
        view_name='cliente-detail',
        lookup_field='id'
    )

    cliente_cotizacion = Opr_Cotizacion_Serializado(many=True, read_only=True)


    class Meta:
        model = Cat_Cliente
        fields = "__all__"
        # fields = ['id']

# Usando Core Arguments para mapear todas propiedades de la entidad CAT_EQUIPO
class Cat_Equipo_Serializado(serializers.HyperlinkedModelSerializer):
    # equipo_solicitud = Opr_Solicitud_Serializado(many=True, read_only=True)
    # equipo_solicitud = serializers.StringRelatedField(many=True)
    # equipo_solicitud = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    equipo_solicitud = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        lookup_field='id',
        view_name='solicitud-detail'
    )
    url = serializers.HyperlinkedIdentityField(
        view_name='equipo-detail',
        lookup_field='id'
    )
    equipo_cotizacion = Opr_Cotizacion_Serializado(many=True, read_only=True)

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
