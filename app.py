import streamlit as st
import pandas as pd

# Título de la página
st.title("Horario de Clases STEAM - Universidad Peruana Cayetano Heredia")

# Información introductoria
st.markdown("""
Esta página muestra el horario de las clases STEAM disponibles. Puedes filtrar la información
por semana, curso o sede para encontrar los detalles específicos de tus clases.
""")

# URL del archivo CSV en GitHub
csv_url = "https://raw.githubusercontent.com/inefable12/STEAM_UPCH/refs/heads/main/HorarioJesus.csv"

# Cargar datos
#@st.cache
def load_data():
    return pd.read_csv(csv_url)

data = load_data()

# Mostrar tabla completa
st.header("Horario Completo")
st.dataframe(data)

# Filtros
st.sidebar.header("Filtrar Horario")
semana = st.sidebar.selectbox("Seleccionar Semana", options=["Todas"] + sorted(data["Semana"].unique()))
curso = st.sidebar.selectbox("Seleccionar Curso", options=["Todos"] + sorted(data["Curso"].unique()))
sede = st.sidebar.selectbox("Seleccionar Sede", options=["Todas"] + sorted(data["Sede"].unique()))

# Aplicar filtros
filtered_data = data
if semana != "Todas":
    filtered_data = filtered_data[filtered_data["Semana"] == semana]
if curso != "Todos":
    filtered_data = filtered_data[filtered_data["Curso"] == curso]
if sede != "Todas":
    filtered_data = filtered_data[filtered_data["Sede"] == sede]

# Mostrar datos filtrados
st.header("Horario Filtrado")
st.dataframe(filtered_data)

# Mensaje de despedida
st.markdown("""
---
Gracias por visitar esta página. Si tienes alguna pregunta, comunícate con el coordinador de las clases STEAM.
""")
