# Aula 1: Excel, tabelas e perguntas de RH

## Objetivo da aula

Aprender a enxergar uma planilha como uma base de dados. Esta aula e propositalmente anterior ao Python: antes de automatizar qualquer analise, precisamos saber o que uma tabela representa, o que uma coluna mede e que tipo de pergunta ela permite responder.

Ao final, a pessoa estudante deve conseguir abrir um CSV no Excel, transformar o intervalo em tabela, criar filtros, montar tabelas dinamicas, calcular indicadores simples e escrever conclusoes com cuidado.

## 1. O que e uma tabela analitica

Uma tabela analitica e uma estrutura em que **cada linha representa uma observacao** e **cada coluna representa uma caracteristica dessa observacao**. Observacao e o "sujeito da frase": pode ser uma vaga, uma pessoa, um treinamento, um registro de ponto ou um mes. Parece simples, mas essa definicao evita metade dos erros que aparecem em planilhas reais.

A palavra mais importante aqui e **unidade de analise**: o que cada linha representa. Toda a leitura dos indicadores depende disso.

Em recrutamento, uma linha pode representar **uma vaga**. As colunas (`cargo`, `area`, `source_of_hire`, `data_abertura`, `time_to_hire_dias`) descrevem aquela vaga especifica.

Em treinamento, uma linha pode representar **uma participacao de uma pessoa em um treinamento**. As colunas (`colaborador_id`, `treinamento`, `horas_treinamento`, `concluiu`, `nota_eficacia`) descrevem aquela participacao. Atencao: a mesma pessoa pode aparecer em varias linhas se fez varios treinamentos.

Em indicadores mensais, uma linha pode representar **um mes**. As colunas (`headcount_inicio`, `admitidos`, `demitidos`, `ausencias_dias`) descrevem aquele periodo.

O erro mais comum de iniciantes e misturar unidades de analise: colocar na mesma linha informacoes de uma vaga, de uma pessoa e de um mes sem deixar claro o que a linha representa. Quando a unidade de analise fica confusa, os indicadores tambem ficam. Antes de qualquer calculo, faca a pergunta: **"o que cada linha desta tabela representa?"**. Se voce nao souber responder em uma frase, pare e investigue.

## 2. Vocabulario essencial

**Linha:** uma observacao. Pode ser uma vaga, uma pessoa, um treinamento, um registro de ponto ou um mes.

**Coluna:** uma variavel. Pode ser texto, numero, data, categoria ou indicador.

**Chave:** coluna que identifica uma linha ou conecta tabelas. Exemplos: `vaga_id`, `colaborador_id`, `registro_id`.

**Categoria:** valor usado para agrupar. Exemplos: area, genero, raca, source of hire, modalidade.

**Medida:** valor numerico que pode ser somado, contado ou resumido. Exemplos: salario, horas extras, custo, dias.

**Indicador:** calculo criado para acompanhar um fenomeno. Exemplos: turnover, taxa de conclusao, absenteismo, custo por contratado.

## 3. Qualidade de dados antes de indicador

Antes de calcular, pergunte:

- Existem linhas duplicadas?
- Alguma coluna essencial esta vazia?
- As categorias foram escritas de forma consistente?
- Datas estao no formato correto?
- Numeros foram importados como numeros ou como texto?
- O periodo da analise esta claro?

Exemplo: se `LinkedIn`, `linkedin` e `Linkedin` aparecem como tres fontes diferentes, uma tabela dinamica pode separar indevidamente a mesma fonte em tres linhas. O problema nao e a tabela dinamica; e a padronizacao do dado.

## 4. Primeira pratica: source of hire e time to hire

Arquivo: `dados/vagas_recrutamento.csv`

Pergunta de negocio: quais fontes de contratacao parecem mais rapidas e quais parecem mais caras?

**Antes dos passos, dois termos novos:**

- **Tabela do Excel** (`Ctrl + T`): converte um intervalo de celulas em um objeto "tabela" com cabecalho, filtros automaticos e expansao quando voce adiciona linhas. Diferente de simplesmente formatar.
- **Tabela dinamica** (`Pivot Table`, em ingles): uma ferramenta do Excel que permite arrastar campos para Linhas, Colunas e Valores para gerar resumos automaticamente. E o equivalente visual do `groupby` que voce vai ver em pandas mais tarde.

Passos no Excel:

1. Abra o CSV (Arquivo > Abrir > selecione o arquivo).
2. Selecione qualquer celula com dados e aperte `Ctrl + T`. Marque "Minha tabela tem cabecalhos".
3. Confirme se `time_to_hire_dias`, `candidatos`, `contratados` e `custo_divulgacao` estao alinhados a direita (sinal de numero) e nao a esquerda (sinal de texto).
4. Em `Inserir > Tabela Dinamica`, crie uma tabela dinamica em uma nova aba.
5. Arraste `source_of_hire` para `Linhas`.
6. Arraste `vaga_id` para `Valores` e mude o resumo para `Contagem`.
7. Arraste `time_to_hire_dias` para `Valores` e mude para `Media`.
8. Arraste `custo_divulgacao` para `Valores` e mantenha `Soma`.
9. Fora da dinamica, crie uma coluna chamada `custo_por_contratado` = custo total / contratados.

Como interpretar:

Uma fonte com baixo time to hire pode parecer atrativa, mas isso nao basta. Tambem precisamos olhar volume (quantas vagas), custo, tipo de cargo e senioridade. Se uma fonte fechou apenas uma vaga junior, ela nao deve ser comparada diretamente com uma fonte que fechou varios cargos senior complexos. Em RH, comparar grupos diferentes como se fossem iguais e a raiz de muitas conclusoes erradas.

## 5. Segunda pratica: treinamentos

Arquivo: `dados/treinamentos.csv`

Pergunta de negocio: os treinamentos estao sendo concluidos e percebidos como eficazes?

Indicadores:

- Taxa de conclusao = pessoas que concluiram / total de participacoes.
- Horas medias = soma de horas / total de participacoes.
- Nota media de eficacia = media das notas respondidas.
- Custo de coffee = soma de `custo_coffee`.

Cuidados:

Se uma pessoa nao respondeu a avaliacao, a nota fica ausente. Nao trate ausencia de resposta como nota zero automaticamente. Zero significa avaliacao pessima; vazio significa informacao nao coletada.

## 6. Terceira pratica: indicadores mensais

Arquivo: `dados/indicadores_mensais.csv`

Pergunta de negocio: como evoluem turnover, absenteismo, retencao por diversidade e corte de gastos?

Formulas:

```text
headcount_medio = (headcount_inicio + headcount_fim) / 2
turnover = demitidos / headcount_medio
taxa_absenteismo = ausencias_dias / (headcount_fim * dias_trabalho)
retencao_diversidade = 1 - (desligamentos_diversidade / headcount_diversidade)
```

Por que usar headcount medio no turnover? Porque o tamanho da empresa pode mudar ao longo do mes. Usar apenas o inicio ou o fim pode distorcer o indicador quando ha muitas admissoes ou demissoes.

## 7. Como escrever conclusoes

Uma boa conclusao tem tres partes.

**Evidencia:** o que foi observado no dado.

**Interpretacao:** o que isso pode significar no contexto de RH.

**Cautela:** o que ainda nao sabemos.

Exemplo:

> No dataset didatico, a fonte LinkedIn apresenta time to hire medio mais alto que Indicacao. Isso pode indicar maior complexidade das vagas divulgadas nessa fonte, maior concorrencia ou processo seletivo mais longo. Antes de concluir que a fonte e pior, seria necessario comparar por cargo, senioridade e area.

## Perguntas e respostas

**Uma tabela dinamica ja e ciencia de dados?**

Ela pode ser parte de uma analise de dados. Ciencia de dados nao e definida pela ferramenta, mas pelo processo: pergunta, dado, metodo, interpretacao e decisao.

**Por que nao posso comparar qualquer media diretamente?**

Porque grupos podem ser diferentes. Comparar time to hire de vagas junior com vagas senior pode gerar uma conclusao injusta. Sempre pergunte se os grupos sao comparaveis.

**Quando uso contagem e quando uso taxa?**

Use contagem para volume absoluto. Use taxa quando quiser comparar grupos de tamanhos diferentes. Por exemplo: 10 desligamentos em 100 pessoas e diferente de 10 desligamentos em 1.000 pessoas.

**O que fazer quando ha dados faltantes?**

Primeiro entenda o motivo. Pode ser erro de preenchimento, informacao nao aplicavel ou dado ainda nao coletado. A decisao de remover, preencher ou manter vazio depende do contexto.

**Por que criar uma tabela antes da tabela dinamica?**

Porque a tabela do Excel preserva cabecalhos, filtros e expansao automatica. Isso reduz erros quando novas linhas sao adicionadas.

## Exercicios

### Fixacao

1. Abra `dados/vagas_recrutamento.csv` e identifique a unidade de analise.
2. Liste tres colunas categoricas e tres colunas numericas.
3. Explique a diferenca entre `candidatos`, `entrevistas`, `ofertas` e `contratados`.

### Aplicacao

1. Crie uma tabela dinamica com time to hire medio por `area`.
2. Crie uma tabela dinamica com custo total de divulgacao por `source_of_hire`.
3. Em `dados/treinamentos.csv`, calcule taxa de conclusao por `modalidade`.
4. Em `dados/indicadores_mensais.csv`, calcule turnover e taxa de absenteismo.

### Desafio

Monte uma pequena analise de uma pagina no Excel respondendo: qual tema parece mais critico para o RH agir primeiro, recrutamento, treinamento ou indicadores mensais? Use pelo menos dois indicadores e uma limitacao.

## Fechamento

O objetivo desta aula nao e virar especialista em Excel. E construir a base mental da ciencia de dados: saber o que uma linha representa, o que uma coluna mede, como um indicador e calculado e como uma conclusao pode ser util sem prometer mais do que os dados permitem.
