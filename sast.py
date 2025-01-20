import streamlit as st


class SASTModule:
    def __init__(self):
        self.title = "SAST - Static Application Security Testing"

    @staticmethod
    def render_abas():
        aba1, aba2 = st.tabs(["Início", "Métricas"])
        with aba1:

            col1, col2, col3, col4 = st.columns(4)
            col1.metric(label="Total de Vulnerabilidades", value="14.562", delta="2", border=True)
            col2.metric(label="Total de Críticas", value="550", delta="-15", border=True)
            col3.metric(label="Total de Altas", value="2.548", delta="8", border=True)
            col4.metric(label="Total de Médias", value="12.023", delta="-2", border=True)

            st.sidebar.subheader("Filtros - SAST")
            severities = st.sidebar.multiselect(
                "Severidades", ["Crítico", "Alto", "Médio", "Baixo"], default=["Crítico", "Alto"]
            )
            st.write(f"Exibindo vulnerabilidades com severidades: {', '.join(severities)}")
        with aba2:
            st.write("Métricas")

    @staticmethod
    def render_render():
        st.subheader("SAST - Veracode")
        SASTModule.render_abas()
