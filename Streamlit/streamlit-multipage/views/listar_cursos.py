import pandas as pd
import streamlit as st


def view():
    st.title("Listagem de Cursos")

    try:
        st.dataframe(pd.read_csv("data/cursos.csv"))
    except:
        st.warning("Nenhum curso dísponível encontrado!")
