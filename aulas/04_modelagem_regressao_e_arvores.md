# Aula 4: Modelagem preditiva, regressao linear e arvores de decisao

## Objetivo da aula

Entender o que e um modelo preditivo, quando ele faz sentido e como interpretar dois modelos introdutorios: regressao linear e arvore de decisao.

A meta nao e apenas rodar `scikit-learn`. A meta e entender o raciocinio: qual variavel queremos prever, quais informacoes usamos, como avaliamos erro e como comunicamos limites.

## 1. O que e um modelo preditivo

Um modelo preditivo e uma funcao que aprende padroes em dados historicos para estimar um resultado em novos casos.

Em RH, exemplos possiveis:

- Prever time to hire de uma vaga.
- Estimar custo de divulgacao por contratacao.
- Classificar risco de desligamento.
- Identificar treinamentos com maior chance de nao conclusao.
- Priorizar auditoria de divergencias de ponto.

Um modelo nao entende pessoas, cultura ou contexto sozinho. Ele aprende relacoes nos dados disponiveis. Se os dados forem incompletos, enviesados ou antigos, o modelo herdara esses problemas.

## 2. Variavel alvo e variaveis explicativas

A variavel alvo e o que queremos prever.

As variaveis explicativas sao as informacoes usadas para fazer a previsao.

Exemplo de regressao:

```text
alvo = time_to_hire_dias
explicativas = candidatos, entrevistas, ofertas, senioridade, source_of_hire, area
```

Exemplo de classificacao:

```text
alvo = desligou_12m
explicativas = tempo_empresa, absenteismo, horas_extras, treinamento, nota_performance
```

Uma regra importante: use apenas dados que estariam disponiveis no momento da decisao. Se voce usa uma informacao que so aparece depois do evento, cria vazamento de dados.

## 3. Treino, teste e generalizacao

Para avaliar um modelo, separamos dados em treino e teste.

- Treino: parte usada para o modelo aprender.
- Teste: parte guardada para avaliar se ele funciona em dados que nao viu.

Isso simula uma situacao real. O objetivo nao e decorar o passado, mas generalizar para casos novos.

Quando um modelo se ajusta demais ao treino e falha no teste, chamamos de overfitting. Em linguagem simples: ele decorou exemplos em vez de aprender um padrao util.

## 4. Regressao linear

Regressao linear e usada quando a variavel alvo e numerica. Ela tenta encontrar uma relacao aproximadamente linear entre as variaveis explicativas e o resultado.

Exemplo de RH:

> Com base no historico de vagas, estimar quantos dias uma nova vaga pode levar para fechar.

A forma conceitual e:

```text
time_to_hire = intercepto + peso_1 * candidatos + peso_2 * entrevistas + ... + erro
```

Cada peso indica como o modelo relaciona uma variavel ao resultado, mantendo as demais no contexto do modelo.

Cuidado: regressao linear supoe uma relacao simples. Processos de RH podem ter efeitos nao lineares, gargalos, sazonalidade e mudancas de politica.

## 5. Metricas de regressao

**Erro medio absoluto:** mostra, em media, quanto o modelo erra na unidade original. Se o alvo e dias, o erro tambem e em dias. E uma metrica facil de explicar.

**R²:** indica quanto da variacao do alvo o modelo consegue explicar. Pode ser util, mas nao deve ser interpretado sozinho.

Exemplo de comunicacao:

> O modelo erra em media 6 dias na base de teste. Isso significa que ele pode apoiar planejamento, mas nao deve ser usado como promessa de SLA.

## 6. Arvore de decisao

Arvore de decisao e um modelo que cria regras sucessivas para separar os dados.

Exemplo simplificado:

```text
Se absenteismo_dias_ano > 8:
    risco de desligamento aumenta
Senao, se nota_performance > 4:
    risco de desligamento diminui
```

A vantagem da arvore e interpretabilidade. A pessoa consegue ler as regras. A desvantagem e que arvores podem decorar padroes se ficarem profundas demais.

Por isso, nos notebooks usamos profundidade limitada. Uma arvore menor geralmente e menos precisa no treino, mas mais facil de explicar e menos propensa a overfitting.

## 7. Metricas de classificacao

Quando o alvo e uma classe, como desligou ou nao desligou, usamos metricas de classificacao.

**Acuracia:** percentual geral de acertos. Pode enganar se uma classe for muito mais comum.

**Matriz de confusao:** mostra acertos e erros por classe.

**Recall:** entre os casos positivos reais, quantos o modelo encontrou.

**Precisao:** entre os casos que o modelo marcou como positivos, quantos eram positivos de fato.

Em turnover, falsos positivos e falsos negativos tem impactos diferentes. Um falso positivo pode gerar preocupacao indevida; um falso negativo pode perder chance de apoio. A metrica deve ser escolhida com a finalidade do uso.

## 8. Etica e governanca em modelos de RH

Modelos de RH exigem cuidado especial porque podem afetar oportunidades, reputacao, remuneracao e permanencia de pessoas.

Principios:

- Nao usar modelo como decisor automatico de contratacao, promocao ou desligamento.
- Avaliar vieses por grupo quando houver dados sensiveis e base legal/etica para isso.
- Explicar finalidade e limitacoes.
- Proteger dados pessoais.
- Usar resultados para melhorar processos e condicoes, nao para punir individuos.

## Perguntas e respostas

**Quando uso regressao e quando uso classificacao?**

Use regressao quando quer prever um numero, como dias, custo ou salario. Use classificacao quando quer prever uma categoria, como concluiu ou nao concluiu, desligou ou nao desligou.

**Um modelo com alta acuracia e sempre bom?**

Nao. Se 95% das pessoas nao desligam, um modelo que sempre diz "nao desligou" pode ter 95% de acuracia e ainda ser inutil para identificar risco.

**Posso usar genero ou raca em modelos?**

Depende da finalidade, governanca e contexto legal. Em geral, dados sensiveis devem ser usados com muito cuidado, frequentemente para auditar equidade, nao para tomar decisao individual automatizada.

**O que e vazamento de dados?**

E quando o modelo usa uma informacao que nao estaria disponivel no momento da previsao. Isso faz o desempenho parecer melhor do que seria na vida real.

**Por que modelos pequenos sao bons para aprendizado?**

Porque sao mais faceis de entender. Em RH, interpretabilidade muitas vezes importa tanto quanto desempenho.

## Exercicios

### Fixacao

1. Defina variavel alvo e variaveis explicativas.
2. Explique a diferenca entre treino e teste.
3. Diga por que erro medio absoluto e facil de comunicar.
4. Explique por que acuracia pode enganar.

### Aplicacao

1. Abra `notebooks/04_regressao_linear_time_to_hire.ipynb` e rode as celulas.
2. Registre o erro medio absoluto do modelo de regressao.
3. Abra `notebooks/05_arvore_decisao_turnover.ipynb` e rode as celulas.
4. Leia as regras da arvore e traduza uma delas para linguagem de RH.

### Desafio

Escreva uma nota executiva explicando um dos modelos para uma lideranca de RH. A nota deve conter objetivo, dados usados, metrica, achado, limitacao e cuidado etico.

## Fechamento

Modelos sao ferramentas de previsao, nao maquinas de verdade. Um bom analista nao pergunta apenas "qual foi a acuracia?". Pergunta tambem: para que serve, quem pode ser afetado, quais dados faltam e como explicar o resultado com honestidade.
