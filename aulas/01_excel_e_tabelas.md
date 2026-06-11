# Aula 1: Excel, tabelas e perguntas de RH

## Objetivo da aula

Aprender a enxergar uma planilha como uma base de dados. Esta aula e propositalmente anterior ao Python: antes de automatizar qualquer analise, precisamos saber o que uma tabela representa, o que uma coluna mede e que tipo de pergunta ela permite responder.

Ao final, a pessoa estudante deve conseguir abrir um CSV no Excel, transformar o intervalo em tabela, criar filtros, montar tabelas dinamicas, calcular indicadores simples e escrever conclusoes com cuidado.

## 1. O que e uma tabela analitica

Uma tabela analitica e uma estrutura em que cada linha representa uma observacao e cada coluna representa uma caracteristica dessa observacao. Parece simples, mas essa definicao evita muitos erros.

Em recrutamento, uma linha pode representar uma vaga. Nesse caso, colunas como `cargo`, `area`, `source_of_hire`, `data_abertura` e `time_to_hire_dias` descrevem aquela vaga.

Em treinamento, uma linha pode representar a participacao de uma pessoa em um treinamento. Nesse caso, colunas como `colaborador_id`, `treinamento`, `horas_treinamento`, `concluiu` e `nota_eficacia` descrevem aquela participacao.

Em indicadores mensais, uma linha pode representar um mes. Nesse caso, colunas como `headcount_inicio`, `admitidos`, `demitidos` e `ausencias_dias` descrevem aquele periodo.

O erro mais comum de iniciantes e misturar unidades de analise. Por exemplo: colocar na mesma linha informacoes de uma vaga, de uma pessoa e de um mes sem deixar claro o que a linha representa. Quando a unidade de analise fica confusa, os indicadores tambem ficam confusos.

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

Passos no Excel:

1. Abra o CSV.
2. Transforme o intervalo em tabela com `Ctrl + T`.
3. Confirme se `time_to_hire_dias`, `candidatos`, `contratados` e `custo_divulgacao` estao como numeros.
4. Crie uma tabela dinamica.
5. Coloque `source_of_hire` em linhas.
6. Coloque `vaga_id` em valores como contagem.
7. Coloque `time_to_hire_dias` em valores como media.
8. Coloque `custo_divulgacao` em valores como soma.
9. Crie uma coluna calculada fora da dinamica: custo por contratado = custo total / contratados.

Como interpretar:

Uma fonte com baixo time to hire pode ser interessante, mas isso nao basta. Tambem precisamos olhar volume, custo, tipo de cargo e senioridade. Se uma fonte fechou apenas uma vaga junior, ela nao deve ser comparada diretamente com uma fonte que fechou cargos senior complexos.

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
