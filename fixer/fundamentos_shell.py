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


class FundamentosShell(BaseShell):

    prompt = make_colorized_prompt("fixer:none:none:none")

    def do_pre_01(self, arg):
        """Taller Presencial 01 - Hola mundo."""

        fixer.constants.assignment = "PRE-01"
        fixer.constants.prefix = "PRE-01-hola-mundo"
        fixer.constants.template = "TMPL_PRE_01_hola_mundo"
        return True

    def do_pre_02(self, arg):
        """Taller Presencial 03 — Programación en Python MapReduce."""

        fixer.constants.assignment = "PRE-02"
        fixer.constants.prefix = "PRE-02-programacion-en-python-mapreduce"
        fixer.constants.template = "TMPL_PRE_02_programacion_en_python_mapreduce"
        return True

    def do_pre_03(self, arg):
        """Taller Presencial 03 — Consultas SQL en MapReduce."""

        fixer.constants.assignment = "PRE-03"
        fixer.constants.prefix = "PRE-03-consultas-sql-en-mapreduce"
        fixer.constants.template = "TMPL_PRE_03_consultas_sql_en_mapreduce"
        return True

    def do_pre_04(self, arg):
        """Taller Presencial 04 — WordCount con Pandas."""

        fixer.constants.assignment = "PRE-04"
        fixer.constants.prefix = "PRE-04-wordcount-con-pandas"
        fixer.constants.template = "TMPL_PRE_04_wordcount_con_pandas"
        return True

    def do_pre_05(self, arg):
        """Taller Presencial 05 — Subconjuntos de datos en Pandas."""

        fixer.constants.assignment = "PRE-05"
        fixer.constants.prefix = "PRE-05-subconjuntos-de-datos-en-pandas"
        fixer.constants.template = "TMPL_PRE_05_subconjuntos_de_datos_en_pandas"
        return True

    def do_pre_06(self, arg):
        """Taller Presencial 06 — Agrupamiento y filtrado en Pandas."""

        fixer.constants.assignment = "PRE-06"
        fixer.constants.prefix = "PRE-06-agrupamiento-y-filtrado-en-pandas"
        fixer.constants.template = "TMPL_PRE_06_agrupamiento_y_filtrado_en_pandas"
        return True

    def do_pre_07(self, arg):
        """Taller Presencial 07 — Manipulación de datos con ChatGPT."""

        fixer.constants.assignment = "PRE-07"
        fixer.constants.prefix = "PRE-07-manipulacion-de-datos-con-chatgpt"
        fixer.constants.template = "TMPL_PRE_07_manipulacion_de_datos_con_chatgpt"
        return True

    def do_pre_08(self, arg):
        """Taller Presencial 08 — Limpieza de texto fingerprint."""

        fixer.constants.assignment = "PRE-08"
        fixer.constants.prefix = "PRE-08-limpieza-de-texto-fingerprint"
        fixer.constants.template = "TMPL_PRE_08_limpieza_de_texto_fingerprint"
        return True

    def do_pre_09(self, arg):
        """Taller Presencial 09 — Limpieza de texto ngram."""

        fixer.constants.assignment = "PRE-09"
        fixer.constants.prefix = "PRE-09-limpieza-de-texto-ngrams"
        fixer.constants.template = "TMPL_PRE_09_limpieza_de_texto_ngrams"
        return True

    def do_pre_10(self, arg):
        """Taller Presencial 10 — Tokenización de texto."""

        fixer.constants.assignment = "PRE-10"
        fixer.constants.prefix = "PRE-10-tokenizacion-de-texto"
        fixer.constants.template = "TMPL_PRE_10_tokenizacion_de_texto"
        return True

    def do_pre_11(self, arg):
        """Taller Presencial 11 — Worldmap en Folium."""

        fixer.constants.assignment = "PRE-11"
        fixer.constants.prefix = "PRE-11-worldmap-en-folium"
        fixer.constants.template = "TMPL_PRE_11_worldmap_en_folium"
        return True

    def do_pre_12(self, arg):
        """Taller Presencial 12 — Matplotlib Networkx."""

        fixer.constants.assignment = "PRE-12"
        fixer.constants.prefix = "PRE-12-matplotlib-networkx"
        fixer.constants.template = "TMPL_PRE_12_matplotlib_networkx"
        return True

    def do_pre_13(self, arg):
        """Taller Presencial 13 — Bootstrapping."""

        fixer.constants.assignment = "PRE-13"
        fixer.constants.prefix = "PRE-13-bootstrapping"
        fixer.constants.template = "TMPL_PRE_13_bootstrapping"
        return True

    def do_pre_14(self, arg):
        """Taller Presencial 14 — Análisis de datos con Pandas."""

        fixer.constants.assignment = "PRE-14"
        fixer.constants.prefix = "PRE-14-analisis-de-datos-con-pandas"
        fixer.constants.template = "TMPL_PRE_14_analisis_de_datos_con_pandas"
        return True

    def do_pre_15(self, arg):
        """Taller Presencial 15 — Despliegue de modelos de ML."""

        fixer.constants.assignment = "PRE-15"
        fixer.constants.prefix = "PRE-15-despliegue-de-modelos-de-ml"
        fixer.constants.template = "TMPL_PRE_15_despliegue_de_modelos_de_ml"
        return True

    def do_pre_16(self, arg):
        """Taller Presencial 16 — Implementación de modelos."""

        fixer.constants.assignment = "PRE-16"
        fixer.constants.prefix = "PRE-16-implementacion-de-modelos-de-ml"
        fixer.constants.template = "TMPL_PRE_16_implementacion_de_modelos_de_ml"
        return True

    def do_pre_17(self, arg):
        """Taller Presencial 17 — Clasificacion basica de imagenes."""

        fixer.constants.assignment = "PRE-17"
        fixer.constants.prefix = "PRE-17-clasificacion-basica-de-imagenes"
        fixer.constants.template = "TMPL_PRE_17_clasificacion_basica_de_imagenes"
        return True

    def do_pre_18(self, arg):
        """Taller Presencial 18 — Clasificacion basica de texto."""

        fixer.constants.assignment = "PRE-18"
        fixer.constants.prefix = "PRE-18-clasificacion-basica-de-texto"
        fixer.constants.template = "TMPL_PRE_18_clasificacion_basica_de_texto"
        return True

    def do_pre_19(self, arg):
        """Taller Presencial 19 — Regresion basica."""

        fixer.constants.assignment = "PRE-19"
        fixer.constants.prefix = "PRE-19-regresion-basica"
        fixer.constants.template = "TMPL_PRE_19_regresion_basica"
        return True

    def do_pre_20(self, arg):
        """Taller Presencial 20 — Optimizacion de Hiperparametros."""

        fixer.constants.assignment = "PRE-20"
        fixer.constants.prefix = "PRE-20-ajuste-de-hiperparametros"
        fixer.constants.template = "TMPL_PRE_20_ajuste_de_hiperparametros"
        return True

    def do_pre_21(self, arg):
        """Taller Presencial 21 — Pipelines."""

        fixer.constants.assignment = "PRE-21"
        fixer.constants.prefix = "PRE-21-pipelines"
        fixer.constants.template = "TMPL_PRE_21_pipelines"
        return True

    def do_pre_22(self, arg):
        """Taller Presencial 22 — SelectKBest para regresion."""

        fixer.constants.assignment = "PRE-22"
        fixer.constants.prefix = "PRE-22-selectkbest-para-regresion"
        fixer.constants.template = "TMPL_PRE_22_selectkbest_para_regresion"
        return True

    def do_pre_23(self, arg):
        """Taller Presencial 23 — SelectKBest para clasificacion."""

        fixer.constants.assignment = "PRE-23"
        fixer.constants.prefix = "PRE-23-selectkbest-para-clasificacion"
        fixer.constants.template = "TMPL_PRE_23_selectkbest_para_clasificacion"
        return True

    def do_pre_24(self, arg):
        """Taller Presencial 24 — Reduccion de la dimensionalidad digits."""

        fixer.constants.assignment = "PRE-24"
        fixer.constants.prefix = "PRE-24-reduccion-de-la-dimensionalidad-digits"
        fixer.constants.template = "TMPL_PRE_24_reduccion_de_la_dimensionalidad_digits"
        return True

    def do_pre_25(self, arg):
        """Taller Presencial 25 — Patrones de demanda diaria."""

        fixer.constants.assignment = "PRE-25"
        fixer.constants.prefix = "PRE-25-patrones-de-demanda-diaria"
        fixer.constants.template = "TMPL_PRE_25_patrones_de_demanda_diaria"
        return True

    def do_pre_26(self, arg):
        """Taller Presencial 26 — Visualización de la estructura del mercado."""

        fixer.constants.assignment = "PRE-26"
        fixer.constants.prefix = "PRE-26-visualizacion-mercado-accionario"
        fixer.constants.template = "TMPL_PRE_26_visualizacion_mercado_accionario"
        return True

    def do_pre_27(self, arg):
        """Taller Presencial 27 — Prediccion basica de series de tiempo."""

        fixer.constants.assignment = "PRE-27"
        fixer.constants.prefix = "PRE-27-prediccion-basica-series-de-tiempo"
        fixer.constants.template = "TMPL_PRE_27_prediccion_basica_series_de_tiempo"
        return True

    def do_lab_01(self, arg):
        """Lab 01 — Programacion básica en Python."""

        fixer.constants.assignment = "LAB-01"
        fixer.constants.prefix = "LAB-01-python-basico"
        fixer.constants.template = "TMPL_LAB_01_python_basico"
        return True

    def do_lab_02(self, arg):
        """Lab 02 — Pandas."""

        fixer.constants.assignment = "LAB-02"
        fixer.constants.prefix = "LAB-02-pandas"
        fixer.constants.template = "TMPL_LAB_02_pandas"
        return True

    def do_lab_03(self, arg):
        """Lab 03 — Ingestión de texto plano."""

        fixer.constants.assignment = "LAB-03"
        fixer.constants.prefix = "LAB-03-ingestion-de-texto-plano"
        fixer.constants.template = "TMPL_LAB_03_ingestion_de_texto_plano"
        return True

    def do_lab_04(self, arg):
        """Lab 04 — Ingestión de texto en directorios."""

        fixer.constants.assignment = "LAB-04"
        fixer.constants.prefix = "LAB-04-ingestion-de-texto-en-directorios"
        fixer.constants.template = "TMPL_LAB_04_ingestion_de_texto_en_directorios"
        return True

    def do_lab_05(self, arg):
        """Lab 05 — Limpieza de datos de campañas de marketing."""

        fixer.constants.assignment = "LAB-05"
        fixer.constants.prefix = "LAB-05-limpieza-de-datos-de-campa-as-de-marketing"
        fixer.constants.template = (
            "TMPL_LAB_05_limpieza_de_datos_de_campanas_de_marketing"
        )
        return True

    def do_lab_06(self, arg):
        """Lab 06 — Limpieza de datos de solicitudes de credito."""

        fixer.constants.assignment = "LAB-06"
        fixer.constants.prefix = "LAB-06-limpieza-de-datos-de-solicitudes-de-credito"
        fixer.constants.template = (
            "TMPL_LAB_06_limpieza_de_datos_de_solicitudes_de_credito"
        )
        return True

    def do_lab_07(self, arg):
        """Lab 07 — Matplotlib news plot."""

        fixer.constants.assignment = "LAB-07"
        fixer.constants.prefix = "LAB-07-matplotlib-news-plot"
        fixer.constants.template = "TMPL_LAB_07_matplotlib_news_plot"
        return True

    def do_lab_08(self, arg):
        """Lab 08 — Matplotlib dashboard."""

        fixer.constants.assignment = "LAB-08"
        fixer.constants.prefix = "LAB-08-matplotlib-dashboard"
        fixer.constants.template = "TMPL_LAB_08_matplotlib_dashboard"
        return True

    def do_lab_09(self, arg):
        """Lab 09 - Prediccion del default usando bosques aleatorios."""

        fixer.constants.assignment = "LAB-09"
        fixer.constants.prefix = "LAB-09-prediccion-del-default-usando-rf"
        fixer.constants.template = (
            "TMPL_LAB_09_prediccion_del_default_usando_bosques_aleatorios"
        )
        return True

    def do_lab_10(self, arg):
        """Lab 10 - Prediccion del default usando regresion logistica."""

        fixer.constants.assignment = "LAB-10"
        fixer.constants.prefix = "LAB-10-prediccion-del-default-usando-logreg"
        fixer.constants.template = "TMPL_LAB_10_prediccion_del_default_usando_logreg"
        return True

    def do_lab_11(self, arg):
        """Lab 11 - Prediccion del default usando maquinas de vectores de soporte."""

        fixer.constants.assignment = "LAB-11"
        fixer.constants.prefix = "LAB-11-prediccion-del-default-usando-svc"
        fixer.constants.template = "TMPL_LAB_11_prediccion_del_default_usando_svc"
        return True

    def do_lab_12(self, arg):
        """Lab 12 - Prediccion del default usando redes neuronales."""

        fixer.constants.assignment = "LAB-12"
        fixer.constants.prefix = "LAB-12-prediccion-del-default-usando-mlp"
        fixer.constants.template = "TMPL_LAB_12_prediccion_del_default_usando_mlp"
        return True

    def do_lab_13(self, arg):
        """Lab 13 - Prediccion de precios usando regresion lineal."""

        fixer.constants.assignment = "LAB-13"
        fixer.constants.prefix = "LAB-13-prediccion-de-precios-usando-regresion-lineal"
        fixer.constants.template = (
            "TMPL_LAB_13_prediccion_de_precios_usando_regresion_lineal"
        )
        return True
