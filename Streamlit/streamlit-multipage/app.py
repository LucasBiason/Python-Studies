import streamlit as st
from streamlit_option_menu import option_menu
from views import home, listar_cursos, criar_cursos, login


st.set_page_config(page_title="Teste de Multipage", layout="wide")

if st.session_state.get("logged_in", False):
    col1, col2 = st.columns(2)
    with col1:
        selected=option_menu(
            menu_title= "Páginas",
            options = ["Home", "Lista de Cursos", "Criar de Cursos"],
            #icons = ["house-heart-fill", ...],
            menu_icon = "house-heart-fill",
            default_index=0
        )

    with col2:
        if selected == "Home":
            home.view()
        if selected == "Lista de Cursos":
            listar_cursos.view()
        if selected == "Criar de Cursos":
            criar_cursos.view()
else:
    login.view()
