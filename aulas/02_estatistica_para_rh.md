# Aula 2: Estatistica para RH sem susto

## Objetivo da aula

Construir, do zero, a intuicao estatistica necessaria para tomar decisoes melhores em RH. Esta aula assume que voce nunca estudou estatistica formalmente. Cada termo novo aparece com uma definicao em linguagem simples, um exemplo de RH e, quando possivel, uma analogia visual.

Ao final, voce deve conseguir:

- Olhar para uma coluna de dados e descrever a forma dela em palavras.
- Escolher entre media, mediana ou moda dependendo do que os dados parecem.
- Entender o que e uma "distribuicao normal" e por que ela importa.
- Diferenciar correlacao de causalidade.
- Ler uma hipotese e um `p-valor` sem se intimidar.
- Decidir entre um teste parametrico e um nao parametrico, com argumento.

Esta aula nao quer transformar voce em estatistica profissional. Ela quer dar coragem para usar estatistica como uma lente de leitura, nao como uma caixa preta.

## 0. Antes de comecar: palavras que vao aparecer

Antes de mergulhar, vale fixar dez palavras que vao aparecer o tempo todo. Nao precisa decorar agora; volte aqui sempre que cruzar com um termo desconhecido.

| Palavra | O que significa em uma frase |
|---|---|
| **Variavel** | Uma caracteristica medida ou observada (ex: `salario`, `area`, `idade`). |
| **Observacao** | Uma linha da tabela. Em RH, costuma ser uma pessoa, uma vaga ou um mes. |
| **Distribuicao** | A forma como os valores de uma variavel se espalham. Algumas concentradas, outras espalhadas. |
| **Amostra** | Um pedaco dos dados que voce conseguiu coletar. Quase nunca temos todo mundo. |
| **Populacao** | O grupo completo que voce gostaria de entender (ex: todos os colaboradores da empresa, hoje e no futuro). |
| **Hipotese** | Uma afirmacao testavel. Ex: "homens e mulheres ganham, em media, salarios diferentes". |
| **Significancia (p-valor)** | O quanto seria estranho ver esse resultado por puro acaso. |
| **Outlier** | Um valor extremo, muito acima ou abaixo dos outros. Pode ser real, erro de digitacao ou caso raro. |
| **Variancia / desvio padrao** | Duas medidas de "o quanto os dados se espalham em torno da media". |
| **Distribuicao normal** | A famosa forma de sino. Muitas variaveis naturais se parecem com ela. |

Os proximos capitulos explicam cada um desses termos com calma.

## 1. Por que RH precisa de estatistica

RH lida com variacao o tempo todo. Pessoas tem salarios diferentes, tempos de empresa diferentes, jornadas diferentes, historicos diferentes e experiencias diferentes. Uma unica medida raramente conta a historia inteira.

Estatistica ajuda a responder perguntas como:

- O turnover aumentou de verdade ou apenas oscilou de um mes para o outro?
- A media salarial representa bem a empresa, ou alguns salarios altos puxam tudo para cima?
- Uma modalidade de treinamento tem avaliacao mesmo melhor que outra?
- Horas extras e absenteismo parecem caminhar juntos?
- Uma diferenca observada entre dois grupos e grande o suficiente para investigar?

Sem estatistica, a analise depende de impressao ("achei que estava aumentando"). Com estatistica, a impressao vira uma hipotese que pode ser examinada. A pergunta deixa de ser "eu estou certo?" e vira "o que esses dados conseguem, de fato, sustentar?".

## 2. Tipos de variavel: o primeiro filtro

Antes de calcular qualquer coisa, classifique a variavel. O tipo dela determina o que faz sentido calcular e qual teste usar.

**Variavel numerica continua:** valores que podem assumir qualquer numero dentro de um intervalo. Aceitam casas decimais.

- Exemplos em RH: `salario_mensal`, `horas_treinamento`, `tempo_empresa_meses`.
- Faz sentido calcular: media, mediana, desvio padrao, correlacao.

**Variavel numerica discreta (contagem):** numeros inteiros que contam quantas vezes algo aconteceu.

- Exemplos: `dias_de_falta`, `numero_de_filhos`, `quantidade_de_divergencias_de_ponto`.
- Cuidado: medias podem dar resultados estranhos ("1,7 dias de falta"). Costumam ser assimetricas (muitos zeros).

**Variavel categorica nominal:** rotulos sem ordem natural.

- Exemplos: `area`, `genero`, `source_of_hire`.
- Nao faz sentido calcular media. Use proporcoes e tabelas de contagem.

**Variavel categorica ordinal:** rotulos com ordem, mas sem distancia clara entre eles.

- Exemplos: `senioridade` (junior, pleno, senior), `nota_avaliacao` em escala (ruim, regular, bom, otimo).
- Pode usar mediana e quartis; medias podem ate ser uteis, com cautela.

Marque cada coluna do seu dataset com um destes quatro rotulos antes de continuar. Esse exercicio simples evita metade dos erros de iniciante.

## 3. Distribuicao: a forma dos dados

Distribuicao e simplesmente o desenho que sai quando voce empilha os valores de uma variavel por faixa. Imagine pegar todos os salarios da empresa, agrupar de mil em mil reais e desenhar uma coluna para cada faixa, com altura igual a quantidade de pessoas naquela faixa. Esse desenho e um **histograma**, e o formato geral dele e a **distribuicao**.

Formatos que voce vai reconhecer com pratica:

- **Sino simetrico:** maioria no meio, pouco nos extremos, lados parecidos. E o formato da famosa **distribuicao normal**.
- **Assimetrica a direita (cauda longa a direita):** maioria de valores baixos, alguns muito altos puxando o lado direito. Tipico de salarios e tempo de empresa.
- **Assimetrica a esquerda:** o contrario. Comum em notas de avaliacao quando quase todo mundo recebe nota alta.
- **Bimodal (dois picos):** dois grupos misturados, cada um com seu centro. Costuma sinalizar que existem duas populacoes diferentes dentro do mesmo dado.
- **Uniforme:** todos os valores aparecem com frequencia parecida. Raro em RH.

Por que isso importa? Porque quase tudo que vamos fazer depois (escolher media ou mediana, escolher teste parametrico ou nao, interpretar correlacoes) muda dependendo da forma. Olhar a forma antes de calcular qualquer numero e a regra de ouro.

## 4. Medidas de tendencia central: media, mediana e moda

Sao tres maneiras diferentes de responder "qual o valor `tipico` desse grupo?". Cada uma protege contra um problema diferente.

**Media:** soma todos os valores e divide pela quantidade. E util quando os dados sao simetricos, mas pode ser puxada por valores extremos.

**Mediana:** ordene os valores do menor para o maior; a mediana e o valor que fica exatamente no meio. Metade da turma esta abaixo dela, metade acima. E robusta contra valores extremos.

**Moda:** o valor que mais se repete. Util em variaveis categoricas (source of hire mais comum) ou para identificar concentracoes.

Exemplo concreto. Imagine cinco salarios em uma area pequena:

```text
2.000   2.200   2.300   2.500   20.000
```

- Media = (2.000 + 2.200 + 2.300 + 2.500 + 20.000) / 5 = `5.800`
- Mediana = `2.300` (terceiro valor, ja que estao ordenados)
- Moda = nao ha repeticao, nao se aplica

A media diz `5.800`, mas quase ninguem ganha isso. A mediana, `2.300`, descreve melhor o grupo. Esse e o efeito de um **outlier** (o salario de 20.000) sobre a media. Por isso, em salarios, custos e tempos de processo, prefira a mediana.

Regra pratica: se media e mediana estao proximas, a distribuicao e simetrica. Se sao muito diferentes, ha assimetria ou outliers. Calcule sempre as duas e compare.

## 5. Outliers: amigos ou inimigos?

Outlier e um valor muito distante dos demais. Em uma planilha de salarios entre 2 e 5 mil, um salario de 50 mil e um outlier.

Existem tres origens possiveis, e cada uma pede uma decisao diferente:

1. **Erro de digitacao ou sistema.** Ex: salario `200.000` em vez de `2.000`. Decisao: corrigir ou excluir.
2. **Caso real e raro.** Ex: salario de um C-level. Decisao: manter, mas reportar separadamente. Considere usar mediana e relatar o outlier.
3. **Sub-populacao misturada.** Ex: estagiarios e diretores na mesma tabela. Decisao: separar grupos antes de analisar.

Nunca remova um outlier sem investigar. Outliers as vezes contam justamente a historia mais importante (uma area com horas extras absurdas, uma fonte de contratacao com custo desproporcional).

## 6. Dispersao: o quanto os dados se espalham

Dois grupos podem ter a mesma media e realidades completamente diferentes. Compare:

```text
Area A: salarios 3.000, 3.000, 3.000, 3.000, 3.000   -> media 3.000
Area B: salarios 1.500, 2.000, 3.000, 4.000, 4.500   -> media 3.000
```

Mesma media, dispersao totalmente diferente. Para descrever isso, usamos:

- **Minimo e maximo:** menor e maior valor.
- **Amplitude:** maximo menos minimo. Simples, mas muito sensivel a outliers.
- **Quartis (Q1, Q2, Q3):** dividem os dados ordenados em quatro partes iguais. Q2 e a mediana. Q1 e o valor abaixo do qual estao 25% das observacoes; Q3, 75%.
- **Intervalo interquartil (IQR = Q3 - Q1):** mede onde estao os 50% do meio. Muito menos sensivel a outliers do que a amplitude.
- **Variancia:** media dos quadrados das diferencas em relacao a media. Ela existe porque a soma simples das diferencas da zero (positivos cancelam negativos). Elevar ao quadrado resolve o cancelamento. O problema: a unidade fica estranha (`reais ao quadrado`).
- **Desvio padrao:** raiz quadrada da variancia. Volta para a unidade original (reais). E a forma mais usada de medir espalhamento em torno da media.

Em cargos e salarios, dispersao alta dentro do mesmo nivel pode indicar diferencas de tempo de empresa, performance, escopo, negociacao, historico de reajustes ou problemas de equidade. Dispersao baixa indica padronizacao (boa ou ma, depende do caso).

## 7. A distribuicao normal e a regra do sino

A distribuicao normal (tambem chamada de gaussiana) e aquela curva em forma de sino que aparece em quase todo livro de estatistica. Ela tem tres propriedades visiveis:

1. **Simetrica:** o lado esquerdo e o espelho do direito.
2. **Pico unico no centro:** a moda, a mediana e a media coincidem.
3. **Caudas que decaem rapido:** valores extremos sao raros.

Quando os dados seguem uma normal, vale uma regra util chamada **regra 68-95-99**:

- Cerca de **68%** das observacoes ficam dentro de um desvio padrao em torno da media.
- Cerca de **95%** ficam dentro de dois desvios padrao.
- Cerca de **99,7%** ficam dentro de tres desvios padrao.

Exemplo. Se `score_engajamento` tem media 70 e desvio padrao 12, esperamos que cerca de 95% das pessoas tenham score entre 46 e 94 (70 menos 2x12 e 70 mais 2x12). Quem cai fora disso e raro.

Por que a normal aparece tanto? Porque muitos fenomenos sao a soma de muitas pequenas influencias independentes. O **teorema central do limite** diz que, mesmo quando os dados nao sao normais, a media de varias amostras tende a se comportar como normal. Voce nao precisa memorizar o teorema; precisa saber que ele e a razao de testes parametricos funcionarem razoavelmente bem em amostras grandes mesmo quando os dados originais nao sao perfeitamente normais.

**Atencao:** muita coisa em RH NAO e normal. Salario tem cauda longa; absenteismo tem muitos zeros; tempo de empresa decai. Por isso, a primeira pergunta sempre e: "essa variavel parece um sino, ou nao?".

## 8. Proporcoes e taxas

Muitos indicadores de RH sao proporcoes. Uma proporcao sempre tem numerador (`quantos casos`) e denominador (`em quantos no total`).

```text
taxa_conclusao = concluidos / total_inscritos
turnover = demitidos / headcount_medio
absenteismo = dias_ausentes / dias_previstos_de_trabalho
representatividade = pessoas_do_grupo / total_de_pessoas
```

Perguntas obrigatorias antes de reportar qualquer taxa:

- Quem esta no numerador?
- Quem esta no denominador?
- Qual periodo foi considerado?
- O indicador e por pessoa, por vaga, por treinamento, por area ou por mes?

Uma taxa sem denominador claro e perigosa. Dizer "houve 8 desligamentos" parece muito ou pouco dependendo se a empresa tem 30, 300 ou 3.000 pessoas. Em RH, a frase "isso e muito?" so faz sentido depois de definir o denominador.

## 9. Correlacao: medir associacao sem afirmar causa

Correlacao mede o quanto duas variaveis variam juntas. O numero da correlacao varia entre -1 e +1.

- **+1:** quando uma sobe, a outra sobe sempre na mesma proporcao. Linha reta crescente.
- **0:** nao ha associacao linear visivel.
- **-1:** quando uma sobe, a outra cai sempre na mesma proporcao. Linha reta decrescente.

Na pratica, valores absolutos entre 0,1 e 0,3 indicam associacao fraca; 0,3 a 0,5 moderada; acima de 0,5 forte. Mas isso varia muito por area.

Existem duas correlacoes muito usadas:

- **Pearson:** mede o quanto a relacao e linear. Sensivel a outliers e exige variaveis aproximadamente simetricas.
- **Spearman:** transforma os valores em postos (1, 2, 3, ...) e mede o quanto uma cresce junto com a outra. Captura relacoes monotonicas, mesmo nao lineares, e e robusta contra outliers.

**Postos (ranks):** sao a posicao do valor depois de ordenar tudo. Se voce ordena os salarios e atribui 1 ao menor, 2 ao segundo menor, e assim por diante, voce esta criando postos. Testes nao parametricos trabalham com postos para nao depender do formato exato dos dados.

E o mais importante: **correlacao nao prova causa.** Se horas de treinamento e performance se correlacionam, pode ser que treinamento melhore performance, ou que pessoas com alta performance recebam mais oportunidades, ou que ambas dependam de uma terceira variavel (lideranca, area, tempo de empresa). Em RH, essa cautela e vital, porque decisoes afetam pessoas. Uma correlacao deve abrir investigacao, nao encerrar debate.

## 10. Amostra, populacao e incerteza

Populacao e o conjunto completo que voce gostaria de entender. Amostra e o pedaco que voce conseguiu medir.

Quase nunca temos a populacao inteira. Mesmo dados de RH "completos" sao uma amostra no tempo: representam quem esta na empresa hoje, nao quem entrou no ano passado e ja saiu, nem quem vai entrar amanha. Toda estatistica e, no fundo, uma tentativa de aprender sobre a populacao a partir de uma amostra.

Tres ideias importantes nascem disso:

1. **Tamanho importa.** Com 30 respostas, voce pode ver padroes que sao acaso. Com 3.000, pequenas diferencas viram quase certeza. Nem sempre "mais e melhor": importa tambem como os dados foram coletados.
2. **Vies de selecao.** Se 35 pessoas responderam uma pesquisa de eficacia em uma empresa de 1.000, provavelmente responderam as mais engajadas ou as mais insatisfeitas. A amostra nao e a populacao.
3. **Incerteza nao e defeito.** E parte honesta da analise. Dizer "estimamos turnover de 12% com margem de erro de mais ou menos 3 pontos" e mais responsavel que dizer "turnover e 12%".

## 11. Hipoteses: transformar opiniao em pergunta testavel

Uma hipotese e uma afirmacao especifica o suficiente para ser confrontada com dados. Toda analise estatistica de comparacao envolve duas hipoteses:

- **Hipotese nula (H0):** nao ha diferenca, ou nao ha associacao. E o estado "nada acontece aqui".
- **Hipotese alternativa (H1):** ha diferenca, ou ha associacao. E o que voce desconfia que esta acontecendo.

Por convencao, a estatistica protege a hipotese nula. Voce so a abandona quando os dados forem suficientemente surpreendentes contra ela. E como um julgamento: presuncao de inocencia ate prova em contrario.

Exemplos pareados para RH:

| Pergunta de negocio | H0 | H1 |
|---|---|---|
| Treinamento presencial tem nota maior que online? | As notas medias sao iguais. | A nota media presencial e maior. |
| Vagas senior demoram mais que pleno? | O tempo medio e igual. | O tempo medio senior e maior. |
| Genero e area estao associados? | Sao independentes. | Existe associacao. |

Uma boa hipotese tem tres caracteristicas: e especifica, pode ser medida com os dados disponiveis e esta ligada a uma decisao real.

## 12. p-valor: o que ele realmente diz

O `p-valor` e o numero mais malinterpretado da estatistica. A definicao formal e:

> p-valor e a probabilidade de observar um resultado tao extremo quanto o que vimos, ou mais extremo, supondo que a hipotese nula seja verdadeira.

Em portugues claro: "se H0 fosse verdadeira (nada acontece), com que frequencia o acaso, sozinho, produziria um resultado deste tamanho?". Se a resposta for "quase nunca", isso e uma evidencia contra H0.

Convencao mais comum:

- `p < 0,05`: o resultado seria raro sob H0; ha **evidencia** para rejeitar H0.
- `p >= 0,05`: o resultado e compativel com H0; voce **nao tem evidencia suficiente** para rejeita-la (isso nao significa que H0 e verdadeira, apenas que esses dados nao a derrubam).

Quatro cuidados que separam quem entende `p` de quem decora:

1. `p` nao e a probabilidade de a hipotese nula ser verdadeira.
2. `p` pequeno nao significa "diferenca grande". Ele significa "diferenca dificil de explicar por acaso". Com `n` enorme, diferencas minusculas viram `p` minusculo.
3. `p` maior que 0,05 nao prova que nao existe diferenca. Pode faltar amostra.
4. Sempre reporte, junto com `p`, o tamanho do efeito (diferenca de medias, razao, percentual). E o tamanho do efeito que move uma decisao de RH.

## 13. Suposicoes dos testes: o que precisa ser verdade para o teste funcionar

Testes estatisticos sao "ferramentas calibradas". Cada teste assume coisas sobre os dados e, se essas suposicoes forem muito violadas, o resultado pode enganar. As tres suposicoes mais comuns:

- **Independencia das observacoes:** uma observacao nao deve depender da outra. Se voce mede a mesma pessoa varias vezes, nao pode tratar como se fossem pessoas diferentes.
- **Normalidade:** os dados (ou as medias amostrais) seguem aproximadamente uma distribuicao normal. Cada teste exige isso em graus diferentes.
- **Homogeneidade de variancias (homoscedasticidade):** quando voce compara grupos, espera-se que a dispersao dentro de cada grupo seja parecida. O teste de **Levene** verifica isso.

Quando essas suposicoes valem, usamos **testes parametricos** (porque eles "confiam" em parametros como media e desvio). Quando nao valem, usamos **testes nao parametricos**, que trabalham com postos e nao exigem normalidade.

## 14. Parametrico ou nao parametrico, em uma frase

- **Parametrico:** confia que os dados seguem uma forma conhecida (quase sempre a normal). Usa media e desvio padrao. E mais poderoso quando as suposicoes valem.
- **Nao parametrico:** nao exige formato. Usa postos (a posicao do valor depois de ordenar tudo). E mais robusto contra outliers e distribuicoes torcidas, mas tem menos poder estatistico quando a normalidade vale.

Equivalencias mais comuns:

| Pergunta | Parametrico | Nao parametrico |
|---|---|---|
| Comparar a media de dois grupos independentes | Teste t independente (Welch) | Mann-Whitney U |
| Comparar dois grupos pareados | Teste t pareado | Wilcoxon dos sinais |
| Comparar tres ou mais grupos | ANOVA | Kruskal-Wallis |
| Associacao entre duas variaveis numericas | Correlacao de Pearson | Correlacao de Spearman |
| Associacao entre duas variaveis categoricas | Qui-quadrado (padrao) | Teste exato de Fisher (tabelas pequenas) |

## 15. Testes mais usados no curso, explicados sem jargao

**Teste t (de Welch):** compara a media de dois grupos independentes. Pergunta: "essa diferenca de medias e maior que o que seria esperado por acaso?". Use quando os dados em cada grupo sao aproximadamente simetricos.

**ANOVA (analise de variancia):** generaliza o teste t para tres ou mais grupos. Resposta apenas "existe ao menos um grupo diferente?". Para saber quais, faca um teste **post-hoc** como Tukey HSD.

**Mann-Whitney U:** versao nao parametrica do teste t para dois grupos. Compara as distribuicoes inteiras usando postos.

**Kruskal-Wallis:** versao nao parametrica da ANOVA. Mesma logica, para tres ou mais grupos.

**Qui-quadrado de independencia:** compara duas variaveis categoricas. Pergunta: "a distribuicao de uma muda dependendo da outra?". Exemplo: `area` x `tipo_contrato`.

**Correlacao (Pearson ou Spearman):** mede o quanto duas variaveis numericas andam juntas. Pearson exige linearidade; Spearman so exige que cresca ou caia junto.

**Testes de normalidade (Shapiro-Wilk e D'Agostino-Pearson):** avaliam se uma distribuicao pode ser tratada como normal. Voce nao usa esses testes para decidir hipoteses de negocio; voce os usa como **diagnostico** antes de escolher entre parametrico e nao parametrico.

## 16. Etica em estatistica de RH

Analises de genero, raca, idade, salario, desempenho, ponto e desligamento precisam de cuidado especial. Numeros parecem neutros, mas carregam escolhas humanas (como o dado foi coletado, quem ficou de fora, qual definicao foi usada).

Boas praticas:

- Agregar resultados quando possivel. Evite tabelas com poucos individuos identificaveis.
- Nao expor pessoas desnecessariamente. Use IDs e relate por grupo.
- Usar dados sensiveis para medir desigualdades e barreiras, nao para reforca-las.
- Documentar limitacoes. Toda analise tem buracos; melhor explicita-los.
- Separar achado estatistico de decisao administrativa. Estatistica informa; ela nao decide.

## 17. Pratica guiada: do histograma ao teste

Ate aqui cada conceito apareceu isolado. Esta secao costura tudo: tipo de variavel, distribuicao, suposicoes, escolha do teste e interpretacao. Para isso usamos duas planilhas geradas especificamente para a aula, com 1.200 observacoes sinteticas por coluna e distribuicoes propositalmente diferentes.

Arquivos:

- `dados/distribuicoes_exercicio.xlsx`: versao em branco. Voce preenche estatisticas, histogramas, testes e interpretacoes.
- `dados/distribuicoes_resolvido.xlsx`: gabarito. Mesma base, mas com abas ja calculadas e comentadas.

Para regenerar as duas planilhas a qualquer momento:

```bash
python scripts/gerar_planilhas_distribuicoes.py
```

### 17.1 O que cada coluna esta tentando ensinar

A aba `Dicionario` resume, mas vale dizer aqui o porque de cada escolha:

- `salario_mensal`: **lognormal**. Cauda longa a direita. Tipica de salarios: maioria concentrada em baixo, poucos puxando para cima.
- `idade`: normal truncada (entre 18 e 65). E o sino "bem comportado" que a regra 68-95-99 descreve.
- `tempo_empresa_meses`: **exponencial**. Muita gente com pouco tempo de casa, poucos com muito tempo. Tipico de empresa em crescimento.
- `horas_treinamento_ano`: **gamma**. Assimetria moderada a direita. Usada para mostrar uma distribuicao "quase normal, mas nao bem".
- `nota_avaliacao` (1 a 5): quase normal, mas limitada. Lembra que escala restrita nao impede teste parametrico se o formato for simetrico.
- `dias_absenteismo_ano`: **Poisson** (contagem). Inteiros pequenos, muitos zeros, cauda assimetrica.
- `score_engajamento`: normal. Bom candidato para testes parametricos.
- `horas_extras_mes`: **bimodal**. Dois grupos misturados (quem faz pouca e quem faz muita hora extra). Mostra distribuicao em que nem media nem mediana descrevem bem.

### 17.2 Roteiro pratico, uma coluna numerica de cada vez

1. **Olhe a forma antes do numero.** Va para a aba `Histogramas` e desenhe um histograma. Sino simetrico? Cauda longa? Dois picos? Muitos zeros? A primeira hipotese sobre normalidade nasce aqui.
2. **Compare media e mediana.** Na aba `Estatisticas`, se a media for muito maior que a mediana, ha cauda a direita. Se for menor, cauda a esquerda. Se baterem, a distribuicao e simetrica.
3. **Confirme com teste de normalidade.** Na aba `Normalidade`, rode Shapiro-Wilk (ate cerca de 5.000 observacoes) e D'Agostino-Pearson. Lembre: com `n` grande, qualquer desvio minusculo rejeita a normal. O teste e diagnostico, nao sentenca.
4. **Decida o tipo de teste.** Va para a aba `Decisao` e siga a arvore. Variavel numerica simetrica e variancias parecidas? Pode parametrico. Forma torcida, outliers, bimodal ou contagem? Use nao parametrico ou transforme os dados (por exemplo, aplique logaritmo no salario para "endireitar" a cauda).
5. **Rode o teste e escreva a interpretacao em portugues claro.** Sempre relate quatro coisas: o que foi comparado, o tamanho do efeito (diferenca de medias ou medianas em unidades reais), o `p` e a recomendacao para o negocio.

### 17.3 Armadilhas mais comuns

- **Confundir significancia com importancia.** Com 1.200 observacoes, diferencas minusculas saem com `p < 0,05`. Pergunte sempre: essa diferenca muda alguma decisao?
- **Aplicar teste t em distribuicao bimodal.** A media nao representa o grupo. Olhe `horas_extras_mes` para sentir o problema.
- **Ignorar variancias diferentes.** Para o teste t, prefira a versao de Welch (nao assume variancias iguais). Confirme com Levene.
- **Trocar Pearson por Spearman sem motivo.** Se a relacao e claramente linear e os dados sao simetricos, Pearson e mais informativo. Quando os dois resultados divergem, suspeite de nao linearidade ou outliers.
- **Esquecer o tipo da variavel.** Calcular media de uma variavel categorica codificada como numero (ex: `genero` salvo como 0 e 1) gera um numero que nao significa nada util.

## Perguntas e respostas

**Media alta significa que todo mundo esta bem?**

Nao. A media pode esconder desigualdades. Sempre olhe dispersao, mediana e distribuicao por grupo.

**Quando devo usar mediana em vez de media?**

Use mediana quando houver valores extremos (outliers) ou distribuicao muito assimetrica, como salarios, custos e tempos longos de contratacao. Em duvida, calcule as duas e compare.

**O que e "distribuicao normal", em uma frase?**

E aquela curva em formato de sino em que a maioria dos valores fica perto da media e os extremos sao raros, com lados esquerdo e direito iguais.

**Por que o teste de Shapiro-Wilk fica "irritado" com amostras grandes?**

Porque ele detecta qualquer desvio da normal, por menor que seja. Com 1.200 ou mais observacoes, ate uma assimetria muito leve produz `p < 0,05`. Por isso o teste deve ser usado junto com o histograma e a comparacao media x mediana, nao sozinho.

**O que e um outlier e o que eu faco com ele?**

E um valor muito distante dos demais. Antes de remover, investigue: pode ser erro de digitacao (corrija), caso real raro (mantenha e reporte separado) ou sub-populacao misturada (separe os grupos).

**Um `p-valor` maior que 0,05 prova que nao existe diferenca?**

Nao. Ele indica que, com aqueles dados, nao ha evidencia estatistica suficiente. Pode faltar amostra, qualidade de dado ou uma medida melhor.

**Se duas variaveis tem correlacao alta, posso agir direto?**

Nao sem contexto. Correlacao ajuda a priorizar investigacao, nao substitui ela. Para agir, combine dado, conhecimento do processo e escuta qualitativa.

**Como decido entre um teste parametrico e um nao parametrico?**

Combine tres sinais: forma do histograma, comparacao entre media e mediana e resultado do teste de normalidade. Se a distribuicao parece um sino e nao ha outliers extremos, parametrico costuma servir. Se ha assimetria forte, bimodalidade, contagens com muitos zeros ou outliers que mexem a media, prefira o nao parametrico. Em duvida, rode os dois e veja se a conclusao muda.

**Qual a diferenca pratica entre Pearson e Spearman?**

Pearson mede o quanto a relacao e linear; e sensivel a outliers. Spearman usa postos: capta relacoes que crescem ou decrescem juntas, mesmo nao lineares, e e robusto. Quando os dois batem, a relacao e bem comportada. Quando divergem, suspeite de nao linearidade ou outliers.

**Dados sensiveis devem ser removidos da analise?**

Depende da pergunta e da governanca. Para medir equidade e representatividade, esses dados podem ser necessarios. O ponto e usa-los com finalidade clara, protecao e responsabilidade.

## Exercicios

### Fixacao

1. Classifique cada uma destas variaveis como numerica continua, numerica discreta, categorica nominal ou categorica ordinal: `salario_mensal`, `area`, `senioridade`, `dias_de_falta`, `tipo_contrato`, `nota_avaliacao`.
2. Explique, com um exemplo de salarios, a diferenca entre media e mediana e por que a mediana e mais robusta contra outliers.
3. Em uma frase, descreva o que e uma distribuicao normal e cite a regra 68-95-99.
4. Crie um exemplo em que uma contagem engana e uma taxa ajuda.
5. Escreva uma hipotese nula (H0) e uma hipotese alternativa (H1) para a pergunta "o treinamento presencial gera nota de eficacia maior que o online?".
6. Explique, em portugues claro, o que e o `p-valor` e o que ele NAO e.
7. Em uma frase, diga o que diferencia um teste parametrico de um teste nao parametrico.
8. Para cada situacao, marque P (parametrico) ou N (nao parametrico) e justifique:
   a) Comparar salario medio entre dois departamentos com `n=2.500` e cauda longa.
   b) Comparar nota de eficacia (1 a 5, quase simetrica) entre duas turmas de `n=120`.
   c) Comparar dias de absenteismo (contagem com muitos zeros) entre tres areas.
   d) Verificar se area e tipo de contrato estao associados.
9. Explique por que correlacao nao prova causalidade, usando o exemplo `horas_treinamento` x `performance`.

### Aplicacao

1. Em `dados/colaboradores.csv`, compare salario medio e mediano por `nivel`. Para cada nivel, escreva uma frase dizendo se a distribuicao parece simetrica ou assimetrica e por que.
2. Em `dados/indicadores_mensais.csv`, calcule o turnover mensal e identifique o mes mais alto. Cuidado: turnover de 1 mes isolado pode ser ruido. Veja a tendencia.
3. Em `dados/treinamentos.csv`, compare a taxa de conclusao por `modalidade`. Calcule a proporcao e tambem o tamanho de cada grupo (n).
4. Em `dados/ponto_horas.csv`, observe se horas extras indevidas parecem concentradas em algum mes ou area. Use medianas alem de medias, ja que contagens costumam ter caudas longas.

### Pratica guiada com planilhas

Use `dados/distribuicoes_exercicio.xlsx` para responder. Confira depois com `dados/distribuicoes_resolvido.xlsx`.

1. Na aba `Estatisticas`, preencha media, mediana, desvio, quartis, assimetria e curtose das oito colunas numericas. Para quais colunas a media e a mediana ficaram bem distantes? Por que isso aconteceu?
2. Na aba `Histogramas`, plote o histograma de `salario_mensal`, `idade`, `tempo_empresa_meses` e `horas_extras_mes`. Para cada um, escreva uma linha descrevendo a forma (simetrico, cauda longa, bimodal, etc.).
3. Na aba `Normalidade`, anote o `p` de Shapiro-Wilk e D'Agostino para cada coluna numerica. Considerando que `n = 1.200`, em quais variaveis voce confia que a forma e proxima da normal mesmo se o teste rejeitar?
4. Na aba `Decisao`, escolha o teste indicado para cada uma destas perguntas e justifique em uma frase:
   a) `score_engajamento` difere entre genero F e M?
   b) `salario_mensal` difere entre genero F e M?
   c) `dias_absenteismo_ano` difere entre as quatro areas?
   d) Existe associacao entre `area` e `tipo_contrato`?
   e) Existe relacao entre `horas_treinamento_ano` e `nota_avaliacao`?
5. Rode os testes escolhidos em Python (use `scipy.stats`) e escreva, para cada um, uma interpretacao de duas linhas: o que foi observado e o que voce recomendaria ao time de RH.

### Desafio

Escolha uma hipotese de RH e escreva uma mini analise com: pergunta, variaveis, indicador, possivel teste estatistico, interpretacao esperada e cuidado etico.

### Desafio extra (planilha resolvida como gabarito)

Escolha uma das colunas numericas de `dados/distribuicoes_exercicio.xlsx` e produza um mini relatorio de uma pagina contendo:

- Pergunta de negocio relacionada a essa variavel.
- Histograma comentado (forma, simetria, picos).
- Diagnostico de normalidade combinando histograma, comparacao media x mediana e teste de Shapiro-Wilk.
- Justificativa explicita para escolher teste parametrico ou nao parametrico.
- Teste rodado, `p`-valor, tamanho do efeito e interpretacao em portugues claro.
- Riscos eticos e limitacoes da analise.

Use a aba correspondente em `dados/distribuicoes_resolvido.xlsx` apenas para conferir o resultado depois de escrever sua propria versao.

## Fechamento

Estatistica nao serve para dar uma aura de certeza a uma decisao. Ela serve para tornar a incerteza visivel. Em RH, essa humildade e uma virtude: protege pessoas, melhora processos e evita conclusoes apressadas.

Guarde tres lembretes que voltam em quase toda analise:

1. **Olhe a forma antes do numero.** Um histograma evita escolher o teste errado.
2. **Reporte tamanho do efeito junto com `p`.** `p` mostra raridade; tamanho do efeito mostra relevancia.
3. **Hipotese nasce de pergunta de negocio, nao de teste estatistico.** Se voce nao consegue ligar o resultado a uma decisao, talvez a pergunta esteja mal formulada.
