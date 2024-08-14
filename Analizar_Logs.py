import pandas as pd
from docx import Document
import streamlit as st

def analizar_logs_error_y_generar_informe(df):
    if 'Severidad' not in df.columns:
        st.error("La columna 'Severidad' no se encuentra en el archivo.")
        return

    errores_df = df[df['Severidad'] == 'ERROR']

    if errores_df.empty:
        st.warning("No se encontraron registros con severidad 'ERROR'.")
    else:
        nombre_archivo_errores = 'Errores_Detectados.xlsx'
        errores_df.to_excel(nombre_archivo_errores, index=False)
        st.success(f"Archivo Excel con registros de ERROR generado exitosamente en {nombre_archivo_errores}.")
        st.download_button(label="Descargar Excel de Errores", data=open(nombre_archivo_errores, 'rb'), file_name=nombre_archivo_errores)

        doc = Document()
        doc.add_heading('Informe Técnico de Auditoría de Sistemas: Análisis de Logs de Error', level=1)

        doc.add_heading('1. Introducción', level=2)
        doc.add_paragraph(
            "Este informe presenta un análisis detallado de los registros de error críticos identificados "
            "durante la auditoría, con el objetivo de mejorar las medidas de seguridad y responder "
            "efectivamente a incidentes futuros. El propósito es asegurar la integridad y confidencialidad "
            "de la información del sistema.\n")

        doc.add_heading('2. Metodología', level=2)
        doc.add_paragraph(
            "La auditoría se realizó utilizando herramientas automatizadas y revisión manual para extraer y analizar "
            "logs de errores. Este proceso incluyó la correlación de eventos de error con intentos de acceso y "
            "anomalías de tráfico de red, proporcionando una visión integral de posibles fallos de seguridad.")

        doc.add_heading('3. Hallazgos Detallados', level=2)
        table = doc.add_table(rows=1, cols=5)
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'Fecha y Hora'
        hdr_cells[1].text = 'Usuario'
        hdr_cells[2].text = 'IP No Registrada'
        hdr_cells[3].text = 'Código de Error'
        hdr_cells[4].text = 'Detalle del Error'
        for _, row in errores_df.iterrows():
            row_cells = table.add_row().cells
            row_cells[0].text = str(row['Fecha y Hora'])
            row_cells[1].text = str(row['Usuario'])
            row_cells[2].text = str(row['IP NO REGISTRADO'])
            row_cells[3].text = str(row['DETALLE DE ERROR'])
            row_cells[4].text = str(row['Mensaje'])

        doc.add_heading('4. Recomendaciones', level=2)
        doc.add_paragraph(
            "Se recomienda fortalecer los mecanismos de autenticación, mejorar la supervisión "
            "de la actividad en la red y capacitar a los usuarios en prácticas de seguridad "
            "informática. Es crucial actualizar el software de seguridad a la última versión disponible.\n")

        nombre_informe = 'Informe_Auditoria_Logs_Error.docx'
        doc.save(nombre_informe)
        st.success(f"Informe generado exitosamente en {nombre_informe}.")
        st.download_button(label="Descargar Informe de Auditoría", data=open(nombre_informe, 'rb'), file_name=nombre_informe)

# Interfaz con Streamlit
st.title("Análisis de Logs de Error y Generación de Informe de Auditoría")

archivo_subido = st.file_uploader("Cargue su archivo de Logs", type=["xlsx"])

if archivo_subido is not None:
    df = pd.read_excel(archivo_subido)
    analizar_logs_error_y_generar_informe(df)
