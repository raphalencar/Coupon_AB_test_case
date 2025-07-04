# 📊 Análise de Teste A/B - Campanha de Cupom iFood

Este projeto apresenta uma análise robusta de um teste A/B conduzido com dados reais de uma campanha promocional do iFood, utilizando PySpark e Databricks. O objetivo é avaliar o impacto do uso de cupons sobre métricas como gasto total, frequência de pedidos e retenção de usuários, incluindo análises segmentadas.

---

## 🔍 Objetivos

- Avaliar a efetividade da campanha de cupons.
- Medir impacto em KPIs como:
  - Gasto total por usuário
  - Número de pedidos
  - Ticket médio
  - Retenção
- Analisar os efeitos por segmento de usuário:
  - Frequência de pedidos
  - Ticket médio
  - Perfil de restaurante
- Estimar a viabilidade financeira da ação.
- Gerar recomendações de negócio com base nos dados.

---

## ⚙️ Tecnologias Utilizadas

- Apache Spark (PySpark)
- Databricks
- Python 3.9+
- Pandas, Matplotlib, Seaborn (para visualizações locais)
- Scipy/Statsmodels (para testes estatísticos)

---

## 📁 Estrutura do Projeto
.
├── notebooks/
│ ├── 01_data_acquisition.ipynb
│ ├── 02_data_cleasing.ipynb
│ ├── 03_campaign_impact_analysis.ipynb
│ ├── 04_customer_segmentation.ipynb
├── constants.py
├── schemas.py
├── utils.py
├── README.md
└── requirements.txt

