import streamlit as st
import pandas as pd

# Título principal de la página
st.set_page_config(page_title="STEAM - UPCH", layout="wide")

st.info("STEAM EN UPCH 2025")
st.write("Por Jesus Alvarado H, MSc. Dr.")

# Crear pestañas
tabs = st.tabs(["Horarios", "Encendiendo focos con Arduino", "Uso de servomotor con Arduino"])

# Pestaña "Horarios"
with tabs[0]:
    st.title("Horarios")

    st.markdown("""
    Esta apartado muestra mis horarios en el ciclo verano 2025.
    """)

    # URL del archivo CSV en GitHub
    csv_url = "https://raw.githubusercontent.com/inefable12/STEAM_UPCH/refs/heads/main/HorarioJesus.csv"

    # Cargar datos
    def load_data():
        return pd.read_csv(csv_url)

    data = load_data()

    # Mostrar tabla completa
    #st.header("H")
    st.dataframe(data)

    # Mensaje de despedida
    st.markdown("""
    ---
    Gracias por visitar esta página. Si tienes alguna pregunta, comunícate con el coordinador de las clases STEAM.
    """)

# Pestaña "Encendiendo focos con Arduino"
with tabs[1]:
    st.title("Encendiendo focos con Arduino")
    url = "https://www.tiktok.com/@inefable12x/video/7463614157187861765?is_from_webapp=1&sender_device=pc&web_id=7464532847794472453"
    st.markdown("Revisa algunas imágenes de la sesión anterior [link](%s)" % url)

    st.markdown("""
    En esta sección aprenderás cómo encender y apagar focos utilizando una placa Arduino. Este proyecto incluye:

    - Conexión de un circuito básico con un LED o foco.
    - Configuración de un código sencillo en el entorno Arduino IDE.
    - Ejecución del programa para controlar el foco.

    Sigue las instrucciones proporcionadas en la clase para completar este experimento práctico.
    """)

# Pestaña "Uso de servomotor con Arduino"
with tabs[2]:
    st.title("Uso de servomotor con Arduino")
    st.markdown("""
    En esta sección aprenderás cómo controlar un servomotor usando una placa Arduino. El objetivo del proyecto es:

    - Configurar el servomotor para que gire a ángulos específicos.
    - Utilizar el código de ejemplo en Arduino IDE para controlar el movimiento del servomotor.
    - Aplicar este conocimiento en proyectos robóticos o de automatización.

    Recuerda seguir los pasos indicados en la documentación y traer los materiales necesarios para la clase.
    """)
