# Ciência de Dados para RH (mas nao qualquer RH, minha ISA totosa :D)

Curso introdutório e extremamente didático para quem nunca trabalhou com ciência de dados. A trilha começa em planilhas e evolui para Python, análise exploratória, estatística, testes estatísticos, regressão linear e árvores de decisão.

As aulas em Markdown foram escritas em formato de capítulos: cada uma traz base teórica, exemplos de RH, perguntas e respostas, exercícios de fixação, exercícios de aplicação e um desafio final.

O tema central é People Analytics aplicado ao dia a dia de RH: recrutamento e seleção, treinamento, cargos e salários, departamento pessoal, terceiros, turnover, absenteísmo, diversidade e corte de gastos.

## Como usar este repositório

1. Comece pelo roteiro: `aulas/00_roteiro_do_curso.md`.
2. Leia cada aula como um capítulo de livro, sem pular a teoria.
3. Faça a seção de perguntas e respostas para checar entendimento.
4. Resolva os exercícios de fixação, aplicação e desafio.
5. Depois abra os notebooks em ordem, dentro da pasta `notebooks/`.
6. Use o projeto final para consolidar a aprendizagem.

## Instalação

Crie ou selecione um ambiente Python e instale as dependências:

```bash
pip install -r requirements.txt
```

## Estrutura

```text
aulas/       Guias didáticos em Markdown
dados/       CSVs sintéticos para exercícios em Excel e Python
notebooks/   Aulas práticas em Jupyter Notebook
scripts/     Utilitários, incluindo download opcional de datasets do Kaggle
```

## Trilha sugerida

| Ordem | Aula | Resultado esperado |
|---|---|---|
| 1 | `aulas/00_roteiro_do_curso.md` | Entender a trilha, o método de estudo e o ciclo de análise |
| 2 | `aulas/01_excel_e_tabelas.md` | Entender pensamento tabular, qualidade de dados e KPIs em Excel |
| 3 | `aulas/02_estatistica_para_rh.md` | Entender estatística descritiva, hipóteses, testes e ética |
| 4 | `aulas/03_python_para_iniciantes.md` | Traduzir o raciocínio de Excel para pandas |
| 5 | `notebooks/00_fundamentos_python.ipynb` | Aprender variáveis, tipos, listas, dicionários, condições, loops e funções |
| 6 | `notebooks/01_primeiros_passos_python.ipynb` | Abrir CSV, filtrar, agrupar e criar indicadores com pandas |
| 7 | `notebooks/02_analise_exploratoria_rh.ipynb` | Fazer uma análise exploratória de RH com gráficos |
| 8 | `notebooks/03_estatistica_e_testes.ipynb` | Aplicar testes estatísticos simples com interpretação |
| 9 | `aulas/04_modelagem_regressao_e_arvores.md` | Entender modelos preditivos, métricas, treino/teste e ética |
| 10 | `notebooks/04_regressao_linear_time_to_hire.ipynb` | Treinar uma regressão linear para prever time to hire |
| 11 | `notebooks/05_arvore_decisao_turnover.ipynb` | Treinar uma árvore de decisão para risco de desligamento |
| 12 | `aulas/05_kaggle_datasets_publicos.md` | Usar datasets públicos com critério e senso crítico |
| 13 | `aulas/06_projeto_final.md` | Apresentar um mini projeto de People Analytics |

## Formato das aulas

Cada aula principal segue esta estrutura:

- Objetivo da aula.
- Fundamentação teórica.
- Exemplos aplicados a RH.
- Perguntas e respostas.
- Exercícios de fixação.
- Exercícios de aplicação.
- Desafio.
- Fechamento conceitual.

Os notebooks seguem a mesma filosofia: células curtas, explicações antes do código, comentários linha a linha sempre que o comando pode não ser óbvio e exercícios ao final.

## Datasets do curso

Os datasets em `dados/` são sintéticos e seguros para estudo. Eles cobrem:

- Source of hire e time to hire.
- Horas de treinamento, conclusão, eficácia e custo de coffee.
- Headcount, representatividade, salário, absenteísmo, horas extras e turnover.
- Divergências de ponto e horas extras indevidas pelo Artigo 58.
- Ações de terceiros em refeitório, portaria, crachás e transporte.

Veja o dicionário em `aulas/dicionario_dados.md`.

## Kaggle

Para praticar com datasets públicos maiores, veja `aulas/05_kaggle_datasets_publicos.md` e execute:

```bash
python scripts/baixar_datasets_kaggle.py
```

Observação: o Kaggle pode exigir login e aceite dos termos do dataset.

## Princípios do curso

- Começar pela pergunta de negócio, não pelo modelo.
- Explicar indicadores em português claro.
- Usar estatística para apoiar decisões, não para decorar fórmulas.
- Tratar dados sensíveis com cuidado ético.
- Modelos preditivos são ferramentas de investigação, não verdades automáticas.