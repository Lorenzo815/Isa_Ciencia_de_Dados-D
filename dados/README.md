# Dados didáticos

Os arquivos desta pasta são pequenos datasets sintéticos de RH criados para fins de aprendizagem. Eles foram desenhados para parecerem planilhas reais, mas **não representam pessoas, empresas ou processos reais**. Use para treinar técnica, não para tirar conclusões sobre o mundo.

Todas as bases usam codificação UTF-8 e separador `,` (vírgula).

## Arquivos

- `vagas_recrutamento.csv`: uma linha por vaga. Inclui source of hire, time to hire, candidatos, entrevistas, ofertas, contratados e custo de divulgação. Use para indicadores de recrutamento.
- `treinamentos.csv`: uma linha por participação de uma pessoa em um treinamento. Inclui horas, conclusão, nota de eficácia, modalidade e custo de coffee.
- `colaboradores.csv`: uma linha por colaborador. Headcount analítico com área, cargo, salário, dados de diversidade, absenteísmo, horas extras, performance e flag de desligamento nos últimos 12 meses (`desligou_12m`).
- `ponto_horas.csv`: uma linha por registro de ponto. Divergências, horas extras e horas extras indevidas pelo Artigo 58.
- `terceiros.csv`: ações ligadas a serviços terceirizados (refeitório, portaria, crachás provisórios, transporte).
- `indicadores_mensais.csv`: uma linha por mês. Turnover, absenteísmo, horas extras, headcount e corte de gastos consolidados.
- `distribuicoes_exercicio.xlsx` / `distribuicoes_resolvido.xlsx`: planilhas multi-abas geradas pelo script `scripts/gerar_planilhas_distribuicoes.py`, usadas na Aula 2 para praticar distribuições e escolha de testes estatísticos.

A unidade de análise ("o que cada linha representa") é o primeiro filtro mental antes de calcular qualquer indicador.

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
