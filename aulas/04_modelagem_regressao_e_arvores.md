# Aula 4: Modelagem preditiva, regressao linear e arvores de decisao

## Objetivo da aula

Entender o que e um modelo preditivo, quando ele faz sentido e como interpretar dois modelos introdutorios: regressao linear e arvore de decisao.

A meta nao e apenas rodar `scikit-learn`. A meta e entender o raciocinio: qual variavel queremos prever, quais informacoes usamos, como avaliamos erro e como comunicamos limites.

## 1. O que e um modelo preditivo

Um modelo preditivo e uma "formula aprendida" que recebe informacoes conhecidas sobre um caso e devolve uma previsao sobre algo desconhecido. Em vez de voce escrever a formula a mao, o algoritmo encontra a melhor formula olhando muitos exemplos historicos.

Dois tipos basicos:

- **Regressao:** preve um numero. Ex: quantos dias uma vaga vai levar para fechar.
- **Classificacao:** preve uma categoria. Ex: essa pessoa tem alto ou baixo risco de se desligar.

Em RH, exemplos possiveis:

- Prever `time_to_hire` de uma vaga nova (regressao).
- Estimar custo de divulgacao por contratacao (regressao).
- Classificar risco de desligamento (classificacao).
- Identificar treinamentos com maior chance de nao conclusao (classificacao).
- Priorizar auditoria de divergencias de ponto (classificacao).

Um modelo nao entende pessoas, cultura ou contexto sozinho. Ele so aprende relacoes presentes nos dados que voce der. Se os dados forem incompletos, enviesados ou antigos, o modelo herdara esses problemas e os apresentara como se fossem verdades.

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

Para avaliar um modelo, separamos os dados historicos em dois pedacos:

- **Treino:** parte usada para o modelo aprender os padroes. Costuma ser 70% a 80% dos dados.
- **Teste:** parte guardada para avaliar como ele se sai em casos que nao viu. Costuma ser 20% a 30%.

Isso simula uma situacao real: no dia a dia, voce vai usar o modelo em vagas ou pessoas novas. Se ele so funcionar nos dados em que aprendeu, e inutil.

O objetivo nao e **decorar** o passado, e sim **generalizar** para casos novos.

**Overfitting** (super-ajuste) acontece quando o modelo decora o treino e falha no teste. E como um estudante que decora as respostas da prova antiga mas erra a prova nova. Sinal classico: desempenho otimo no treino e ruim no teste.

**Underfitting** (sub-ajuste) e o oposto: o modelo e tao simples que nao aprende nem o treino. Sinal: desempenho ruim em ambos.

A arte de modelar e ficar no meio: aprender o suficiente para generalizar, sem decorar.

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

Uma metrica e um numero que resume o quao bem o modelo esta acertando. Para regressao, as duas mais usadas sao:

**Erro medio absoluto (MAE):** pega cada erro (previsto menos real), tira o sinal (valor absoluto) e calcula a media. Mostra, em media, o quanto o modelo erra na unidade original. Se o alvo e `time_to_hire_dias`, o MAE tambem e em dias. E a metrica mais facil de explicar para uma pessoa de negocio.

**R² (R quadrado, ou coeficiente de determinacao):** indica que fracao da variacao do alvo o modelo consegue explicar. Vai de 0 (o modelo nao explica nada melhor que a media) a 1 (explica perfeitamente). Pode ser negativo se o modelo for pior que simplesmente "chutar a media".

  - R² = 0,80 significa que 80% da variacao do alvo e capturada pelas variaveis explicativas.
  - R² alto nao garante que o modelo seja util: ele pode ter aprendido com vazamento de dados ou estar superajustado.
  - R² baixo nao significa que o modelo seja inutil: em RH, fenomenos sao complexos, e R² de 0,3 ja pode ajudar uma decisao.

Exemplo de comunicacao:

> O modelo erra em media 6 dias na base de teste (MAE = 6) e explica cerca de 40% da variacao do tempo de fechamento (R² = 0,40). Isso significa que ele pode apoiar planejamento de recrutamento, mas nao deve ser usado como promessa de SLA.

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

Quando o alvo e uma classe (como "desligou" ou "nao desligou"), nao faz sentido calcular erro em dias ou em reais. Usamos metricas que olham acertos e erros por categoria.

Antes das metricas, quatro contagens basicas. Imagine que voce esta tentando prever quem vai se desligar:

- **VP (verdadeiro positivo):** o modelo disse "vai desligar" e a pessoa desligou. Acerto.
- **VN (verdadeiro negativo):** o modelo disse "nao vai desligar" e a pessoa ficou. Acerto.
- **FP (falso positivo):** o modelo disse "vai desligar" e a pessoa ficou. Alarme falso.
- **FN (falso negativo):** o modelo disse "nao vai desligar" e a pessoa desligou. Alarme perdido.

A **matriz de confusao** e uma tabela 2x2 que mostra essas quatro contagens lado a lado. E a foto mais completa do desempenho.

A partir delas:

**Acuracia:** (VP + VN) / total. Percentual geral de acertos. Pode enganar se uma classe for muito mais comum: se so 5% desliga, um modelo que sempre diz "nao desliga" tem 95% de acuracia e e inutil para o problema.

**Recall (ou sensibilidade):** VP / (VP + FN). Entre todos que realmente desligaram, quantos o modelo conseguiu encontrar. Alto recall = poucos alarmes perdidos. Importante quando perder um caso e custoso.

**Precisao:** VP / (VP + FP). Entre todos os que o modelo marcou como "vai desligar", quantos realmente desligaram. Alta precisao = poucos alarmes falsos. Importante quando agir indevidamente custa caro.

**F1:** uma media harmonica entre precisao e recall, util quando voce quer um numero unico que equilibre os dois.

Em turnover, falsos positivos e falsos negativos tem impactos diferentes. Um falso positivo pode gerar preocupacao indevida sobre alguem que ia ficar; um falso negativo pode fazer voce perder a chance de uma conversa de retencao com quem realmente ia sair. A metrica certa depende de qual erro doi mais para o RH.

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
