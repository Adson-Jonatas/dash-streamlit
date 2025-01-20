import ast

import pandas as pd
import json
import csv
from datetime import datetime, timedelta

"""
# Ler o JSON diretamente do arquivo
with open("IaC-Data/cve_repositorio.json", "r") as file:
    json_data = json.load(file)  # Carregar o JSON como um objeto Python

# Converter o JSON para um DataFrame
df = pd.json_normalize(json_data)

# Salvar como CSV
df.to_csv("IaC-Data/cve_repositorio.csv", index=False)

print("JSON convertido e salvo como CSV!")
# json para csv
"""


# Teste de DataFrame com Prisma Imagem:
csv_prisma = pd.read_csv("prisma.csv")
df = pd.DataFrame(csv_prisma)

# Início Frame Básico
frame_basico = df.copy()
frame_basico["DashBasico"] = df["info.allCompliance.compliance"].apply(ast.literal_eval)
frame_basico = (frame_basico[["info.name", "info.namespace", "hostname", "DashBasico", "scanTime"]])
frame_basico["block"] = (frame_basico["DashBasico"].apply(lambda x: x[0]["block"] if isinstance(x, list) and len(x) > 0 else f"Jotta: Algo de errado não está certo!"))
frame_basico["cve"] = (frame_basico["DashBasico"].apply(lambda x: x[0]["cve"] if isinstance(x, list) and len(x) > 0 else f"Jotta: Algo de errado não está certo!"))
frame_basico["cvss"] = (frame_basico["DashBasico"].apply(lambda x: x[0]["cvss"] if isinstance(x, list) and len(x) > 0 else f"Jotta: Algo de errado não está certo!"))
frame_basico["description"] = (frame_basico["DashBasico"].apply(lambda x: x[0]["description"] if isinstance(x, list) and len(x) > 0 else f"Jotta: Algo de errado não está certo!"))
frame_basico["discovered"] = (frame_basico["DashBasico"].apply(lambda x: x[0]["discovered"] if isinstance(x, list) and len(x) > 0 else f"Jotta: Algo de errado não está certo!"))
frame_basico["severity"] = (frame_basico["DashBasico"].apply(lambda x: x[0]["severity"] if isinstance(x, list) and len(x) > 0 else f"Jotta: Algo de errado não está certo!"))
# Fim Frame Básico

# Início Frame Repositórios
frame_rep = pd.read_csv("IaC-Data/repositorio.csv")
# From Frame Repositórios

# Início Frame CVE por Repositórios
df_cve_rep = pd.read_csv("IaC-Data/cve_repositorio.csv")
frame_cve_rep = df_cve_rep.copy()
frame_cve_rep["utils"] = frame_cve_rep["data"].apply(ast.literal_eval)
frame_cve_rep["causePackageId"] = (frame_cve_rep["utils"].apply(lambda x: x[0]["causePackageId"] if isinstance(x, list) and len(x) > 0 else "errado"))
frame_cve_rep["cveId"] = (frame_cve_rep["utils"].apply(lambda x: x[0]["cveId"] if isinstance(x, list) and len(x) > 0 else "errado"))
frame_cve_rep["cvss"] = (frame_cve_rep["utils"].apply(lambda x: x[0]["cvss"] if isinstance(x, list) and len(x) > 0 else "errado"))
frame_cve_rep["description"] = (frame_cve_rep["utils"].apply(lambda x: x[0]["description"] if isinstance(x, list) and len(x) > 0 else "errado"))
frame_cve_rep["packageName"] = (frame_cve_rep["utils"].apply(lambda x: x[0]["packageName"] if isinstance(x, list) and len(x) > 0 else "errado"))
frame_cve_rep["packageVersion"] = (frame_cve_rep["utils"].apply(lambda x: x[0]["packageVersion"] if isinstance(x, list) and len(x) > 0 else "errado"))
frame_cve_rep["severity"] = (frame_cve_rep["utils"].apply(lambda x: x[0]["severity"] if isinstance(x, list) and len(x) > 0 else "errado"))
frame_cve_rep["uuid"] = (frame_cve_rep["utils"].apply(lambda x: x[0]["uuid"] if isinstance(x, list) and len(x) > 0 else "errado"))
frame_cve_repositorio = frame_cve_rep.drop(["data"], axis=1).drop(["utils"], axis=1)
# Fim Frame CVE por Repositórios





















