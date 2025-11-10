# Projeto PROUNI: Análise Comparativa (Power BI vs. AWS)

**Descrição:** Projeto de Extensão (UNIP) que realiza uma análise de dados do PROUNI e demonstra duas arquiteturas de BI: Desktop (Power BI) e Cloud (AWS).

## 🎯 Objetivo

O objetivo deste projeto é duplo:
1.  **Democratizar os Dados:** Transformar dados públicos brutos do PROUNI em um dashboard interativo, facilitando a análise pela comunidade.
2.  **Educar (Tutorial):** Apresentar um tutorial comparativo de duas arquiteturas de análise de dados, demonstrando as vantagens e complexidades de cada uma.

---

## 🚀 Arquitetura 1: Análise Desktop (Power BI)

Esta abordagem foca na velocidade de prototipação e na análise local.

* **Ferramentas:** Python (Pandas) para unificação dos dados e Microsoft Power BI para modelagem e visualização.
* **ETL:** Os 3 arquivos CSV anuais (2017-2019) foram unificados com um script Python.
* **Modelagem:** Colunas calculadas (ex: `Idade Na Concessão`) foram criadas com DAX.
* **Resultado:**

![Dashboard Power BI](power_bi_local/Dashboard_ProUni.jpg)
*(Substituir pelo seu print de tela. O arquivo .pbix está na pasta /power-bi-local)*

---

## ☁️ Arquitetura 2: Pipeline de Nuvem (AWS) - EM CONSTRUÇÃO

Esta abordagem foca em uma solução escalável, automatizável e padrão de mercado, capaz de lidar com volumes de dados massivos.

* **Ferramentas:** AWS S3, AWS Glue, AWS Athena e AWS QuickSight.
* **ETL:**
    1.  Os dados unificados são armazenados no **S3**.
    2.  O **AWS Glue** (Crawler) cataloga os dados, tornando-os disponíveis para consulta.
    3.  *(Em breve: Script de ETL com Glue para tratar os dados)*
* **Análise:** O **AWS Athena** permite consultas SQL diretamente nos arquivos do S3.
* **Resultado:**
    *(Em breve: O dashboard do QuickSight será incorporado aqui)*
