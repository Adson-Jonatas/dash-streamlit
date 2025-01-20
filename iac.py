import streamlit as st


class IACModule:
    def __init__(self):
        self.title = "Infraestrutura como Código"

    @staticmethod
    def render_metricas():
        col1, col2, col3, col4 = st.columns(4)
        col1.metric(label="Total de Vulnerabilidades", value="14.562", delta="2", border=True)
        col2.metric(label="Total de Críticas", value="550", delta="-15", border=True)
        col3.metric(label="Total de Altas", value="2.548", delta="8", border=True)
        col4.metric(label="Total de Médias", value="12.023", delta="-2", border=True)

    @staticmethod
    def render_abas():
        aba1, aba2, aba3, aba4 = st.tabs(["Início", "GCP", "AWS", "AZURE"])
        with aba1:
            st.write("Início")
        with aba2:
            st.write("GCP")
        with aba3:
            st.write("AWS")
        with aba4:
            st.write("AZURE")


    @staticmethod
    def render_render():
        st.subheader("IaC - Prisma")
        st.markdown("---")
        IACModule.render_metricas()
        IACModule.render_abas()


