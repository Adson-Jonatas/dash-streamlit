import streamlit as st


class ContainerModule:
    def __init__(self):
        self.title = "Containers e Imagens"

    @staticmethod
    def render_metricas():
        col1, col2, col3, col4 = st.columns(4)
        col1.metric(label="Total de Vulnerabilidades", value="14.562", delta="2", border=True)
        col2.metric(label="Total de Críticas", value="550", delta="-15", border=True)
        col3.metric(label="Total de Altas", value="2.548", delta="8", border=True)
        col4.metric(label="Total de Médias", value="12.023", delta="-2", border=True)

    @staticmethod
    def render_abas():
        aba1, aba2 = st.tabs(["Início", "Métricas"])

        with aba1:
            st.write("Início")
        with aba2:
            st.write("Métricas")

    @staticmethod
    def render_render():
        st.subheader("Imagem - Prisma")
        st.markdown("---")
        ContainerModule.render_metricas()
        ContainerModule.render_abas()

