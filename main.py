from base_layout import BaseLayout
from principal import PrincipalModule
from sast import SASTModule
from sca import SCAModule
from imagem import ContainerModule
from iac import IACModule
import streamlit as st


def main():
    layout = BaseLayout(title="DevSecOps", sidebar_title="Security by Design")
    layout.render_layout()
    modules = {
        "Infraestrutura como Código": IACModule(),
        "Visão Geral": PrincipalModule(),
        "SAST": SASTModule(),
        "SCA": SCAModule(),
        "Containers e Imagens": ContainerModule(),
    }
    st.sidebar.header("Painel DevSecOps")
    selected_module = st.sidebar.selectbox(
        "", list(modules.keys())
    )

    def render_content():
        module = modules[selected_module]
        module.render_render()

    layout.render_render(render_content)


if __name__ == "__main__":
    main()
