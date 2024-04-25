import pandas as pd
import streamlit as st
from views import listar_cursos


def view():
    st.header("Criação de Cursos")

    with st.form("form_curso"):
        nome_curso = st.text_input("Nome do Curso")
        descricao_curso = st.text_area("Descricão do Curso", max_chars=400)
        valor_curso = st.number_input("Valor do Curso")
        duracao_curso = st.number_input("Duração do Curso(Horas)", step=1)
        professor_curso = st.text_input("Nome do Professor")
        submit = st.form_submit_button("Criação de Cursos")
        if submit:
            novo_curso = {
                "Nome do Curso": nome_curso,
                "Descricão do Curso": descricao_curso,
                "Valor do Curso": valor_curso,
                "Duração do Curso(Horas)": duracao_curso,
                "Nome do Professor": professor_curso,
            }

            try:
                df = pd.read_csv("data/cursos.csv")
            except FileNotFoundError:
                df = pd.DataFrame(
                    columns=[
                        "Nome do Curso",
                        "Descricão do Curso",
                        "Valor do Curso",
                        "Duração do Curso(Horas)",
                        "Nome do Professor",
                    ]
                )

            df = pd.concat([df, pd.DataFrame([novo_curso])], ignore_index=True)

            df.to_csv("data/cursos.csv", index=False)
            st.success("Curso criado com sucesso!")
            listar_cursos()