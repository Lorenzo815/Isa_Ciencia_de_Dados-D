# Roteiro do curso: Ciencia de Dados para RH

Este curso foi desenhado para uma pessoa que nunca trabalhou com ciencia de dados, mas conhece problemas reais de RH. A proposta e construir o raciocinio aos poucos: primeiro com tabelas e Excel, depois com Python, estatistica, testes estatisticos e modelos preditivos simples.

A ideia central e simples: ciencia de dados e uma forma disciplinada de transformar perguntas em evidencias. O computador ajuda, mas a qualidade da pergunta, do dado e da interpretacao continua sendo humana.

## Como este curso esta organizado

O curso tem tres movimentos.

Primeiro, aprendemos a olhar planilhas como bases de dados. Isso inclui linhas, colunas, filtros, chaves, indicadores e problemas comuns de qualidade. Essa etapa e essencial porque a maioria dos erros de ciencia de dados nasce antes do modelo, em tabelas mal definidas ou indicadores mal calculados.

Depois, entramos em estatistica e Python. Python aparece como uma ferramenta para repetir analises, criar graficos, cruzar tabelas e reduzir trabalho manual. Estatistica aparece como uma linguagem para falar de variacao, incerteza e diferenca entre grupos.

Por fim, chegamos aos modelos. Regressao linear e arvore de decisao entram como instrumentos para previsao e classificacao, sempre com cuidado: um modelo nao substitui contexto de RH, governanca, privacidade ou julgamento profissional.

## Competencias desenvolvidas

Ao final da trilha, a pessoa deve conseguir:

- Organizar uma planilha de RH em formato analitico.
- Formular perguntas de negocio antes de escolher ferramentas.
- Calcular KPIs como time to hire, turnover, absenteismo, taxa de conclusao e retencao.
- Diferenciar media, mediana, dispersao, proporcao, correlacao e causalidade.
- Aplicar testes estatisticos simples com interpretacao responsavel.
- Usar pandas para ler, filtrar, agrupar e resumir dados.
- Criar graficos simples e adequados para comunicar resultados.
- Treinar uma regressao linear para prever um numero.
- Treinar uma arvore de decisao para prever uma classe.
- Apresentar achados com recomendacoes, limitacoes e proximos passos.

## Trilha sugerida

| Etapa | Material | Foco |
|---|---|---|
| 1 | `aulas/01_excel_e_tabelas.md` | Pensamento tabular, qualidade de dados e primeiros KPIs |
| 2 | `aulas/02_estatistica_para_rh.md` | Estatistica descritiva, inferencia, testes e cuidado etico |
| 3 | `aulas/03_python_para_iniciantes.md` | Ponte entre Excel e pandas |
| 4 | `notebooks/00_fundamentos_python.ipynb` | Fundamentos de Python para quem nunca programou |
| 5 | `notebooks/01_primeiros_passos_python.ipynb` | Primeiros passos com pandas e CSV |
| 6 | `notebooks/02_analise_exploratoria_rh.ipynb` | Analise exploratoria com graficos |
| 7 | `notebooks/03_estatistica_e_testes.ipynb` | Teste t, qui-quadrado e interpretacao |
| 8 | `aulas/04_modelagem_regressao_e_arvores.md` | Fundamentos de modelos preditivos |
| 9 | `notebooks/04_regressao_linear_time_to_hire.ipynb` | Regressao linear aplicada a recrutamento |
| 10 | `notebooks/05_arvore_decisao_turnover.ipynb` | Arvore de decisao aplicada a turnover |
| 11 | `aulas/05_kaggle_datasets_publicos.md` | Pratica com datasets publicos |
| 12 | `aulas/06_projeto_final.md` | Projeto final de People Analytics |

## Metodo de estudo

Cada aula deve ser estudada em quatro passagens.

Na primeira passagem, leia a teoria sem tentar memorizar tudo. O objetivo e construir vocabulario: tabela, indicador, variavel, hipotese, amostra, modelo, erro.

Na segunda passagem, abra os dados e reproduza os exemplos. Nao avance se uma coluna, formula ou grafico nao fizer sentido. Ciencia de dados se aprende muito pelo atrito com os detalhes.

Na terceira passagem, responda as perguntas e respostas da aula. Elas foram escritas para corrigir confusoes comuns de iniciantes.

Na quarta passagem, faca os exercicios. Os exercicios estao divididos em fixacao, aplicacao e desafio. A fixacao treina conceito; a aplicacao liga o conceito ao RH; o desafio pede interpretacao.

## O ciclo de uma boa analise

Use este ciclo em todas as aulas:

1. Pergunta de negocio: o que queremos decidir ou entender?
2. Unidade de analise: cada linha representa o que?
3. Dados necessarios: quais colunas precisamos?
4. Qualidade: ha valores ausentes, duplicados ou categorias inconsistentes?
5. Indicador: qual formula traduz a pergunta?
6. Comparacao: por area, mes, grupo, fonte, modalidade ou nivel.
7. Interpretacao: o que os dados sugerem?
8. Limitacao: o que os dados nao provam?
9. Acao: qual proximo passo seria razoavel?

## Perguntas e respostas

**Preciso saber matematica avancada para comecar?**

Nao. O mais importante no inicio e entender proporcoes, medias, diferencas e graficos. A matematica fica mais formal conforme a necessidade aparece.

**Por que comecar no Excel se o curso tem Python?**

Porque Excel ensina o pensamento tabular de forma visual. Quem entende uma boa tabela dinamica entende metade do caminho para usar pandas bem.

**Ciencia de dados e a mesma coisa que inteligencia artificial?**

Nao. Ciencia de dados e um campo amplo que inclui coleta, organizacao, analise, estatistica, visualizacao, comunicacao e modelos. Inteligencia artificial e uma parte possivel desse universo.

**Modelos preditivos podem decidir quem deve ser contratado ou desligado?**

Nao neste curso, e em contextos reais isso exigiria governanca rigorosa. Modelos em RH devem apoiar investigacao e melhoria de processos, nao automatizar decisoes sensiveis sem controle.

**Por que falar de etica logo no comeco?**

Porque RH trabalha com pessoas. Dados de genero, raca, idade, salario, saude, ponto e desempenho podem gerar dano se forem usados sem cuidado.

## Exercicios

### Fixacao

1. Explique com suas palavras a diferenca entre dado, informacao, indicador e decisao.
2. Escreva tres perguntas de RH que poderiam ser respondidas com uma tabela.
3. Escolha um indicador do curso e identifique numerador, denominador e periodo.

### Aplicacao

1. Abra `dados/README.md` e liste quais arquivos se conectam a recrutamento, treinamento, cargos e salarios, ponto, terceiros e indicadores.
2. Escolha uma pergunta de negocio para cada tema de RH citado no curso.
3. Para cada pergunta, diga qual arquivo de dados voce usaria primeiro.

### Desafio

Monte um mini plano de analise com cinco linhas: pergunta, base, indicador, comparacao e decisao possivel. Use um tema que a pessoa estudante ache interessante no dia a dia de RH.

## Fechamento

A regra mais importante do curso e esta: nao comece pelo grafico, pela formula ou pelo modelo. Comece pela pergunta. Uma boa pergunta protege a analise de virar apenas uma colecao de numeros bonitos.
