# Aula 3: Python para quem vem do Excel

## Objetivo da aula

Entender Python como uma ferramenta para trabalhar com tabelas de forma repetivel, auditavel e escalavel. A pessoa estudante nao precisa abandonar o raciocinio de Excel; ela vai traduzir esse raciocinio para pandas.

Ao final, a pessoa deve saber ler um CSV, visualizar as primeiras linhas, filtrar dados, criar colunas, agrupar informacoes e interpretar pequenos resultados.

## 1. Por que aprender Python depois do Excel

Excel e excelente para explorar dados pequenos, criar tabelas dinamicas e fazer analises visuais rapidas. Mas algumas tarefas ficam dificeis quando a rotina cresce:

- Repetir a mesma limpeza todo mes.
- Cruzar varias bases com regras consistentes.
- Registrar exatamente como um indicador foi calculado.
- Evitar alteracoes manuais invisiveis.
- Trabalhar com bases maiores.
- Criar analises que outras pessoas possam reproduzir.

Python ajuda nesses pontos porque transforma a analise em instrucoes. Em vez de clicar varias vezes, escrevemos uma receita. Se a receita estiver correta, ela pode ser executada de novo com dados atualizados.

## 2. O que e pandas

Pandas e uma biblioteca Python para trabalhar com dados tabulares. Sua estrutura principal e o `DataFrame`, que pode ser entendido como uma tabela com linhas e colunas.

Quando escrevemos:

```python
import pandas as pd
vagas = pd.read_csv("dados/vagas_recrutamento.csv")
```

Estamos dizendo:

1. Carregue a biblioteca pandas.
2. Leia o arquivo CSV.
3. Guarde a tabela dentro de uma variavel chamada `vagas`.

Uma variavel e como um nome dado a um objeto. Nesse caso, `vagas` passa a representar a tabela de recrutamento.

## 3. Tradução Excel para pandas

| Acao no Excel | Acao em pandas |
|---|---|
| Abrir CSV | `pd.read_csv()` |
| Ver primeiras linhas | `.head()` |
| Ver filtros | `dados[dados["area"] == "RH"]` |
| Criar coluna | `dados["nova"] = ...` |
| Tabela dinamica | `.groupby().agg()` |
| Contar linhas | `.count()` ou `.size()` |
| Media | `.mean()` |
| Ordenar | `.sort_values()` |
| Grafico simples | `.plot()` |

A diferenca principal e que em pandas precisamos ser explicitos. Isso pode parecer mais dificil no comeco, mas torna a analise mais clara e repetivel.

## 4. Lendo uma tabela

Exemplo:

```python
from pathlib import Path
import pandas as pd

DADOS = Path("dados")
vagas = pd.read_csv(DADOS / "vagas_recrutamento.csv")
vagas.head()
```

`head()` mostra as primeiras linhas. Essa e uma boa pratica antes de qualquer analise. Ela responde: o arquivo abriu? As colunas vieram certas? Os valores parecem coerentes?

Depois, usamos:

```python
vagas.shape
vagas.dtypes
vagas.info()
```

`shape` mostra quantidade de linhas e colunas. `dtypes` mostra tipos de dados. `info()` mostra uma visao geral com valores nao nulos.

## 5. Filtrando linhas

No Excel, filtramos pela setinha da coluna. Em pandas, criamos uma condicao.

```python
vagas_rh = vagas[vagas["area"] == "RH"]
```

Leia como: dentro da tabela `vagas`, traga apenas as linhas em que a coluna `area` e igual a `RH`.

Filtros podem combinar condicoes:

```python
vagas_rh_linkedin = vagas[(vagas["area"] == "RH") & (vagas["source_of_hire"] == "LinkedIn")]
```

O `&` significa "e". Cada condicao fica entre parenteses.

## 6. Criando colunas

Criar coluna em pandas e parecido com criar uma formula no Excel, mas a formula fica registrada no codigo.

```python
vagas["custo_por_contratado"] = vagas["custo_divulgacao"] / vagas["contratados"]
```

Essa linha cria um indicador para cada vaga. Se houver uma vaga com zero contratados, a formula precisaria de cuidado para evitar divisao por zero. Esse tipo de detalhe e parte da qualidade da analise.

## 7. Agrupando dados

Agrupar e o equivalente conceitual da tabela dinamica.

```python
resumo = (
    vagas
    .groupby("source_of_hire")
    .agg(
        vagas=("vaga_id", "count"),
        time_to_hire_medio=("time_to_hire_dias", "mean"),
        custo_total=("custo_divulgacao", "sum")
    )
)
```

Essa estrutura responde: para cada source of hire, quantas vagas existem, qual o time to hire medio e qual o custo total?

O ponto mais importante e interpretar o agrupamento como uma pergunta. Sem pergunta, `groupby` vira apenas comando.

## 8. Erros comuns de iniciantes

**Caminho do arquivo errado:** o notebook pode estar rodando de dentro da pasta `notebooks/`. Por isso os notebooks do curso usam logica para encontrar a pasta `dados/`.

**Nome de coluna diferente:** Python diferencia maiusculas, minusculas, acentos e espacos. `area` e diferente de `Área`.

**Numero importado como texto:** se uma coluna numerica aparece como texto, medias e somas podem falhar.

**Filtro sem parenteses:** ao combinar condicoes, use parenteses em cada uma.

**Alterar dados sem perceber:** sempre que criar uma coluna, confira algumas linhas com `.head()`.

## 9. Como estudar os notebooks

Use este metodo:

1. Rode a celula sem alterar.
2. Leia o resultado.
3. Explique em voz alta o que aconteceu.
4. Altere uma pequena parte.
5. Rode de novo.
6. Compare antes e depois.

Aprender Python nao e decorar comandos. E desenvolver a capacidade de prever o que uma linha de codigo deve fazer.

## Perguntas e respostas

**Python substitui Excel?**

Nao necessariamente. Em muitas rotinas, Excel continua sendo otimo para consumo, revisao e apresentacao. Python entra melhor quando a analise precisa ser repetivel, rastreavel ou mais complexa.

**Preciso decorar todos os comandos de pandas?**

Nao. No inicio, memorize apenas o ciclo: ler, inspecionar, filtrar, criar coluna, agrupar, visualizar e interpretar.

**Por que o codigo parece mais lento que clicar no Excel?**

No comeco, escrever codigo e mais lento. A vantagem aparece quando voce precisa repetir a analise muitas vezes ou explicar exatamente como chegou ao resultado.

**O que e uma variavel em Python?**

E um nome que aponta para um valor ou objeto. Quando escrevemos `vagas = pd.read_csv(...)`, `vagas` passa a ser o nome da tabela carregada.

**Por que usar notebook?**

Porque notebook combina texto, codigo e resultado no mesmo lugar. Isso e ideal para aprendizado e analise exploratoria.

## Exercicios

### Fixacao

1. Explique o que faz `pd.read_csv()`.
2. Explique a diferenca entre `head()`, `shape` e `dtypes`.
3. Escreva em portugues o significado do filtro `vagas[vagas["area"] == "RH"]`.
4. Explique por que `groupby` parece uma tabela dinamica.

### Aplicacao

1. Abra `notebooks/01_primeiros_passos_python.ipynb` e rode todas as celulas.
2. Altere o filtro de `RH` para `TI`.
3. Calcule a media de candidatos por area.
4. Calcule o custo medio de divulgacao por recrutador.
5. Crie uma coluna chamada `entrevistas_por_candidato`.

### Desafio

Crie uma pequena analise em Python respondendo: qual source of hire parece mais eficiente considerando tempo, custo e volume? Escreva uma conclusao com evidencia, interpretacao e limitacao.

## Fechamento

Python e uma linguagem, mas tambem e uma forma de documentar pensamento. Cada linha deve responder a uma intencao analitica. Quando voce entende a pergunta, o codigo deixa de ser um enigma e vira uma receita.
