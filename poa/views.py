from rest_framework.viewsets import ModelViewSet
from poa.serializers import CargoSerializer, PersonaSerializer, UnidadSerializer, UsuariosSerializer, GestionSerializer, ProgramaSerializer, LugarSerializer, ProyectoactividadSerializer, FinanciamientoSerializer, FrentesSerializer, LocalizacionSerializer, OperacionSerializer, EmpresaSerializer, SeguimientoSerializer, ResponsablesSerializer, DetalleSeguimientoSerializer, ContratoSerializer, OrdendecambioSerializer, EjecucionSerializer, EjecucionFinancieraSerializer, EjecucionFisicaSerializer, GaleriaSerializer, ConfiguracionSerializer
from poa.models import Cargo, Persona, Unidad, Usuarios, Gestion, Programa, Lugar, Proyectoactividad, Financiamiento, Frentes, Localizacion, Operacion, Empresa, Seguimiento, Responsables, DetalleSeguimiento, Contrato, Ordendecambio, Ejecucion, EjecucionFinanciera, EjecucionFisica, Galeria, Configuracion


class CargoViewSet(ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer


class PersonaViewSet(ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class UnidadViewSet(ModelViewSet):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer


class UsuariosViewSet(ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer


class GestionViewSet(ModelViewSet):
    queryset = Gestion.objects.all()
    serializer_class = GestionSerializer


class ProgramaViewSet(ModelViewSet):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer


class LugarViewSet(ModelViewSet):
    queryset = Lugar.objects.all()
    serializer_class = LugarSerializer


class ProyectoactividadViewSet(ModelViewSet):
    queryset = Proyectoactividad.objects.all()
    serializer_class = ProyectoactividadSerializer


class FinanciamientoViewSet(ModelViewSet):
    queryset = Financiamiento.objects.all()
    serializer_class = FinanciamientoSerializer


class FrentesViewSet(ModelViewSet):
    queryset = Frentes.objects.all()
    serializer_class = FrentesSerializer


class LocalizacionViewSet(ModelViewSet):
    queryset = Localizacion.objects.all()
    serializer_class = LocalizacionSerializer


class OperacionViewSet(ModelViewSet):
    queryset = Operacion.objects.all()
    serializer_class = OperacionSerializer


class EmpresaViewSet(ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer


class SeguimientoViewSet(ModelViewSet):
    queryset = Seguimiento.objects.all()
    serializer_class = SeguimientoSerializer


class ResponsablesViewSet(ModelViewSet):
    queryset = Responsables.objects.all()
    serializer_class = ResponsablesSerializer


class DetalleSeguimientoViewSet(ModelViewSet):
    queryset = DetalleSeguimiento.objects.all()
    serializer_class = DetalleSeguimientoSerializer


class ContratoViewSet(ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer


class OrdendecambioViewSet(ModelViewSet):
    queryset = Ordendecambio.objects.all()
    serializer_class = OrdendecambioSerializer


class EjecucionViewSet(ModelViewSet):
    queryset = Ejecucion.objects.all()
    serializer_class = EjecucionSerializer


class EjecucionFinancieraViewSet(ModelViewSet):
    queryset = EjecucionFinanciera.objects.all()
    serializer_class = EjecucionFinancieraSerializer


class EjecucionFisicaViewSet(ModelViewSet):
    queryset = EjecucionFisica.objects.all()
    serializer_class = EjecucionFisicaSerializer


class GaleriaViewSet(ModelViewSet):
    queryset = Galeria.objects.all()
    serializer_class = GaleriaSerializer


class ConfiguracionViewSet(ModelViewSet):
    queryset = Configuracion.objects.all()
    serializer_class = ConfiguracionSerializer
