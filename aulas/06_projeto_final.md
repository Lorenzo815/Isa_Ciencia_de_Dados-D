# Projeto final: Mini People Analytics para RH

## Objetivo do projeto

Construir uma analise completa, do dado bruto a recomendacao, usando temas reais de RH. O projeto final integra Excel, Python, estatistica, visualizacao, indicadores e modelagem.

A entrega deve mostrar que a pessoa estudante nao apenas sabe calcular numeros, mas sabe construir uma narrativa analitica responsavel.

## 1. Contexto do desafio

A diretoria de RH quer entender se os processos da area estao saudaveis e onde deve priorizar energia nos proximos meses.

As perguntas principais sao:

1. O processo de recrutamento esta ficando mais rapido, mais caro ou mais seletivo?
2. Treinamentos estao sendo concluidos e percebidos como eficazes?
3. Existem sinais de risco em turnover, absenteismo, horas extras ou ponto?
4. A empresa acompanha representatividade e equidade com cuidado suficiente?
5. Ha oportunidades de corte de gastos sem prejudicar experiencia ou compliance?

## 2. Bases disponiveis

Use os arquivos em `dados/`:

- `vagas_recrutamento.csv`
- `treinamentos.csv`
- `colaboradores.csv`
- `ponto_horas.csv`
- `terceiros.csv`
- `indicadores_mensais.csv`

Opcionalmente, use um dataset publico baixado para `dados_kaggle/`, mas ele deve aparecer como pratica complementar, nao substituir a analise principal.

## 3. Entregaveis

A pessoa estudante deve entregar:

- Uma planilha ou notebook com calculos reproduziveis.
- De 4 a 6 graficos.
- Um resumo executivo de ate uma pagina.
- Uma secao de limitacoes.
- Tres recomendacoes praticas.
- Uma reflexao etica sobre uso de dados de RH.

## 4. Indicadores minimos

### Recrutamento

- Time to hire medio.
- Time to hire por source of hire.
- Candidatos por vaga.
- Entrevistas por candidato.
- Custo medio de divulgacao por contratado.

### Treinamento

- Horas medias por pessoa treinada.
- Taxa de conclusao.
- Nota media de eficacia.
- Custo de coffee por modalidade.
- Comparacao entre treinamentos obrigatorios e nao obrigatorios.

### Cargos, salarios e representatividade

- Headcount por area.
- Representatividade por genero e raca.
- Salario medio e mediano por nivel.
- Distribuicao salarial por area ou nivel.
- Discussao de limites: nao concluir equidade apenas com medias simples.

### Departamento pessoal

- Taxa de absenteismo.
- Horas extras totais.
- Horas extras indevidas pelo Artigo 58.
- Divergencias de ponto por area ou mes.

### Metas e indicadores

- Turnover mensal.
- Retencao por diversidade.
- Corte de gastos estimado.
- Relacao exploratoria entre absenteismo e horas extras.

## 5. Analise estatistica minima

Inclua pelo menos uma analise estatistica alem de medias simples:

- Comparacao de medias entre dois grupos.
- Correlacao entre duas variaveis numericas.
- Teste t para diferenca de medias.
- Qui-quadrado para associacao entre duas categorias.

A analise deve vir com interpretacao. Nao basta mostrar p-valor.

Modelo de frase:

> Neste conjunto didatico, observamos diferenca entre os grupos. O resultado sugere uma hipotese para investigacao, mas nao prova causalidade nem deve ser usado isoladamente para decisao.

## 6. Modelo preditivo minimo

Inclua pelo menos um dos modelos:

- Regressao linear para `time_to_hire_dias`.
- Arvore de decisao para `desligou_12m`.

A explicacao deve conter:

- Variavel alvo.
- Variaveis explicativas.
- Metrica usada.
- Resultado principal.
- Limitacao.
- Cuidado etico.

## 7. Estrutura sugerida da apresentacao

1. Titulo e pergunta central.
2. Contexto de RH.
3. Bases utilizadas.
4. Qualidade e preparacao dos dados.
5. Indicadores principais.
6. Graficos e achados.
7. Analise estatistica.
8. Modelo preditivo, se usado.
9. Recomendacoes.
10. Limitacoes e proximos passos.

## 8. Como formular boas recomendacoes

Uma recomendacao deve ser especifica, viavel e ligada a evidencia.

Fraca:

> Melhorar recrutamento.

Melhor:

> Revisar o funil de vagas senior divulgadas no LinkedIn, porque elas apresentam time to hire mais alto no dataset didatico. Antes de mudar investimento, comparar por cargo e etapa do processo.

Fraca:

> Reduzir horas extras.

Melhor:

> Investigar areas com concentracao de horas extras indevidas pelo Artigo 58 e divergencias de ponto, priorizando ajuste de escala, orientacao de liderancas e revisao de marcacoes.

## Perguntas e respostas

**Preciso fazer tudo em Python?**

Nao. O projeto pode combinar Excel e Python. O importante e que os calculos sejam claros, verificaveis e bem explicados.

**Quantos graficos devo usar?**

Use poucos graficos bons. Quatro graficos bem escolhidos valem mais que quinze graficos repetitivos.

**Posso usar modelo preditivo mesmo com dataset pequeno?**

Sim, para fins didaticos. Mas explique claramente que o modelo nao deve ser tratado como pronto para decisao real.

**O que faz uma recomendacao ser boa?**

Ela nasce de uma evidencia, reconhece limitacoes e aponta uma acao possivel. Recomendacao boa nao exagera a certeza.

**Como falar de diversidade sem cair em conclusoes indevidas?**

Use dados agregados, fale de representatividade e barreiras, evite julgamentos individuais e destaque que dados sensiveis exigem governanca.

## Exercicios

### Fixacao

1. Escolha tres indicadores e escreva suas formulas.
2. Identifique a unidade de analise de cada arquivo em `dados/`.
3. Liste tres possiveis problemas de qualidade de dados no mundo real.

### Aplicacao

1. Monte uma tabela de KPIs de recrutamento.
2. Monte uma tabela de KPIs de treinamento.
3. Crie pelo menos um grafico de tendencia mensal.
4. Crie pelo menos um grafico de comparacao entre grupos.
5. Rode um teste estatistico ou uma correlacao e interprete.

### Desafio

Monte a entrega final completa. Ela deve responder uma pergunta central, apresentar evidencias, incluir pelo menos uma analise estatistica, usar ou discutir um modelo preditivo e terminar com tres recomendacoes praticas.

## Rubrica de avaliacao

| Criterio | Excelente | Em desenvolvimento |
|---|---|---|
| Pergunta | Clara, especifica e ligada a decisao | Generica ou sem decisao associada |
| Dados | Bases identificadas e unidade de analise clara | Bases usadas sem explicacao |
| Indicadores | Formulas corretas e interpretadas | Indicadores apenas calculados |
| Visualizacao | Graficos simples, legiveis e relevantes | Graficos poluidos ou desconectados |
| Estatistica | Reconhece incerteza e limitações | Usa estatistica como certeza absoluta |
| Modelo | Explica alvo, variaveis, metrica e limite | Mostra resultado sem interpretacao |
| Etica | Considera dados sensiveis e impacto humano | Ignora riscos de uso dos dados |
| Comunicacao | Recomenda acoes praticas | Apenas descreve numeros |

## Fechamento

O projeto final e a prova de que ciencia de dados nao e apenas tecnica. E tecnica com pergunta, contexto, responsabilidade e comunicacao. Em RH, uma boa analise deve ajudar a cuidar melhor dos processos e das pessoas.
