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

        doc.add_heading('1. Datos Generales', level=2)
        doc.add_paragraph("• Fecha del Informe: 14 de agosto de 2024")
        doc.add_paragraph("• Nombre de la Entidad Auditada: Empresa XYZ")
        doc.add_paragraph("• Área de Efecto de la Auditoría: Análisis del LOGS y las severidades que presentan")
        doc.add_paragraph("• Objetivo:")
        doc.add_paragraph(
            "  - Evaluar la integridad, seguridad y eficacia de los procesos informáticos de la empresa XYZ mediante el análisis de logs categorizados en 'INFO', 'WARNING', y 'ERROR'.\n"
            "  - Identificar vulnerabilidades y fallos críticos reflejados en los LOGS de 'ERROR' y proponer soluciones para mitigarlos."
        )
        doc.add_paragraph("• Código de la Auditoría: AUD-XYZ-LOG-0814")
        doc.add_paragraph("• Lugar de Auditoría: Infraestructura de TI de la empresa XYZ, incluyendo servidores y bases de datos críticos.")
        doc.add_paragraph("• Normativa Aplicada y Excepciones:")
        doc.add_paragraph(
            "  - Normativas Aplicadas:\n"
            "    • ISO/IEC 27001: Sistema de Gestión de Seguridad de la Información.\n"
            "    • NIST SP 800-92: Guía para la gestión de logs."
        )
        doc.add_paragraph("  - Excepciones: No se incluyeron logs categorizados como 'INFO' o 'WARNING' en el análisis final.")

        doc.add_heading('2. Marco Teórico', level=2)
        doc.add_paragraph(
            "• Referencias Normativas:\n"
            "  - La auditoría se basa en la normativa ISO/IEC 27001 para asegurar que la gestión de la seguridad de la información en la empresa XYZ cumple con los estándares internacionales."
        )
        doc.add_paragraph("• Misión de la Auditoría: Auditoría integral del registro de LOGS, con un enfoque en la identificación y resolución de errores críticos que puedan afectar la operación segura y eficiente de los sistemas de información de la empresa XYZ.")
        doc.add_paragraph(
            "• Definiciones:\n"
            "  - Log: Registro de eventos generado por sistemas y aplicaciones, categorizado en este caso en 'INFO', 'WARNING', y 'ERROR'.\n"
            "  - Error: Eventos que indican fallos críticos en el sistema que requieren intervención inmediata."
        )

        doc.add_heading('3. Presentación de la Organización Auditada', level=2)
        doc.add_paragraph("• Descripción General: La empresa XYZ es una organización que depende fuertemente de su infraestructura de TI para realizar operaciones críticas. XYZ gestiona grandes volúmenes de datos y requiere un sistema robusto para garantizar la continuidad del negocio.")
        doc.add_paragraph("• Procesos Clave: Los procesos auditados incluyen la gestión de bases de datos, operaciones en servidores críticos, y el monitoreo de red.")

        doc.add_heading('4. Alcance de la Auditoría', level=2)
        doc.add_paragraph("• Perímetro Geográfico: La auditoría cubrió la infraestructura de TI de XYZ, incluyendo centros de datos y servidores ubicados en las oficinas principales de la empresa.")
        doc.add_paragraph("• Descripción de los Sistemas de Información: La auditoría abarcó los sistemas de gestión de bases de datos, servidores de aplicaciones, y sistemas de monitoreo de red, todos ellos críticos para la operación de XYZ.")

        doc.add_heading('5. Metodología de la Auditoría', level=2)
        doc.add_paragraph(
            "• Herramientas Utilizadas:\n"
            "  - Splunk: Utilizado para la recolección y análisis de logs.\n"
            "  - Python Scripts: Desarrollados para la separación y análisis específico de logs de 'Error'.\n"
            "  - ELK Stack: Para la indexación y búsqueda avanzada de logs.\n"
            "  - SIEM: Implementado para la correlación de eventos y generación de alertas."
        )
        doc.add_paragraph(
            "• Procedimientos:\n"
            "  - Recolección de logs desde servidores críticos y bases de datos.\n"
            "  - Filtrado y clasificación de logs utilizando scripts en Python para enfocarse en eventos categorizados como 'Error'.\n"
            "  - Análisis manual y automatizado de los logs de error para identificar patrones, vulnerabilidades y fallos críticos."
        )

        doc.add_heading('6. Resultados de la Auditoría', level=2)
        doc.add_heading('6.1 Integridad y Seguridad de los Logs', level=3)
        doc.add_paragraph("• Disponibilidad: Los logs de error se generan de manera consistente en los sistemas críticos, lo que permite una trazabilidad efectiva de los eventos de fallo.")
        doc.add_paragraph("• Seguridad: Se detectaron vulnerabilidades en la protección de logs, lo que podría permitir la manipulación de registros. Es necesario implementar cifrado y control de acceso más estrictos para asegurar la integridad de los logs.")
        doc.add_heading('6.2 Monitoreo y Respuesta', level=3)
        doc.add_paragraph("• Eficacia del Monitoreo: El sistema de monitoreo de XYZ no está configurado para detectar y alertar en tiempo real sobre ciertos errores críticos.")
        doc.add_paragraph("• Capacidad de Respuesta: La capacidad de respuesta a los errores críticos es limitada debido a la falta de un protocolo de actuación claramente definido y documentado.")
        doc.add_heading('6.3 Cumplimiento de Normativas', level=3)
        doc.add_paragraph("• ISO/IEC 27001: Se identificaron áreas de mejora en la gestión de logs, específicamente en la implementación de controles de acceso y cifrado para cumplir plenamente con la normativa.")
        doc.add_paragraph("• NIST SP 800-92: La organización cumple parcialmente con las recomendaciones, pero necesita fortalecer su monitoreo continuo y la retención segura de logs.")

        doc.add_heading('7. Análisis de Vulnerabilidades y Recomendaciones', level=2)
        doc.add_paragraph("• Vulnerabilidad 1: Acceso No Autorizado a Logs. Recomendación: Implementar controles de acceso basados en roles y cifrado de logs para proteger la información crítica.")
        doc.add_paragraph("• Vulnerabilidad 2: Inconsistencia en la Generación de Logs. Recomendación: Revisar y ajustar la configuración de logging en todos los sistemas críticos para asegurar la consistencia.")
        doc.add_paragraph("• Vulnerabilidad 3: Falta de Monitoreo en Tiempo Real. Recomendación: Implementar un sistema de monitoreo en tiempo real que genere alertas automáticas ante eventos críticos.")

        doc.add_heading('8. Evaluación del Riesgo', level=2)
        doc.add_paragraph("• Enfoque Adoptado: La evaluación de riesgos se centró en los procesos críticos para la operación de XYZ, considerando la probabilidad y el impacto de los errores detectados en los logs.")
        doc.add_paragraph("• Resultados: Escenario 1: Fallo en el acceso a la base de datos principal debido a errores no detectados en tiempo real. Recomendación: Implementar redundancias y fortalecer el monitoreo.")

        doc.add_heading('9. Plan de Acción', level=2)
        doc.add_paragraph("• Proyecto 1: Implementación de Controles de Acceso y Cifrado de Logs. Responsable: Departamento de TI de XYZ. Plazo: 30 días.")
        doc.add_paragraph("• Proyecto 2: Mejora en la Consistencia y Monitoreo de Logs. Responsable: Departamento de TI de XYZ. Plazo: 60 días.")

        doc.add_heading('10. Conclusiones', level=2)
        doc.add_paragraph("La auditoría ha identificado varios errores críticos en los sistemas de XYZ que requieren atención inmediata para asegurar la continuidad operativa y la seguridad de los datos. Se recomienda implementar las acciones propuestas en el plan de acción para mitigar los riesgos identificados y fortalecer la infraestructura de seguridad de la empresa.")

        doc.add_heading('11. Anexos', level=2)
        doc.add_paragraph("• Anexo 1: Detalle de Logs Analizados. Incluye una lista de todos los logs de error revisados, con detalles sobre la fecha, hora y sistema afectado.")
        doc.add_paragraph("• Anexo 2: Gráficos y Tablas de Análisis. Visualización de patrones de errores detectados y su impacto en los sistemas.")
        doc.add_paragraph("• Anexo 3: Referencias Normativas y Procedimientos. Citas y detalles de las normativas aplicadas en la auditoría.")
        doc.add_paragraph("• Anexo 4: Plan de Acción Detallado. Cronograma y asignación de responsabilidades para la implementación de mejoras.")

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
