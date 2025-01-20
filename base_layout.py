import streamlit as st


class BaseLayout:
    def __init__(self, title="Título Defaul", sidebar_title="Título Default"):
        self.title = title
        self.sidebar_title = sidebar_title

    @staticmethod
    def render_layout():
        st.set_page_config(
            page_title="Meu Dashboard",
            page_icon="📊",
            layout="wide"  # Opções: "centered" ou "wide"
        )

    def render_header(self):
        st.title(self.title)

    @staticmethod
    def render_footer():
        st.markdown(
            """
            <div style="border-top: 1px solid rgb(60, 60, 60); margin: 5px 0;"></div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div style="text-align: center;">
                <p>🛠️ Sustentação: DevSecOps - Última atualização: **18 de Janeiro de 2025**</h1>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div style="border-top: 1px solid rgb(60, 60, 60); margin: 5px 0;"></div>
            """,
            unsafe_allow_html=True,
        )

    def render_render(self, content_callback):
        # self.render_header()
        if callable(content_callback):
            content_callback()
        self.render_footer()
