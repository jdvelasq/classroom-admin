# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
import fixer.constants
from fixer.base_shell import BaseShell
from fixer.colorized_prompt import make_colorized_prompt


class PredictivaaShell(BaseShell):

    prompt = make_colorized_prompt("fixer:none:none:none")

    def do_pre_01(self, arg):
        """Taller Presencial 01 - Hola mundo."""

        fixer.constants.assignment = "PRE-01"
        fixer.constants.prefix = "PRE-01-hola-mundo"
        fixer.constants.template = "TMPL_PRE_01_hola_mundo"
        return True

    def do_pre_02(self, arg):
        """Taller Presencial 02 — Despliegue de modelos de ML."""

        fixer.constants.assignment = "PRE-02"
        fixer.constants.prefix = "PRE-02-despliegue-de-modelos-de-ml"
        fixer.constants.template = "TMPL_PRE_02_despliegue_de_modelos_de_ml"
        return True

    def do_pre_03(self, arg):
        """Taller Presencial 03 — Implementación de modelos."""

        fixer.constants.assignment = "PRE-03"
        fixer.constants.prefix = "PRE-03-implementacion-de-modelos"
        fixer.constants.template = "TMPL_PRE_03_implementacion_de_modelos"
        return True

    def do_pre_04(self, arg):
        """Taller Presencial 04 — Clasificacion basica de imagenes."""

        fixer.constants.assignment = "PRE-04"
        fixer.constants.prefix = "PRE-04-clasificacion-basica-de-imagenes"
        fixer.constants.template = "TMPL_PRE_04_clasificacion_basica_de_imagenes"
        return True

    def do_pre_05(self, arg):
        """Taller Presencial 05 — Clasificacion basica de texto."""

        fixer.constants.assignment = "PRE-05"
        fixer.constants.prefix = "PRE-05-clasificacion-basica-de-texto"
        fixer.constants.template = "TMPL_PRE_05_clasificacion_basica_de_texto"
        return True

    def do_pre_06(self, arg):
        """Taller Presencial 06 — Regresion basica."""

        fixer.constants.assignment = "PRE-06"
        fixer.constants.prefix = "PRE-06-regresion-basica"
        fixer.constants.template = "TMPL_PRE_06_regresion_basica"
        return True

    def do_pre_07(self, arg):
        """Taller Presencial 07 — Optimizacion de Hiperparametros."""

        fixer.constants.assignment = "PRE-07"
        fixer.constants.prefix = "PRE-07-ajuste-de-hiperparametros"
        fixer.constants.template = "TMPL_PRE_07_ajuste_de_hiperparametros"
        return True

    def do_pre_08(self, arg):
        """Taller Presencial 08 — Pipelines."""

        fixer.constants.assignment = "PRE-08"
        fixer.constants.prefix = "PRE-08-pipelines"
        fixer.constants.template = "TMPL_PRE_08_pipelines"
        return True

    def do_pre_09(self, arg):
        """Taller Presencial 09 — SelectKBest para regresion."""

        fixer.constants.assignment = "PRE-09"
        fixer.constants.prefix = "PRE-09-selectkbest-para-regresion"
        fixer.constants.template = "TMPL_PRE_09_selectkbest_para_regresion"
        return True

    def do_pre_10(self, arg):
        """Taller Presencial 10 — SelectKBest para clasificacion."""

        fixer.constants.assignment = "PRE-10"
        fixer.constants.prefix = "PRE-10-selectkbest-para-clasificacion"
        fixer.constants.template = "TMPL_PRE_10_selectkbest_para_clasificacion"
        return True

    def do_pre_11(self, arg):
        """Taller Presencial 11 — Reduccion de la dimensionalidad digits."""

        fixer.constants.assignment = "PRE-11"
        fixer.constants.prefix = "PRE-11-reduccion-de-la-dimensionalidad-digits"
        fixer.constants.template = "TMPL_PRE_11_reduccion_de_la_dimensionalidad_digits"
        return True

    def do_pre_12(self, arg):
        """Taller Presencial 12 — Patrones de demanda diaria."""

        fixer.constants.assignment = "PRE-12"
        fixer.constants.prefix = "PRE-12-patrones-de-demanda-diaria"
        fixer.constants.template = "TMPL_PRE_12_patrones_de_demanda_diaria"
        return True

    def do_pre_13(self, arg):
        """Taller Presencial 13 — Prediccion basica de series de tiempo."""

        fixer.constants.assignment = "PRE-13"
        fixer.constants.prefix = "PRE-13-prediccion-basica-series-de-tiempo"
        fixer.constants.template = "TMPL_PRE_13_prediccion_basica_series_de_tiempo"
        return True

    def do_lab_01(self, arg):
        """Lab 01 - Prediccion del default usando bosques aleatorios."""
        fixer.constants.template = ""

        fixer.constants.assignment = "LAB-01"
        fixer.constants.prefix = "LAB-01-prediccion-del-default-usando-rf"
        fixer.constants.template = (
            "TMPL_LAB_01_prediccion_del_default_usando_bosques_aleatorios"
        )
        return True

    def do_lab_02(self, arg):
        """Lab 02 - Prediccion del default usando regresion logistica."""

        fixer.constants.assignment = "LAB-02"
        fixer.constants.prefix = "LAB-02-prediccion-del-default-usando-logreg"
        fixer.constants.template = "TMPL_LAB_02_prediccion_del_default_usando_logreg"
        return True

    def do_lab_03(self, arg):
        """Lab 03 - Prediccion del default usando maquinas de vectores de soporte."""

        fixer.constants.assignment = "LAB-03"
        fixer.constants.prefix = "LAB-03-prediccion-del-default-usando-svc"
        fixer.constants.template = "TMPL_LAB_03_prediccion_del_default_usando_svc"
        return True

    def do_lab_04(self, arg):
        """Lab 04 - Prediccion del default usando redes neuronales."""

        fixer.constants.assignment = "LAB-04"
        fixer.constants.prefix = "LAB-04-prediccion-del-default-usando-mlp"
        fixer.constants.template = "TMPL_LAB_04_prediccion_del_default_usando_mlp"
        return True

    def do_lab_05(self, arg):
        """Lab 05 - Prediccion de precios usando regresion lineal."""

        fixer.constants.assignment = "LAB-05"
        fixer.constants.prefix = "LAB-05-prediccion-de-precios-usando-linreg"
        fixer.constants.template = (
            "TMPL_LAB_05_prediccion_de_precios_usando_regresion_lineal"
        )
        return True
