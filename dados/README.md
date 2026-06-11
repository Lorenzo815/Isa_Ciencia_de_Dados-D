# Dados didáticos

Os arquivos desta pasta são pequenos datasets sintéticos de RH criados para fins de aprendizagem. Eles foram desenhados para parecerem planilhas reais, mas não representam pessoas, empresas ou processos reais.

## Arquivos

- `vagas_recrutamento.csv`: source of hire, time to hire, candidatos, entrevistas, ofertas e custo de divulgação.
- `treinamentos.csv`: horas de treinamento, conclusão, avaliação de eficácia e custo de coffee.
- `colaboradores.csv`: headcount analítico com área, cargo, salário, diversidade, absenteísmo, horas extras e desligamento nos últimos 12 meses.
- `ponto_horas.csv`: divergências no ponto, horas extras e horas extras indevidas pelo Artigo 58.
- `terceiros.csv`: ações de refeitório, portaria, crachás provisórios e transporte.
- `indicadores_mensais.csv`: turnover, absenteísmo, horas extras, headcount e corte de gastos.

## Como usar no Excel

1. Abra um arquivo CSV no Excel.
2. Transforme a tabela com `Ctrl + T`.
3. Crie filtros por área, mês e status.
4. Use tabela dinâmica para responder perguntas como: qual fonte de contratação tem menor time to hire? Qual área tem mais horas extras? Qual grupo tem maior taxa de retenção?

## Como usar no Python

```python
import pandas as pd

vagas = pd.read_csv("dados/vagas_recrutamento.csv")
vagas.head()
```
