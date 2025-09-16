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


class DescriptivaShell(BaseShell):

    prompt = make_colorized_prompt("fixer:none:none:none")

    def do_pre_01(self, arg):
        """Taller Presencial 01 - Hola mundo."""

        fixer.constants.assignment = "PRE-01"
        fixer.constants.prefix = "PRE-01-hola-mundo"
        fixer.constants.template = "TMPL_PRE_01_hola_mundo"
        return True

    def do_pre_02(self, arg):
        """Taller Presencial 02 — Maquina Enigma."""

        fixer.constants.assignment = "PRE-02"
        fixer.constants.prefix = "PRE-02-maquina-enigma"
        fixer.constants.template = "TMPL_PRE_02_maquina_enigma"
        return True

    def do_pre_03(self, arg):
        """Taller Presencial 03 — Programación en Python MapReduce."""

        fixer.constants.assignment = "PRE-03"
        fixer.constants.prefix = "PRE-03-programacion-en-python-mapreduce"
        fixer.constants.template = "TMPL_PRE_03_programacion_en_python_mapreduce"
        return True

    def do_pre_04(self, arg):
        """Taller Presencial 04 — Consultas SQL en MapReduce."""

        fixer.constants.assignment = "PRE-04"
        fixer.constants.prefix = "PRE-04-consultas-sql-en-mapreduce"
        fixer.constants.template = "TMPL_PRE_04_consultas_sql_en_mapreduce"
        return True

    def do_pre_05(self, arg):
        """Taller Presencial 05 — Programación en Python Multiprocessing."""

        fixer.constants.assignment = "PRE-05"
        fixer.constants.prefix = "PRE-05-programacion-en-python-multiprocessing"
        fixer.constants.template = "TMPL_PRE_05_programacion_en_python_multiprocessing"
        return True

    def do_pre_06(self, arg):
        """Taller Presencial 06 — Python csv2json."""

        fixer.constants.assignment = "PRE-06"
        fixer.constants.prefix = "PRE-06-python-csv2json"
        fixer.constants.template = "TMPL_PRE_06_python_csv2json"
        return True

    def do_pre_07(self, arg):
        """Taller Presencial 07 — Datos sinteticos con faker."""

        fixer.constants.assignment = "PRE-07"
        fixer.constants.prefix = "PRE-07-datos-sinteticos-con-faker"
        fixer.constants.template = "TMPL_PRE_07_datos_sinteticos_con_faker"
        return True

    def do_pre_08(self, arg):
        """Taller Presencial 08 — WordCount con Pandas."""

        fixer.constants.assignment = "PRE-08"
        fixer.constants.prefix = "PRE-08-wordcount-con-pandas"
        fixer.constants.template = "TMPL_PRE_08_wordcount_con_pandas"
        return True

    def do_pre_09(self, arg):
        """Taller Presencial 09 — Subconjuntos de datos en Pandas."""

        fixer.constants.assignment = "PRE-09"
        fixer.constants.prefix = "PRE-09-subconjuntos-de-datos-en-pandas"
        fixer.constants.template = "TMPL_PRE_09_subconjuntos_de_datos_en_pandas"
        return True

    def do_pre_10(self, arg):
        """Taller Presencial 10 — Agrupamiento y filtrado en Pandas."""

        fixer.constants.assignment = "PRE-10"
        fixer.constants.prefix = "PRE-10-agrupamiento-y-filtrado-en-pandas"
        fixer.constants.template = "TMPL_PRE_10_agrupamiento_y_filtrado_en_pandas"
        return True

    def do_pre_11(self, arg):
        """Taller Presencial 11 — Manipulación de datos con ChatGPT."""

        fixer.constants.assignment = "PRE-11"
        fixer.constants.prefix = "PRE-11-manipulacion-de-datos-con-chatgpt"
        fixer.constants.template = "TMPL_PRE_11_manipulacion_de_datos_con_chatgpt"
        return True

    def do_pre_12(self, arg):
        """Taller Presencial 12 — Limpieza de texto fingerprint."""

        fixer.constants.assignment = "PRE-12"
        fixer.constants.prefix = "PRE-12-limpieza-de-texto-fingerprint"
        fixer.constants.template = "TMPL_PRE_12_limpieza_de_texto_fingerprint"
        return True

    def do_pre_13(self, arg):
        """Taller Presencial 13 — Limpieza de texto ngram."""

        fixer.constants.assignment = "PRE-13"
        fixer.constants.prefix = "PRE-13-limpieza-de-datos-ngrams"
        fixer.constants.template = "TMPL_PRE_13_limpieza_de_texto_ngrams"
        return True

    def do_pre_14(self, arg):
        """Taller Presencial 14 — Tokenización de texto."""

        fixer.constants.assignment = "PRE-14"
        fixer.constants.prefix = "PRE-14-tokenizacion-de-texto"
        fixer.constants.template = "TMPL_PRE_14_tokenizacion_de_texto"
        return True

    def do_pre_15(self, arg):
        """Taller Presencial 15 — Worldmap en Folium."""

        fixer.constants.assignment = "PRE-15"
        fixer.constants.prefix = "PRE-15-worldmap-en-folium"
        fixer.constants.template = "TMPL_PRE_15_worldmap_en_folium"
        return True

    def do_pre_16(self, arg):
        """Taller Presencial 16 — Matplotlib Networkx."""

        fixer.constants.assignment = "PRE-16"
        fixer.constants.prefix = "PRE-16-matplotlib-networkx"
        fixer.constants.template = "TMPL_PRE_16_matplotlib_networkx"
        return True

    def do_pre_17(self, arg):
        """Taller Presencial 17 — Visualización de precios de bolsa."""

        fixer.constants.assignment = "PRE-17"
        fixer.constants.prefix = "PRE-17-visualizacion-de-precios-de-bolsa"
        fixer.constants.template = "TMPL_PRE_17_visualizacion_de_precios_de_bolsa"
        return True

    def do_pre_18(self, arg):
        """Taller Presencial 18 — Análisis de datos con Pandas."""

        fixer.constants.assignment = "PRE-18"
        fixer.constants.prefix = "PRE-18-analisis-de-datos-con-pandas"
        fixer.constants.template = "TMPL_PRE_18_analisis_de_datos_con_pandas"
        return True

    def do_pre_19(self, arg):
        """Taller Presencial 19 — SQLite web app."""

        fixer.constants.assignment = "PRE-19"
        fixer.constants.prefix = "PRE-19-sqlite-web-app"
        fixer.constants.template = "TMPL_PRE_19_sqlite_web_app"
        return True

    def do_lab_01(self, arg):
        """Lab 01 — Programacion básica en Python."""

        fixer.constants.assignment = "LAB-01"
        fixer.constants.prefix = "LAB-01-programacion-basica-en-python"
        fixer.constants.template = "TMPL_LAB_01_programacion_basica_en_python"
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
        fixer.constants.prefix = "LAB-05-limpieza-de-datos-de-campanas-de-marketing"
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
        """Lab 09 — SQL con SQlite."""

        fixer.constants.assignment = "LAB-09"
        fixer.constants.prefix = "LAB-09-sql-con-sqlite"
        fixer.constants.template = "TMPL_LAB_09_sql_con_sqlite"
        return True
