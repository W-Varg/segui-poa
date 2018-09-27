from rest_framework.serializers import ModelSerializer
from poa.models import Cargo, Persona, Unidad, Usuarios, Gestion, Programa, Lugar, Proyectoactividad, Financiamiento, Frentes, Localizacion, Operacion, Empresa, Seguimiento, Responsables, DetalleSeguimiento, Contrato, Ordendecambio, Ejecucion, EjecucionFinanciera, EjecucionFisica, Galeria, Configuracion


class CargoSerializer(ModelSerializer):

    class Meta:
        model = Cargo
        fields = '__all__'


class PersonaSerializer(ModelSerializer):

    class Meta:
        model = Persona
        fields = '__all__'


class UnidadSerializer(ModelSerializer):

    class Meta:
        model = Unidad
        fields = '__all__'


class UsuariosSerializer(ModelSerializer):

    class Meta:
        model = Usuarios
        fields = '__all__'


class GestionSerializer(ModelSerializer):

    class Meta:
        model = Gestion
        fields = '__all__'


class ProgramaSerializer(ModelSerializer):

    class Meta:
        model = Programa
        fields = '__all__'


class LugarSerializer(ModelSerializer):

    class Meta:
        model = Lugar
        fields = '__all__'


class ProyectoactividadSerializer(ModelSerializer):

    class Meta:
        model = Proyectoactividad
        fields = '__all__'


class FinanciamientoSerializer(ModelSerializer):

    class Meta:
        model = Financiamiento
        fields = '__all__'


class FrentesSerializer(ModelSerializer):

    class Meta:
        model = Frentes
        fields = '__all__'


class LocalizacionSerializer(ModelSerializer):

    class Meta:
        model = Localizacion
        fields = '__all__'


class OperacionSerializer(ModelSerializer):

    class Meta:
        model = Operacion
        fields = '__all__'


class EmpresaSerializer(ModelSerializer):

    class Meta:
        model = Empresa
        fields = '__all__'


class SeguimientoSerializer(ModelSerializer):

    class Meta:
        model = Seguimiento
        fields = '__all__'


class ResponsablesSerializer(ModelSerializer):

    class Meta:
        model = Responsables
        fields = '__all__'


class DetalleSeguimientoSerializer(ModelSerializer):

    class Meta:
        model = DetalleSeguimiento
        fields = '__all__'


class ContratoSerializer(ModelSerializer):

    class Meta:
        model = Contrato
        fields = '__all__'


class OrdendecambioSerializer(ModelSerializer):

    class Meta:
        model = Ordendecambio
        fields = '__all__'


class EjecucionSerializer(ModelSerializer):

    class Meta:
        model = Ejecucion
        fields = '__all__'


class EjecucionFinancieraSerializer(ModelSerializer):

    class Meta:
        model = EjecucionFinanciera
        fields = '__all__'


class EjecucionFisicaSerializer(ModelSerializer):

    class Meta:
        model = EjecucionFisica
        fields = '__all__'


class GaleriaSerializer(ModelSerializer):

    class Meta:
        model = Galeria
        fields = '__all__'


class ConfiguracionSerializer(ModelSerializer):

    class Meta:
        model = Configuracion
        fields = '__all__'
