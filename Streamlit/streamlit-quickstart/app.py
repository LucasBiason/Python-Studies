import streamlit as st 
import pandas as pd


st.set_page_config(page_title="Site Streamlit")

with st.container():
    st.subheader("Testando a criação de sites com Streamlit")
    st.title("Dashboard de Contratos")
    st.write("Informações osbre os contratos fechados pela Empresa ao longo de Maio")


@st.cache_data
def carregar_dados():
    tabela = pd.read_csv("resultados.csv")
    return tabela


with st.container():
    st.write("---")
    qtde_dias = st.selectbox("Selecione o período", ["7 dias", "15 dias", "20 dias", "30 dias"])
    qtde_dias = int(qtde_dias.replace(" dias", ""))
    
    dados = carregar_dados()
    dados = dados[-qtde_dias:]
    
    st.area_chart(
        data=dados,
        x="Data",
        y="Contratos"
    )
