# Aula 2: Estatistica para RH sem susto

## Objetivo da aula

Entender os conceitos estatisticos que sustentam boas decisoes de RH: media, mediana, dispersao, proporcao, correlacao, amostra, incerteza, hipotese e teste estatistico.

Esta aula nao tenta transformar a pessoa estudante em estatistica profissional. O objetivo e formar intuicao: saber quando uma diferenca e grande, quando pode ser acaso, quando uma media engana e quando uma conclusao precisa de mais dados.

## 1. Por que RH precisa de estatistica

RH lida com variacao o tempo todo. Pessoas tem salarios diferentes, tempos de empresa diferentes, jornadas diferentes, historicos diferentes e experiencias diferentes. Uma unica medida raramente conta a historia inteira.

Estatistica ajuda a responder perguntas como:

- O turnover aumentou de verdade ou apenas oscilou?
- A media salarial representa bem a empresa?
- Uma modalidade de treinamento tem avaliacao melhor que outra?
- Horas extras e absenteismo parecem caminhar juntos?
- Uma diferenca entre grupos e grande o suficiente para investigar?

Sem estatistica, a analise tende a depender de impressao. Com estatistica, a impressao vira uma hipotese que pode ser examinada.

## 2. Media, mediana e moda

A media soma todos os valores e divide pela quantidade de observacoes. Ela e util quando queremos uma medida geral, mas pode ser puxada por valores extremos.

A mediana e o valor central quando os dados estao ordenados. Ela costuma ser melhor para salarios, porque salarios muito altos de lideranca podem puxar a media para cima.

A moda e o valor mais frequente. Em RH, ela pode ajudar em categorias, como source of hire mais comum ou modalidade de treinamento mais frequente.

Exemplo: imagine salarios de 2.000, 2.200, 2.300, 2.500 e 20.000. A media sera muito maior que a realidade da maior parte das pessoas. A mediana mostrara melhor o centro do grupo.

## 3. Dispersao: a parte esquecida da media

Dispersao e o quanto os dados se espalham. Duas areas podem ter o mesmo salario medio e realidades muito diferentes.

Indicadores de dispersao:

- Minimo: menor valor observado.
- Maximo: maior valor observado.
- Amplitude: maximo menos minimo.
- Quartis: pontos que dividem os dados em quatro partes.
- Desvio padrao: medida de espalhamento em torno da media.

Em cargos e salarios, dispersao alta dentro do mesmo nivel pode indicar diferencas de tempo de empresa, performance, escopo, negociacao, historico de reajustes ou possiveis problemas de equidade.

## 4. Proporcoes e taxas

Muitos indicadores de RH sao proporcoes. Uma proporcao sempre tem numerador e denominador.

Exemplos:

```text
taxa_conclusao = concluidos / total_inscritos
turnover = demitidos / headcount_medio
absenteismo = dias_ausentes / dias_previstos_de_trabalho
representatividade = pessoas_do_grupo / total_de_pessoas
```

Perguntas obrigatorias:

- Quem esta no numerador?
- Quem esta no denominador?
- Qual periodo foi considerado?
- O indicador e por pessoa, vaga, treinamento, area ou mes?

Uma taxa sem denominador claro e perigosa. Dizer que houve 8 desligamentos parece muito ou pouco dependendo se a empresa tem 30, 300 ou 3.000 pessoas.

## 5. Correlacao nao e causalidade

Correlacao mede associacao entre duas variaveis. Quando uma sobe e a outra tambem tende a subir, a correlacao e positiva. Quando uma sobe e a outra tende a cair, a correlacao e negativa.

Mas correlacao nao prova causa.

Exemplo: horas de treinamento e performance podem estar positivamente correlacionadas. Isso pode significar que treinamento melhora performance, mas tambem pode significar que pessoas de alta performance recebem mais oportunidades de treinamento. Tambem pode haver uma terceira variavel, como lideranca, area ou tempo de empresa.

Em RH, essa cautela e vital porque decisoes afetam pessoas. Uma correlacao deve abrir investigacao, nao encerrar debate.

## 6. Amostra, populacao e incerteza

Populacao e o conjunto completo que queremos entender. Amostra e uma parte desse conjunto.

Se a empresa tem 1.000 colaboradores e apenas 35 responderam uma pesquisa de eficacia de treinamento, a resposta pode ser enviesada. Talvez tenham respondido justamente as pessoas mais engajadas ou mais insatisfeitas.

Quanto menor e menos representativa a amostra, maior deve ser a cautela. Incerteza nao e defeito da analise; e parte honesta da analise.

## 7. Hipoteses

Uma hipotese e uma afirmacao que pode ser investigada com dados.

Exemplos:

- Treinamentos presenciais tem nota de eficacia maior que treinamentos online.
- Vagas de senioridade senior demoram mais para fechar.
- Areas operacionais concentram mais horas extras.
- Pessoas com maior absenteismo apresentam maior risco de desligamento.

Uma boa hipotese tem tres caracteristicas: e especifica, pode ser medida e esta ligada a uma decisao ou investigacao real.

## 8. Testes estatisticos

Testes estatisticos ajudam a avaliar se uma diferenca observada pode ser explicada apenas por variacao aleatoria. Eles geralmente trabalham com duas ideias:

**Hipotese nula:** nao ha diferenca ou associacao relevante.

**Hipotese alternativa:** ha diferenca ou associacao.

O p-valor indica, de forma simplificada, quao surpreendente seria observar aquele resultado se a hipotese nula fosse verdadeira. Um p-valor pequeno sugere que o resultado observado seria improvavel apenas por acaso.

Mas cuidado: p-valor nao mede importancia pratica. Uma diferenca pode ser estatisticamente detectavel e ainda assim pequena demais para justificar uma acao. Tambem pode acontecer o contrario: uma diferenca importante para o negocio nao aparecer como estatisticamente significativa porque a amostra e pequena.

## 9. Testes que aparecem no curso

**Teste t:** compara medias entre dois grupos. Exemplo: horas extras medias em Operacoes versus outras areas.

**Qui-quadrado:** avalia associacao entre variaveis categoricas. Exemplo: treinamento obrigatorio versus conclusao.

**Correlacao:** avalia associacao linear entre duas variaveis numericas. Exemplo: absenteismo e horas extras.

## 10. Etica em estatistica de RH

Analises de genero, raca, idade, salario, desempenho, ponto e desligamento precisam de cuidado especial.

Boas praticas:

- Agregar resultados quando possivel.
- Evitar expor individuos desnecessariamente.
- Usar dados sensiveis para medir desigualdades e barreiras, nao para reforca-las.
- Documentar limitacoes.
- Separar achado estatistico de decisao administrativa.

## Perguntas e respostas

**Media alta significa que todo mundo esta bem?**

Nao. A media pode esconder desigualdades. Sempre olhe dispersao, mediana e distribuicao por grupo.

**Quando devo usar mediana em vez de media?**

Use mediana quando houver valores extremos ou distribuicao muito assimetrica, como salarios, custos e tempos muito longos de contratacao.

**Um p-valor maior que 0,05 prova que nao existe diferenca?**

Nao. Ele indica que, com aqueles dados, nao ha evidencia estatistica suficiente. Pode faltar amostra, qualidade de dado ou uma medida melhor.

**Se duas variaveis tem correlacao alta, posso agir direto?**

Nao sem contexto. Correlacao ajuda a priorizar investigacao. Para agir, combine dados, conhecimento do processo e escuta qualitativa.

**Dados sensiveis devem ser removidos da analise?**

Depende da pergunta e da governanca. Para medir equidade e representatividade, dados sensiveis podem ser necessarios. O ponto e usa-los com finalidade clara, protecao e responsabilidade.

## Exercicios

### Fixacao

1. Explique a diferenca entre media e mediana usando salarios.
2. Crie um exemplo em que uma contagem engana e uma taxa ajuda.
3. Escreva uma hipotese nula e uma hipotese alternativa para treinamentos.
4. Explique por que correlacao nao prova causalidade.

### Aplicacao

1. Em `dados/colaboradores.csv`, compare salario medio e mediano por `nivel`.
2. Em `dados/indicadores_mensais.csv`, calcule o turnover mensal e identifique o maior mes.
3. Em `dados/treinamentos.csv`, compare taxa de conclusao por `modalidade`.
4. Em `dados/ponto_horas.csv`, observe se horas extras indevidas parecem concentradas em algum mes ou area.

### Desafio

Escolha uma hipotese de RH e escreva uma mini analise com: pergunta, variaveis, indicador, possivel teste estatistico, interpretacao esperada e cuidado etico.

## Fechamento

Estatistica nao serve para dar uma aura de certeza a uma decisao. Ela serve para tornar a incerteza visivel. Em RH, essa humildade e uma virtude: protege pessoas, melhora processos e evita conclusoes apressadas.
