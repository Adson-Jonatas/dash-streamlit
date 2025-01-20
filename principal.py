import streamlit as st
import plotly.express as px
from dataset import df
import pandas as pd


class PrincipalModule:

    def __init__(self):
        self.title = "Principal"

    @staticmethod
    def render_abas():
        aba1, aba2 = st.tabs(["Início", "Métricas"])
        with aba1:

            col1, col2, col3, col4 = st.columns(4)
            col1.metric(label="Total de Vulnerabilidades", value="14.562", delta="2", border=True)
            col2.metric(label="Total de Críticas", value="550", delta="-15", border=True)
            col3.metric(label="Total de Altas", value="2.548", delta="8", border=True)
            col4.metric(label="Total de Médias", value="12.023", delta="-2", border=True)
            # Texto centralizado usando HTML
            st.markdown(
                """
                <div style="border-top: 1px solid rgb(60, 60, 60); margin: 5px 0;"></div>
                """,
                unsafe_allow_html=True,
            )
            st.markdown(
                """
                <div style="text-align: center;">
                    <h5>Vulnerabilidades por Sigla</h1>
                </div>
                """,
                unsafe_allow_html=True,
            )

            col1, col2 = st.columns(2)

            with col1:
                frame_col4 = df[
                    (df["vuln_critica"] > 0) |
                    (df["vuln_alta"] > 0) |
                    (df["vuln_media"] > 0) |
                    (df["vuln_baixa"] > 0)
                    ]
                frame_col4["vuln_alta"] = df["vuln_alta"].replace(0, 1)  # Substituir zeros por 1

                fig_treemap = px.treemap(
                    frame_col4,
                    path=["aplicacao", "sigla", "componente"],
                    values="vuln_alta",  # Usando as vulnerabilidades altas como peso
                    color="vuln_critica",  # Colorindo com base nas vulnerabilidades críticas
                    color_continuous_scale=px.colors.sequential.Reds,
                    title="Distribuição de Vulnerabilidades Altas e Críticas"
                )
                st.plotly_chart(fig_treemap)

            with col2:
                df['total_vuln'] = df[['vuln_critica', 'vuln_alta', 'vuln_media', 'vuln_baixa']].sum(axis=1)

                # Calculando a soma das vulnerabilidades por sigla
                sigla_vuln = df.groupby('sigla')['total_vuln'].sum().reset_index()

                # Calculando o total geral de vulnerabilidades
                total_vuln_geral = sigla_vuln['total_vuln'].sum()

                # Calculando as porcentagens de vulnerabilidade por sigla
                sigla_vuln['porcentagem'] = (sigla_vuln['total_vuln'] / total_vuln_geral) * 100

                # Gráfico de Pizza
                fig = px.pie(
                    sigla_vuln,
                    values='porcentagem',
                    names='sigla',
                    # title='Distribuição das Vulnerabilidades por Sigla',
                    labels={'porcentagem': 'Porcentagem de Vulnerabilidades', 'sigla': 'Sigla'},
                    color='sigla'
                )

                # Renderizando o gráfico no Streamlit
                st.plotly_chart(fig, use_container_width=True)

            st.markdown(
                """
                <div style="border-top: 1px solid rgb(60, 60, 60); margin: 5px 0;"></div>
                """,
                unsafe_allow_html=True,
            )
            st.markdown(
                """
                <div style="text-align: center;">
                    <h5>Vulnerabilidades por Componentes</h1>
                </div>
                """,
                unsafe_allow_html=True,
            )

            col3, col4 = st.columns(2)
            with col3:
                df_grouped = df.groupby("aplicacao")[
                    ["vuln_critica", "vuln_alta", "vuln_media", "vuln_baixa"]].sum().reset_index()
                fig_barras1 = px.bar(
                    df_grouped,
                    x="aplicacao",
                    y=["vuln_critica", "vuln_alta", "vuln_media", "vuln_baixa"],
                    title="Comparação de Vulnerabilidades por Aplicação",
                    labels={"value": "Quantidade de Vulnerabilidades", "aplicacao": "Aplicação"},
                    barmode="group",
                    color_discrete_sequence=px.colors.qualitative.Set2,
                )
                st.plotly_chart(fig_barras1, use_container_width=True)
            with col4:
                df_long = df.melt(
                    id_vars=["sigla"],
                    value_vars=["vuln_critica", "vuln_alta", "vuln_media", "vuln_baixa"],
                    var_name="Categoria",
                    value_name="Quantidade"
                )

                # Criar gráfico de linha
                fig_line = px.line(
                    df_long,
                    x="sigla",
                    y="Quantidade",
                    color="Categoria",
                    title="Vulnerabilidades por Sigla e Categoria",
                    labels={"sigla": "Sigla", "Quantidade": "Número de Vulnerabilidades"},
                    markers=True
                )
                fig_line.update_layout(xaxis=dict(tickangle=45))
                st.plotly_chart(fig_line, use_container_width=True)
        with aba2:
            st.write("Sem implementação")

    @staticmethod
    def render_render():
        st.subheader("DevSecOps - Visão Geral")
        PrincipalModule.render_abas()



