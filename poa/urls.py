from rest_framework.routers import SimpleRouter
from poa import views


router = SimpleRouter()

router.register(r'cargo', views.CargoViewSet)
router.register(r'persona', views.PersonaViewSet)
router.register(r'unidad', views.UnidadViewSet)
router.register(r'usuarios', views.UsuariosViewSet)
router.register(r'gestion', views.GestionViewSet)
router.register(r'programa', views.ProgramaViewSet)
router.register(r'lugar', views.LugarViewSet)
router.register(r'proyectoactividad', views.ProyectoactividadViewSet)
router.register(r'financiamiento', views.FinanciamientoViewSet)
router.register(r'frentes', views.FrentesViewSet)
router.register(r'localizacion', views.LocalizacionViewSet)
router.register(r'operacion', views.OperacionViewSet)
router.register(r'empresa', views.EmpresaViewSet)
router.register(r'seguimiento', views.SeguimientoViewSet)
router.register(r'responsables', views.ResponsablesViewSet)
router.register(r'detalleseguimiento', views.DetalleSeguimientoViewSet)
router.register(r'contrato', views.ContratoViewSet)
router.register(r'ordendecambio', views.OrdendecambioViewSet)
router.register(r'ejecucion', views.EjecucionViewSet)
router.register(r'ejecucionfinanciera', views.EjecucionFinancieraViewSet)
router.register(r'ejecucionfisica', views.EjecucionFisicaViewSet)
router.register(r'galeria', views.GaleriaViewSet)
router.register(r'configuracion', views.ConfiguracionViewSet)

urlpatterns = router.urls
