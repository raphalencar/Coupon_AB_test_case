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
- Databricks ([Serverless environment version 2](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/two))
- Python 3.9+
- Pandas, Matplotlib, Seaborn (para visualizações locais)
- Scipy/Statsmodels (para testes estatísticos)

---

## 📁 Estrutura do Projeto
```
.
├── notebooks/
│ ├── 01_data_acquisition.ipynb
│ ├── 02_data_cleasing.ipynb
│ ├── 03_campaign_impact_analysis.ipynb
│ ├── 04_customer_segmentation.ipynb
├── relatorios/
│ ├── relatorio_negocio.html
│ ├── relatorio_negocio.pdf
├── __init__.py
├── constants.py
├── schemas.py
├── utils.py
├── README.md
└── requirements.txt
```

---

## 🧪 Como Rodar

1. Clone o repositório:
```bash
https://github.com/raphalencar/Coupon_AB_test_case
```
2. Instale as dependências (ambiente local):

```bash
pip install -r requirements.txt
```

3. Abra no Databricks ou Jupyter para rodar os notebooks em sequência.

--- 

## 📈 Principais KPIs Calculados
`orders_per_user` → Pedidos por usuário

`total_spent_per_user` → Total gasto por usuário

`avg_ticket_per_user` → Ticket médio

`avg_items_per_order` → Itens por pedido

`is_retained` → Flag de retenção (usuário fez mais de 1 pedido)

---

## 🔬 Testes Estatísticos
* `T-Test` para métricas contínuas

* `Qui-Quadrado` para segmentações categóricas

* Verificação de normalidade (`Shapiro-Wilk`)

---

## 📌 Conclusões
* A campanha teve impacto significativo em gasto, pedidos e retenção.

* O efeito foi robusto em todos os segmentos de valor e perfil de consumo.

--- 

## 💡 Recomendações Estratégicas
* Escalar campanha para usuários com ticket baixo/médio

* Ofertas agressivas para reativar usuários inativos

* Personalização por tipo de restaurante

* Padronizar estrutura de testes A/B com automação

* Aplicar clusterização comportamental

## Relatório de negócio
O relatório para o time de negócio está disponível em dois formatos, html e pdf. A versão em html está com um design mais organizado e a versão em pdf foi gerada a partir dela. Recomendo availar pela versão html!

## 👤 Autor
Raphael Alencar – Data Analyst
