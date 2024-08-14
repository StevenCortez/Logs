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

        # Introducción detallada
        doc.add_heading('1. Introducción', level=2)
        doc.add_paragraph(
            "El presente informe de auditoría se enfoca en el análisis exhaustivo de los registros de error (logs) "
            "generados por los sistemas de la empresa XYZ. La auditoría tiene como objetivo identificar fallas críticas "
            "en la infraestructura tecnológica y proponer medidas correctivas para mejorar la seguridad y continuidad operativa."
        )
        doc.add_paragraph(
            "La importancia de este análisis radica en la capacidad de los logs para proporcionar información clave sobre el "
            "rendimiento del sistema, incidentes de seguridad, y posibles vulnerabilidades que podrían ser explotadas. "
            "A través de este informe, se busca no solo detectar errores, sino también comprender sus causas raíz y su impacto "
            "potencial en la organización."
        )

        # Metodología detallada
        doc.add_heading('2. Metodología', level=2)
        doc.add_paragraph(
            "La metodología empleada en esta auditoría combina técnicas automatizadas y manuales para el análisis de los logs de error. "
            "Se utilizaron herramientas como Splunk y ELK Stack para la recolección y análisis preliminar de los datos. "
            "Posteriormente, se emplearon scripts en Python para filtrar y clasificar los logs según su severidad."
        )
        doc.add_paragraph(
            "Además del análisis técnico, se realizaron entrevistas con el personal de TI para entender el contexto en el que "
            "ocurrieron los errores y se revisaron las políticas de seguridad vigentes. Esto permitió no solo identificar errores, "
            "sino también evaluar la eficacia de las medidas de seguridad implementadas."
        )
        doc.add_paragraph(
            "El análisis se estructuró en varias fases: recolección de datos, filtrado de logs, análisis de patrones, "
            "identificación de vulnerabilidades, y generación de recomendaciones. Cada fase fue diseñada para maximizar la "
            "precisión y relevancia de los hallazgos, asegurando que las recomendaciones sean aplicables y efectivas."
        )

        # Hallazgos Detallados con análisis profundo
        doc.add_heading('3. Hallazgos Detallados', level=2)
        doc.add_paragraph(
            "A continuación, se presentan los hallazgos más significativos derivados del análisis de los logs de error. "
            "Estos hallazgos se agrupan en categorías según su impacto y la urgencia de su resolución."
        )

        # Tablas con detalles de los logs
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
            "Los errores identificados incluyen fallas en la autenticación de usuarios, intentos de acceso no autorizados, "
            "y problemas de integridad de datos. Cada uno de estos errores podría comprometer la seguridad del sistema si no se aborda adecuadamente."
        )

        # Análisis de Impacto
        doc.add_heading('3.1 Análisis de Impacto', level=3)
        doc.add_paragraph(
            "El impacto potencial de los errores identificados es considerable. Las fallas en la autenticación podrían permitir "
            "el acceso no autorizado a sistemas críticos, mientras que los problemas de integridad de datos podrían resultar en "
            "pérdida de información valiosa o en la corrupción de bases de datos. Es fundamental que estos errores se solucionen "
            "a la mayor brevedad para prevenir incidentes mayores."
        )
        doc.add_paragraph(
            "Además, se identificaron patrones repetitivos en los errores, lo que sugiere la existencia de vulnerabilidades subyacentes "
            "en la infraestructura de TI. La remediación de estas vulnerabilidades debe ser prioritaria."
        )

        # Recomendaciones detalladas
        doc.add_heading('4. Recomendaciones', level=2)
        doc.add_paragraph(
            "• Implementar autenticación multifactor (MFA) para fortalecer la seguridad de acceso a sistemas críticos.\n"
            "• Revisar y actualizar las políticas de seguridad para garantizar que reflejen las mejores prácticas actuales.\n"
            "• Implementar un sistema de monitoreo en tiempo real para detectar y responder a errores de manera proactiva.\n"
            "• Realizar auditorías periódicas para evaluar la eficacia de las medidas implementadas y ajustar las estrategias de seguridad según sea necesario."
        )

        # Plan de Acción detallado
        doc.add_heading('5. Plan de Acción', level=2)
        doc.add_paragraph(
            "• Proyecto 1: Implementación de MFA en todos los sistemas críticos. Responsable: Departamento de TI. Plazo: 30 días.\n"
            "• Proyecto 2: Actualización de las políticas de seguridad. Responsable: CISO. Plazo: 45 días.\n"
            "• Proyecto 3: Implementación de un sistema de monitoreo en tiempo real. Responsable: Equipo de Seguridad. Plazo: 60 días."
        )

        # Conclusiones mejoradas
        doc.add_heading('6. Conclusiones', level=2)
        doc.add_paragraph(
            "La auditoría ha revelado varios errores críticos en la infraestructura de TI de la empresa XYZ. Estos errores representan "
            "riesgos significativos para la seguridad y continuidad operativa de la organización. Se recomienda la implementación "
            "inmediata de las medidas correctivas descritas en el plan de acción para mitigar estos riesgos y fortalecer la seguridad del sistema."
        )
        doc.add_paragraph(
            "El seguimiento de las recomendaciones propuestas es crucial para asegurar que los problemas identificados no se repitan y que "
            "la organización esté mejor preparada para enfrentar futuros desafíos de seguridad."
        )

        # Anexos detallados
        doc.add_heading('7. Anexos', level=2)
        doc.add_paragraph(
            "• Anexo 1: Detalle de los Logs Analizados. Incluye una lista completa de los logs revisados, con información adicional sobre cada incidente.\n"
            "• Anexo 2: Gráficos y Tablas de Análisis. Visualización de datos que resalta los patrones de error identificados.\n"
            "• Anexo 3: Documentación de Normativas y Políticas. Citas y detalles de las normativas aplicadas en esta auditoría.\n"
            "• Anexo 4: Plan de Acción Detallado. Un cronograma detallado para la implementación de las mejoras recomendadas."
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

