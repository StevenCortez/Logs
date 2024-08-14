import pandas as pd
from docx import Document
from docx.shared import Pt
import streamlit as st

def analizar_logs_error_y_generar_informe(df):
    if 'Severidad' not in df.columns:
        st.error("La columna 'Severidad' no se encuentra en el archivo.")
        return

    errores_df = df[df['Severidad'] == 'ERROR']

    if errores_df.empty:
        st.warning("No se encontraron registros con severidad 'ERROR'.")
    else:
        # Generar el archivo Excel con los errores detectados
        nombre_archivo_errores = 'Errores_Detectados.xlsx'
        errores_df.to_excel(nombre_archivo_errores, index=False)
        st.success(f"Archivo Excel con registros de ERROR generado exitosamente en {nombre_archivo_errores}.")
        st.download_button(label="Descargar Excel de Errores", data=open(nombre_archivo_errores, 'rb'), file_name=nombre_archivo_errores)

        # Crear el documento de Word para el informe
        doc = Document()
        doc.add_heading('INFORME DE AUDITORÍA BASADA EN LOGS DE ERROR', level=1)

        # Introducción mejorada
        doc.add_heading('1. Introducción', level=2)
        doc.add_paragraph(
            "La presente auditoría se realizó con el objetivo de identificar y analizar los errores críticos "
            "en los sistemas informáticos de la empresa XYZ, con un enfoque en asegurar la continuidad operativa "
            "y la protección de la información sensible. La importancia de esta auditoría radica en la capacidad de "
            "identificar fallas que podrían comprometer la seguridad y la eficiencia de los sistemas de información."
        )

        # Metodología mejorada
        doc.add_heading('2. Metodología', level=2)
        doc.add_paragraph(
            "La metodología aplicada en esta auditoría incluyó el uso de herramientas avanzadas de análisis de logs, "
            "como Splunk y ELK Stack, junto con scripts personalizados en Python. Estas herramientas permitieron "
            "la recolección, filtrado y análisis de logs categorizados como 'ERROR', lo que facilitó la identificación "
            "de fallos críticos. Se llevaron a cabo entrevistas con el personal de TI para entender el contexto de los errores detectados."
        )

        # Hallazgos Detallados mejorados
        doc.add_heading('3. Hallazgos Detallados', level=2)
        table = doc.add_table(rows=1, cols=5)
        hdr_cells = table.rows[0].cells
        hdr_cells[0].text = 'Fecha y Hora'
        hdr_cells[1].text = 'Usuario'
        hdr_cells[2].text = 'IP No Registrada'
        hdr_cells[3].text = 'Código de Error'
        hdr_cells[4].text = 'Detalle del Error'
        for _, row in errores_df.iterrows():
            cells = table.add_row().cells
            cells[0].text = str(row['Fecha y Hora'])
            cells[1].text = str(row['Usuario'])
            cells[2].text = str(row['IP NO REGISTRADO'])
            cells[3].text = str(row['DETALLE DE ERROR'])
            cells[4].text = str(row['Mensaje'])

        doc.add_paragraph(
            "Los logs de error encontrados indican posibles brechas en la seguridad y fallos en la configuración de los sistemas. "
            "A continuación, se detalla cómo estos errores pueden afectar la operación diaria y qué medidas pueden tomarse para mitigarlos."
        )

        # Recomendaciones mejoradas
        doc.add_heading('4. Recomendaciones', level=2)
        doc.add_paragraph(
            "• Implementar un sistema de monitoreo en tiempo real para detectar errores críticos de manera proactiva.\n"
            "• Fortalecer los mecanismos de autenticación y control de acceso para proteger la integridad de los logs.\n"
            "• Capacitar al personal en prácticas de seguridad informática, con un enfoque en la detección y respuesta ante incidentes.\n"
            "• Actualizar periódicamente el software de seguridad y asegurar que todos los sistemas cumplen con las normativas vigentes."
        )

        # Conclusiones mejoradas
        doc.add_heading('5. Conclusiones', level=2)
        doc.add_paragraph(
            "La auditoría ha revelado varios puntos críticos en los sistemas de la empresa XYZ que requieren atención inmediata. "
            "Si no se abordan estos problemas, existe un riesgo significativo de interrupciones operativas y compromisos de seguridad. "
            "Se recomienda implementar las medidas propuestas a la mayor brevedad para garantizar la continuidad y seguridad de las operaciones."
        )

        # Anexos mejorados
        doc.add_heading('6. Anexos', level=2)
        doc.add_paragraph(
            "• Anexo 1: Detalle de Logs Analizados. Incluye una lista de todos los logs de error revisados, con detalles sobre la fecha, hora y sistema afectado.\n"
            "• Anexo 2: Gráficos y Tablas de Análisis. Visualización de patrones de errores detectados y su impacto en los sistemas.\n"
            "• Anexo 3: Referencias Normativas y Procedimientos. Citas y detalles de las normativas aplicadas en la auditoría.\n"
            "• Anexo 4: Plan de Acción Detallado. Cronograma y asignación de responsabilidades para la implementación de mejoras."
        )

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

