import streamlit as st


class SCAModule:
    def __init__(self):
        self.title = "SCA - Software Composition Analysis"

    @staticmethod
    def render_abas():
        aba1, aba2 = st.tabs(["Início", "Bloqueio das Altas"])
        with aba1:
            col1, col2, col3, col4 = st.columns(4)
            col1.metric(label="Total de Vulnerabilidades", value="14.562", delta="2", border=True)
            col2.metric(label="Total de Críticas", value="550", delta="-15", border=True)
            col3.metric(label="Total de Altas", value="2.548", delta="8", border=True)
            col4.metric(label="Total de Médias", value="12.023", delta="-2", border=True)
        with aba2:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("Primeiro Quadrimestre")
            with col2:
                st.write("Segundo Quadrimetre")
            with col3:
                st.write("Terceiro Quadrimestre")

    @staticmethod
    def render_render():
        st.subheader("SCA - Veracode")
        SCAModule.render_abas()

