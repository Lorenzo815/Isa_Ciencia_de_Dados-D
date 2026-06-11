"""Gera notebooks didaticos do curso de Ciencia de Dados para RH.

Os notebooks sao escritos como JSON estruturado para manter o formato .ipynb
consistente e incluir metadata.language e metadata.id em cada celula.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = ROOT / "notebooks"


def lines(text: str) -> list[str]:
    return text.strip("\n").splitlines()


def make_cell(kind: str, text: str, cell_id: str) -> dict:
    language = "python" if kind == "code" else "markdown"
    cell = {
        "cell_type": "code" if kind == "code" else "markdown",
        "id": cell_id,
        "metadata": {"id": cell_id, "language": language},
        "source": lines(text),
    }
    if kind == "code":
        cell["execution_count"] = None
        cell["outputs"] = []
    return cell


def md(text: str, cell_id: str) -> dict:
    return make_cell("markdown", text, cell_id)


def code(text: str, cell_id: str) -> dict:
    return make_cell("code", text, cell_id)


def notebook(cells: list[dict]) -> dict:
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "pygments_lexer": "ipython3"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def write_notebook(name: str, cells: list[dict]) -> None:
    path = NOTEBOOKS / name
    path.write_text(json.dumps(notebook(cells), ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Gerado: {path.relative_to(ROOT)} ({len(cells)} celulas)")


nb00 = [
    md("""
# 00 - Fundamentos de Python para quem nunca programou

Este notebook existe para reduzir a ansiedade antes dos notebooks de dados. Aqui vamos aprender o minimo de Python necessario para entender as proximas aulas.

A regra deste notebook e: nada e obvio. Cada celula explica uma ideia pequena, mostra um exemplo e deixa um exercicio curto.
""", "nb00-001"),
    md("""
## 1. O que e programar

Programar e escrever instrucoes para o computador executar. O computador nao entende intencao; ele executa exatamente o que foi escrito.

Em ciencia de dados, usamos codigo para registrar uma receita de analise: abrir dados, limpar dados, calcular indicadores, criar graficos e interpretar resultados.
""", "nb00-002"),
    code("""
# Esta e uma celula de codigo.
# O simbolo # cria um comentario.
# Comentarios sao lidos por pessoas, mas ignorados pelo Python.

# print() mostra uma mensagem na tela.
# O texto precisa ficar entre aspas.
print("Ola! Esta e minha primeira linha em Python.")
""", "nb00-003"),
    md("""
## 2. Variaveis

Uma variavel e um nome que guarda um valor. Pense em uma variavel como uma etiqueta.

No exemplo abaixo, criamos tres etiquetas: `area`, `vagas_abertas` e `time_to_hire_medio`.
""", "nb00-004"),
    code("""
# area guarda um texto.
area = "Recursos Humanos"

# vagas_abertas guarda um numero inteiro.
vagas_abertas = 12

# time_to_hire_medio guarda um numero decimal.
time_to_hire_medio = 34.5

# Agora mostramos os valores guardados.
print(area)
print(vagas_abertas)
print(time_to_hire_medio)
""", "nb00-005"),
    md("""
## 3. Tipos de dados

Python trata tipos diferentes de forma diferente. Texto, numero inteiro, numero decimal e verdadeiro/falso nao sao a mesma coisa.

A funcao `type()` mostra o tipo de um valor.
""", "nb00-006"),
    code("""
# Texto em Python se chama string, ou str.
nome = "Aline"

# Numero inteiro se chama int.
idade = 31

# Numero decimal se chama float.
salario = 5200.50

# Verdadeiro ou falso se chama bool.
concluiu_treinamento = True

# type() mostra o tipo de cada variavel.
print(type(nome))
print(type(idade))
print(type(salario))
print(type(concluiu_treinamento))
""", "nb00-007"),
    md("""
## 4. Operacoes matematicas

Python pode fazer contas como uma calculadora. Isso sera util para criar indicadores de RH.
""", "nb00-008"),
    code("""
# Vamos calcular uma taxa de conclusao de treinamento.
# Numerador: quantidade de pessoas que concluiram.
concluidos = 24

# Denominador: quantidade total de inscricoes.
total_inscritos = 30

# A taxa e uma divisao.
taxa_conclusao = concluidos / total_inscritos

# Multiplicamos por 100 para mostrar em percentual.
print(taxa_conclusao)
print(taxa_conclusao * 100)
""", "nb00-009"),
    md("""
## 5. Textos e f-strings

Uma f-string permite misturar texto com valores de variaveis. Ela comeca com a letra `f` antes das aspas.
""", "nb00-010"),
    code("""
# Criamos uma mensagem usando valores calculados.
mensagem = f"A taxa de conclusao foi de {taxa_conclusao * 100:.1f}%."

# :.1f significa: mostrar o numero com 1 casa decimal.
print(mensagem)
""", "nb00-011"),
    md("""
## 6. Listas

Uma lista guarda varios valores em ordem. Em RH, uma lista pode representar areas, cargos, fontes de contratacao ou notas.
""", "nb00-012"),
    code("""
# Uma lista usa colchetes.
areas = ["RH", "TI", "Financeiro", "Operacoes"]

# len() conta quantos itens existem na lista.
print(len(areas))

# Python comeca a contar posicoes em zero.
# Por isso, areas[0] traz o primeiro item.
print(areas[0])
print(areas[1])
""", "nb00-013"),
    md("""
## 7. Dicionarios

Um dicionario guarda pares de chave e valor. Ele e util quando queremos representar uma linha de informacao.
""", "nb00-014"),
    code("""
# Este dicionario representa uma vaga.
vaga = {
    "cargo": "Analista de RH",
    "area": "RH",
    "source_of_hire": "LinkedIn",
    "time_to_hire_dias": 33,
}

# Para acessar um valor, usamos a chave entre colchetes.
print(vaga["cargo"])
print(vaga["time_to_hire_dias"])
""", "nb00-015"),
    md("""
## 8. Condicoes

Condicoes permitem que o codigo tome caminhos diferentes. A palavra `if` significa "se".
""", "nb00-016"),
    code("""
# Vamos classificar uma vaga como rapida ou lenta.
time_to_hire = 45

# Se o tempo for maior que 40 dias, chamamos de lento.
if time_to_hire > 40:
    print("Processo seletivo lento")
else:
    print("Processo seletivo dentro do esperado")
""", "nb00-017"),
    md("""
## 9. Repeticao com for

Um `for` repete uma acao para cada item de uma lista. Isso e muito comum quando analisamos varias areas ou varios arquivos.
""", "nb00-018"),
    code("""
# Vamos imprimir uma frase para cada area.
for area in areas:
    # Esta linha esta indentada, ou seja, pertence ao for.
    print(f"Analisar indicadores da area: {area}")
""", "nb00-019"),
    md("""
## 10. Funcoes

Funcao e um bloco de codigo reutilizavel. Criamos uma funcao quando uma regra pode ser usada varias vezes.
""", "nb00-020"),
    code("""
# Esta funcao recebe concluidos e total.
# Depois devolve a taxa de conclusao.
def calcular_taxa_conclusao(concluidos, total):
    taxa = concluidos / total
    return taxa

# Usamos a funcao com valores diferentes.
taxa_turma_a = calcular_taxa_conclusao(24, 30)
taxa_turma_b = calcular_taxa_conclusao(18, 20)

print(f"Turma A: {taxa_turma_a:.1%}")
print(f"Turma B: {taxa_turma_b:.1%}")
""", "nb00-021"),
    md("""
## 11. Importar bibliotecas

Bibliotecas sao conjuntos de ferramentas prontas. No curso, usaremos muito `pandas` para tabelas.
""", "nb00-022"),
    code("""
# import carrega uma biblioteca.
# as pd cria um apelido curto para escrever menos.
import pandas as pd

# Criamos uma pequena tabela manualmente para ver o pandas funcionando.
dados = pd.DataFrame([
    {"area": "RH", "vagas": 5},
    {"area": "TI", "vagas": 8},
    {"area": "Financeiro", "vagas": 3},
])

# Ao colocar o nome da tabela no fim da celula, o notebook mostra a tabela.
dados
""", "nb00-023"),
    md("""
## 12. Exercicios

1. Crie uma variavel chamada `cargo` com um texto.
2. Crie uma variavel chamada `salario_mensal` com um numero.
3. Calcule `salario_anual` multiplicando o salario mensal por 12.
4. Crie uma f-string dizendo: `O salario anual estimado e ...`.
5. Crie uma lista com tres fontes de contratacao.
6. Use um `for` para imprimir cada fonte.
7. Crie uma funcao que calcule turnover: `demitidos / headcount_medio`.
""", "nb00-024"),
    code("""
# Espaco para resolver os exercicios.
# Escreva uma linha por vez e execute a celula com calma.

""", "nb00-025"),
]

nb01 = [
    md("""
# 01 - Primeiros passos com Python para RH

Neste notebook vamos sair do Python basico e entrar em tabelas reais. O objetivo e aprender a abrir um CSV, entender linhas e colunas, filtrar dados, agrupar informacoes e criar indicadores simples.

Tudo sera comentado como se fosse a primeira vez. Leia os comentarios do codigo com atencao: eles sao parte da aula.
""", "nb01-001"),
    md("""
## 1. Importar bibliotecas e localizar a pasta de dados

Antes de analisar dados, precisamos carregar ferramentas. Aqui usamos `pathlib` para lidar com caminhos de arquivos e `pandas` para trabalhar com tabelas.
""", "nb01-002"),
    code("""
# pathlib ajuda a montar caminhos de arquivo de forma mais segura.
from pathlib import Path

# pandas e a biblioteca principal para trabalhar com tabelas.
import pandas as pd

# Esta configuracao pede ao pandas para mostrar mais colunas quando exibimos tabelas.
pd.set_option("display.max_columns", 50)

# Path.cwd() mostra a pasta atual em que o notebook esta rodando.
# Se o notebook estiver rodando de dentro da pasta notebooks, subimos uma pasta.
BASE_DIR = Path.cwd().parent if Path.cwd().name == "notebooks" else Path.cwd()

# A pasta dados fica dentro da raiz do projeto.
DADOS = BASE_DIR / "dados"

# Mostramos o caminho para confirmar que o Python encontrou a pasta certa.
DADOS
""", "nb01-003"),
    md("""
## 2. Abrir uma planilha CSV

CSV e um arquivo de texto com colunas separadas por virgula. Ele funciona como uma planilha simples.

Vamos abrir a base de vagas de recrutamento. Cada linha representa uma vaga.
""", "nb01-004"),
    code("""
# pd.read_csv() le um arquivo CSV e devolve uma tabela chamada DataFrame.
# Guardamos essa tabela na variavel vagas.
vagas = pd.read_csv(DADOS / "vagas_recrutamento.csv")

# head() mostra as primeiras 5 linhas.
# Isso ajuda a conferir se o arquivo abriu corretamente.
vagas.head()
""", "nb01-005"),
    md("""
## 3. Entender tamanho, colunas e tipos

Antes de calcular qualquer indicador, fazemos uma inspecao inicial. Esta etapa evita erros simples, como tentar calcular media de uma coluna de texto.
""", "nb01-006"),
    code("""
# shape devolve uma dupla: quantidade de linhas e quantidade de colunas.
print(f"Linhas: {vagas.shape[0]}")
print(f"Colunas: {vagas.shape[1]}")

# columns mostra os nomes das colunas.
print("\nColunas da base:")
print(list(vagas.columns))

# dtypes mostra o tipo de cada coluna.
# int64 e numero inteiro; object geralmente e texto; float64 e numero decimal.
vagas.dtypes
""", "nb01-007"),
    md("""
## 4. Selecionar colunas

Selecionar colunas e como escolher quais campos queremos ver na planilha. Isso ajuda a focar a analise.
""", "nb01-008"),
    code("""
# Criamos uma lista com os nomes das colunas que queremos visualizar.
colunas_para_ver = ["vaga_id", "cargo", "area", "source_of_hire", "time_to_hire_dias"]

# Usamos a lista dentro de vagas[...] para mostrar apenas essas colunas.
vagas[colunas_para_ver].head()
""", "nb01-009"),
    md("""
## 5. Filtrar linhas

Filtro e uma das operacoes mais importantes. Em vez de olhar todas as vagas, podemos olhar apenas uma area, uma fonte ou uma senioridade.
""", "nb01-010"),
    code("""
# Esta condicao verifica, linha por linha, se a area e igual a RH.
condicao_rh = vagas["area"] == "RH"

# Quando usamos a condicao dentro de vagas[...], ficamos apenas com as linhas True.
vagas_rh = vagas[condicao_rh]

# Mostramos algumas colunas para conferir o filtro.
vagas_rh[["vaga_id", "cargo", "area", "source_of_hire", "time_to_hire_dias"]]
""", "nb01-011"),
    md("""
## 6. Criar indicadores como novas colunas

No Excel, criaríamos uma nova coluna com formula. Em pandas, fazemos o mesmo escrevendo a formula em codigo.
""", "nb01-012"),
    code("""
# Criamos uma copia para evitar alterar a tabela original sem querer.
vagas_com_indicadores = vagas.copy()

# Custo por contratado = custo de divulgacao dividido pela quantidade de contratados.
# Este indicador ajuda a comparar eficiencia de fontes de contratacao.
vagas_com_indicadores["custo_por_contratado"] = (
    vagas_com_indicadores["custo_divulgacao"] / vagas_com_indicadores["contratados"]
)

# Candidatos por entrevista mostra quantas candidaturas geram uma entrevista, em media, por vaga.
vagas_com_indicadores["candidatos_por_entrevista"] = (
    vagas_com_indicadores["candidatos"] / vagas_com_indicadores["entrevistas"]
)

vagas_com_indicadores[["vaga_id", "source_of_hire", "custo_por_contratado", "candidatos_por_entrevista"]].head()
""", "nb01-013"),
    md("""
## 7. Agrupar dados: a tabela dinamica do pandas

`groupby` agrupa linhas por uma categoria. Depois usamos `agg` para calcular contagem, media, soma ou outros resumos.
""", "nb01-014"),
    code("""
# Agrupamos por source_of_hire porque queremos comparar fontes de contratacao.
resumo_source = (
    vagas_com_indicadores
    .groupby("source_of_hire")
    .agg(
        # Contamos quantas vagas existem em cada fonte.
        vagas=("vaga_id", "count"),
        # Calculamos o time to hire medio.
        time_to_hire_medio=("time_to_hire_dias", "mean"),
        # Calculamos candidatos medios por vaga.
        candidatos_medios=("candidatos", "mean"),
        # Calculamos o custo medio de divulgacao.
        custo_medio=("custo_divulgacao", "mean"),
        # Calculamos o custo medio por contratado.
        custo_por_contratado_medio=("custo_por_contratado", "mean"),
    )
    # Arredondamos para facilitar leitura.
    .round(1)
    # Ordenamos pela menor media de time to hire.
    .sort_values("time_to_hire_medio")
)

resumo_source
""", "nb01-015"),
    md("""
## 8. Ordenar e interpretar

Ordenar ajuda a ver extremos: maior, menor, mais caro, mais rapido. Mas lembre: ordenar nao explica causa, apenas organiza evidencias.
""", "nb01-016"),
    code("""
# Selecionamos as 5 vagas com maior time to hire.
# Isso ajuda a investigar casos mais demorados.
vagas_mais_lentas = vagas_com_indicadores.sort_values("time_to_hire_dias", ascending=False).head(5)

vagas_mais_lentas[["vaga_id", "cargo", "area", "senioridade", "source_of_hire", "time_to_hire_dias"]]
""", "nb01-017"),
    md("""
## 9. Exercicios

1. Troque o filtro de `RH` para `TI`.
2. Calcule o time to hire medio por `recrutador`.
3. Descubra qual area teve mais candidatos por vaga.
4. Crie uma coluna chamada `entrevistas_por_oferta`.
5. Escreva uma conclusao com: evidencia, interpretacao e limitacao.
""", "nb01-018"),
    code("""
# Espaco para exercicios.
# Dica: copie uma celula anterior, altere uma parte pequena e execute.

""", "nb01-019"),
]

nb02 = [
    md("""
# 02 - Analise exploratoria de dados de RH

Analise exploratoria e a etapa em que conhecemos os dados antes de afirmar qualquer coisa. Vamos calcular indicadores, procurar padroes, criar graficos e praticar interpretacao.

A pergunta constante deste notebook e: o que o dado mostra, o que ele nao mostra e qual proximo passo ele sugere?
""", "nb02-001"),
    code("""
# Importamos pathlib para localizar arquivos.
from pathlib import Path

# pandas trabalha com tabelas.
import pandas as pd

# matplotlib e seaborn criam graficos.
import matplotlib.pyplot as plt
import seaborn as sns

# Definimos um estilo visual simples para os graficos.
sns.set_theme(style="whitegrid")

# Pedimos ao pandas para mostrar ate 60 colunas quando necessario.
pd.set_option("display.max_columns", 60)

# Localizamos a raiz do projeto e a pasta de dados.
BASE_DIR = Path.cwd().parent if Path.cwd().name == "notebooks" else Path.cwd()
DADOS = BASE_DIR / "dados"
""", "nb02-002"),
    md("""
## 1. Carregar bases principais

Vamos abrir quatro bases. Cada uma tem uma unidade de analise diferente: vaga, treinamento, colaborador e mes.
""", "nb02-003"),
    code("""
# Cada read_csv abre um arquivo e cria um DataFrame.
vagas = pd.read_csv(DADOS / "vagas_recrutamento.csv")
treinamentos = pd.read_csv(DADOS / "treinamentos.csv")
colaboradores = pd.read_csv(DADOS / "colaboradores.csv")
indicadores = pd.read_csv(DADOS / "indicadores_mensais.csv")

# Mostramos o tamanho de cada tabela para entender o volume de dados.
print(f"Vagas: {vagas.shape[0]} linhas e {vagas.shape[1]} colunas")
print(f"Treinamentos: {treinamentos.shape[0]} linhas e {treinamentos.shape[1]} colunas")
print(f"Colaboradores: {colaboradores.shape[0]} linhas e {colaboradores.shape[1]} colunas")
print(f"Indicadores: {indicadores.shape[0]} linhas e {indicadores.shape[1]} colunas")
""", "nb02-004"),
    md("""
## 2. Checagem simples de qualidade

Antes de calcular KPIs, verificamos dados faltantes e duplicados. Em bases reais, esta etapa costuma consumir bastante tempo.
""", "nb02-005"),
    code("""
# isna().sum() conta valores vazios por coluna.
# duplicated().sum() conta linhas duplicadas completas.
for nome, tabela in {
    "vagas": vagas,
    "treinamentos": treinamentos,
    "colaboradores": colaboradores,
    "indicadores": indicadores,
}.items():
    print(f"\nBase: {nome}")
    print(f"Linhas duplicadas: {tabela.duplicated().sum()}")
    print("Colunas com valores faltantes:")
    print(tabela.isna().sum()[tabela.isna().sum() > 0])
""", "nb02-006"),
    md("""
## 3. Recrutamento: velocidade, custo e volume

Uma fonte de contratacao nao deve ser avaliada por um unico indicador. Vamos olhar volume de vagas, contratados, time to hire e custo.
""", "nb02-007"),
    code("""
# Agrupamos por source_of_hire para comparar fontes.
kpis_recrutamento = (
    vagas.groupby("source_of_hire")
    .agg(
        vagas=("vaga_id", "count"),
        contratados=("contratados", "sum"),
        time_to_hire_medio=("time_to_hire_dias", "mean"),
        candidatos_por_vaga=("candidatos", "mean"),
        custo_total=("custo_divulgacao", "sum"),
    )
)

# Criamos um indicador derivado: custo por contratado.
kpis_recrutamento["custo_por_contratado"] = (
    kpis_recrutamento["custo_total"] / kpis_recrutamento["contratados"]
)

# Arredondamos e ordenamos para facilitar leitura.
kpis_recrutamento.round(1).sort_values("time_to_hire_medio")
""", "nb02-008"),
    code("""
# Criamos uma figura com tamanho definido.
plt.figure(figsize=(9, 4))

# barplot mostra a media de time_to_hire_dias por source_of_hire.
sns.barplot(data=vagas, x="source_of_hire", y="time_to_hire_dias", estimator="mean", errorbar=None)

# Titulo e rotulos ajudam a pessoa leitora a entender o grafico sem adivinhar.
plt.title("Time to hire medio por source of hire")
plt.xlabel("Source of hire")
plt.ylabel("Dias")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
""", "nb02-009"),
    md("""
## 4. Treinamento: conclusao, eficacia e custo

Transformaremos `Sim` e `Nao` em 1 e 0 para calcular taxa de conclusao. Isso e comum em analises de indicadores.
""", "nb02-010"),
    code("""
# map() troca valores de texto por numeros.
# Sim vira 1; Nao vira 0.
treinamentos["concluiu_bool"] = treinamentos["concluiu"].map({"Sim": 1, "Não": 0})

# Agora agrupamos por modalidade.
kpis_treinamento = (
    treinamentos.groupby("modalidade")
    .agg(
        pessoas=("colaborador_id", "count"),
        taxa_conclusao=("concluiu_bool", "mean"),
        horas_medias=("horas_treinamento", "mean"),
        nota_media=("nota_eficacia", "mean"),
        custo_coffee_total=("custo_coffee", "sum"),
    )
)

kpis_treinamento.round(2)
""", "nb02-011"),
    md("""
## 5. Headcount, representatividade e salarios

Agora olhamos pessoas. Esta parte exige cuidado etico: genero e raca devem ser usados para medir representatividade e possiveis desigualdades, nao para rotular individuos.
""", "nb02-012"),
    code("""
# value_counts conta quantas pessoas existem por area.
headcount_area = colaboradores["area"].value_counts().rename_axis("area").reset_index(name="headcount")

# normalize=True transforma contagem em proporcao.
representatividade_genero = colaboradores["genero"].value_counts(normalize=True).mul(100).round(1)

# Agrupamos salarios por nivel e calculamos estatisticas simples.
salario_por_nivel = (
    colaboradores.groupby("nivel")["salario_mensal"]
    .agg(["count", "mean", "median", "min", "max"])
    .round(0)
)

headcount_area, representatividade_genero, salario_por_nivel
""", "nb02-013"),
    code("""
# Boxplot mostra distribuicao, nao apenas media.
# Ele ajuda a ver dispersao e valores mais extremos.
plt.figure(figsize=(9, 4))
sns.boxplot(data=colaboradores, x="nivel", y="salario_mensal")
plt.title("Distribuicao salarial por nivel")
plt.xlabel("Nivel")
plt.ylabel("Salario mensal")
plt.xticks(rotation=25, ha="right")
plt.tight_layout()
""", "nb02-014"),
    md("""
## 6. Indicadores mensais

Vamos calcular indicadores de turnover, absenteismo e retencao. Observe que cada formula tem numerador, denominador e periodo.
""", "nb02-015"),
    code("""
# Headcount medio reduz distorcao quando ha admissoes e demissoes no mes.
indicadores["headcount_medio"] = (indicadores["headcount_inicio"] + indicadores["headcount_fim"]) / 2

# Turnover mensal: demitidos divididos pelo headcount medio.
indicadores["turnover"] = indicadores["demitidos"] / indicadores["headcount_medio"]

# Absenteismo: dias de ausencia divididos pelo total teorico de dias trabalhados.
indicadores["taxa_absenteismo"] = indicadores["ausencias_dias"] / (
    indicadores["headcount_fim"] * indicadores["dias_trabalho"]
)

# Retencao por diversidade: 1 menos a taxa de desligamentos no grupo de diversidade.
indicadores["retencao_diversidade"] = 1 - (
    indicadores["desligamentos_diversidade"] / indicadores["headcount_diversidade"]
)

indicadores[["mes", "turnover", "taxa_absenteismo", "retencao_diversidade", "corte_gastos_estimado"]].round(4)
""", "nb02-016"),
    code("""
# Um grafico de linha ajuda a ver evolucao no tempo.
plt.figure(figsize=(9, 4))
sns.lineplot(data=indicadores, x="mes", y="turnover", marker="o", label="Turnover")
sns.lineplot(data=indicadores, x="mes", y="taxa_absenteismo", marker="o", label="Absenteismo")
plt.title("Turnover e absenteismo ao longo do tempo")
plt.xlabel("Mes")
plt.ylabel("Taxa")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
""", "nb02-017"),
    md("""
## 7. Exercicios de interpretacao

1. Escolha um indicador de recrutamento e escreva uma conclusao.
2. Escolha um indicador de treinamento e escreva uma limitacao.
3. Explique por que salario medio sozinho nao prova equidade salarial.
4. Identifique um mes que mereceria investigacao em turnover ou absenteismo.
5. Escreva uma recomendacao pratica e nao punitiva para RH.
""", "nb02-018"),
]

nb03 = [
    md("""
# 03 - Estatistica e testes estatisticos em RH

Este notebook pratica estatistica com dados de RH. Vamos calcular medidas descritivas, correlacao, teste t e qui-quadrado.

O objetivo nao e decorar formulas. O objetivo e aprender a fazer perguntas melhores e interpretar resultados com cuidado.
""", "nb03-001"),
    code("""
# pathlib localiza arquivos.
from pathlib import Path

# pandas trabalha com tabelas.
import pandas as pd

# scipy.stats contem funcoes estatisticas prontas.
from scipy import stats

# Localizamos a pasta de dados.
BASE_DIR = Path.cwd().parent if Path.cwd().name == "notebooks" else Path.cwd()
DADOS = BASE_DIR / "dados"

# Abrimos as bases usadas neste notebook.
colaboradores = pd.read_csv(DADOS / "colaboradores.csv")
treinamentos = pd.read_csv(DADOS / "treinamentos.csv")
""", "nb03-002"),
    md("""
## 1. Media, mediana e dispersao

Media mostra um centro aritmetico. Mediana mostra o valor central. Desvio padrao mostra espalhamento. Em salarios, olhar apenas media pode enganar.
""", "nb03-003"),
    code("""
# Agrupamos por nivel porque comparar salarios sem considerar nivel seria injusto.
resumo_salario = (
    colaboradores.groupby("nivel")["salario_mensal"]
    .agg(
        qtd="count",
        media="mean",
        mediana="median",
        desvio="std",
        minimo="min",
        maximo="max",
    )
    .round(1)
)

resumo_salario
""", "nb03-004"),
    md("""
## 2. Correlacao

Correlacao mede associacao entre variaveis numericas. Ela nao prova causa. Aqui vamos observar se absenteismo, horas extras e divergencias de ponto caminham juntos.
""", "nb03-005"),
    code("""
# Selecionamos apenas colunas numericas relevantes para a pergunta.
colunas_correlacao = [
    "absenteismo_dias_ano",
    "horas_extras_mes",
    "divergencias_ponto_mes",
    "nota_performance",
]

# corr() calcula correlacao entre cada par de colunas.
correlacao = colaboradores[colunas_correlacao].corr()

# Arredondamos para facilitar leitura.
correlacao.round(2)
""", "nb03-006"),
    md("""
## 3. Teste t: comparacao de medias

Pergunta: treinamentos presenciais e online tem notas medias de eficacia diferentes?

Hipotese nula: as medias sao iguais.

Hipotese alternativa: as medias sao diferentes.
""", "nb03-007"),
    code("""
# Algumas notas podem estar vazias porque nem todo mundo respondeu.
# dropna remove linhas sem nota para este teste especifico.
notas = treinamentos.dropna(subset=["nota_eficacia"]).copy()

# Separamos as notas em dois grupos.
presencial = notas.loc[notas["modalidade"] == "Presencial", "nota_eficacia"]
online = notas.loc[notas["modalidade"] == "Online", "nota_eficacia"]

# ttest_ind compara medias de dois grupos independentes.
# equal_var=False usa a versao de Welch, mais conservadora quando variancias podem diferir.
resultado_t = stats.ttest_ind(presencial, online, equal_var=False)

print(f"Quantidade presencial: {len(presencial)}")
print(f"Quantidade online: {len(online)}")
print(f"Media presencial: {presencial.mean():.2f}")
print(f"Media online: {online.mean():.2f}")
print(f"p-valor: {resultado_t.pvalue:.4f}")
""", "nb03-008"),
    md("""
### Como interpretar o p-valor

Se o p-valor for menor que 0,05, costumamos dizer que ha evidencia estatistica contra a hipotese nula. Se for maior ou igual a 0,05, nao temos evidencia suficiente para afirmar diferenca estatistica.

Isso nao mede importancia pratica. Tambem nao prova causalidade.
""", "nb03-009"),
    md("""
## 4. Qui-quadrado: associacao entre categorias

Pergunta: existe associacao entre treinamento obrigatorio e conclusao?

Aqui as duas variaveis sao categoricas: `obrigatorio` e `concluiu`.
""", "nb03-010"),
    code("""
# crosstab cria uma tabela de contingencia.
tabela = pd.crosstab(treinamentos["obrigatorio"], treinamentos["concluiu"])

# chi2_contingency aplica o teste qui-quadrado.
chi2, p_valor, graus_liberdade, esperados = stats.chi2_contingency(tabela)

# display mostra a tabela no notebook.
display(tabela)

print(f"Estatistica qui-quadrado: {chi2:.3f}")
print(f"Graus de liberdade: {graus_liberdade}")
print(f"p-valor: {p_valor:.4f}")
""", "nb03-011"),
    md("""
## 5. Exercicios

1. Compare salario medio e mediano entre dois niveis.
2. Calcule a correlacao entre `horas_treinamento_ano` e `nota_performance`.
3. Crie uma hipotese sobre horas extras e teste com media por area.
4. Escreva uma conclusao usando a frase: `neste conjunto de dados didatico...`.
5. Escreva uma limitacao etica ou metodologica da sua analise.
""", "nb03-012"),
]

nb04 = [
    md("""
# 04 - Regressao linear: prever time to hire

Regressao linear e usada quando queremos prever um numero. Neste notebook, o numero e `time_to_hire_dias`, ou seja, quantos dias uma vaga levou da abertura ate a admissao.

Este exemplo e didatico. O dataset e pequeno, entao o foco e entender o processo, nao criar um modelo pronto para uso real.
""", "nb04-001"),
    code("""
# pathlib localiza arquivos.
from pathlib import Path

# pandas trabalha com tabelas.
import pandas as pd

# ColumnTransformer permite tratar colunas numericas e categoricas de formas diferentes.
from sklearn.compose import ColumnTransformer

# LinearRegression e o modelo de regressao linear.
from sklearn.linear_model import LinearRegression

# Metricas para avaliar erro do modelo.
from sklearn.metrics import mean_absolute_error, r2_score

# train_test_split separa dados em treino e teste.
from sklearn.model_selection import train_test_split

# Pipeline junta preprocessamento e modelo em uma unica sequencia.
from sklearn.pipeline import Pipeline

# OneHotEncoder transforma categorias em colunas numericas.
from sklearn.preprocessing import OneHotEncoder

# Localizamos e abrimos a base.
BASE_DIR = Path.cwd().parent if Path.cwd().name == "notebooks" else Path.cwd()
vagas = pd.read_csv(BASE_DIR / "dados" / "vagas_recrutamento.csv")

# Conferimos as primeiras linhas.
vagas.head()
""", "nb04-002"),
    md("""
## 1. Definir alvo e variaveis explicativas

O alvo e o que queremos prever. As variaveis explicativas sao as informacoes usadas para fazer a previsao.
""", "nb04-003"),
    code("""
# Esta e a coluna que queremos prever.
alvo = "time_to_hire_dias"

# Variaveis numericas ja sao numeros e podem entrar no modelo diretamente.
variaveis_numericas = ["candidatos", "entrevistas", "ofertas", "custo_divulgacao"]

# Variaveis categoricas sao textos. Precisam ser convertidas antes do modelo.
variaveis_categoricas = ["area", "senioridade", "source_of_hire", "recrutador"]

# Juntamos todas as variaveis explicativas em uma lista.
variaveis = variaveis_numericas + variaveis_categoricas

# X guarda as variaveis explicativas.
X = vagas[variaveis]

# y guarda a variavel alvo.
y = vagas[alvo]

X.head()
""", "nb04-004"),
    md("""
## 2. Preparar o preprocessamento

Modelos matematicos nao entendem texto como `LinkedIn` ou `RH`. O `OneHotEncoder` transforma cada categoria em colunas de 0 e 1.
""", "nb04-005"),
    code("""
# ColumnTransformer aplica transformacoes diferentes para grupos de colunas.
preprocessamento = ColumnTransformer(
    transformers=[
        # Nas categorias, aplicamos OneHotEncoder.
        ("categorias", OneHotEncoder(handle_unknown="ignore"), variaveis_categoricas),
        # Nos numeros, usamos passthrough, ou seja, passamos como estao.
        ("numeros", "passthrough", variaveis_numericas),
    ]
)

# Pipeline executa primeiro o preprocessamento e depois a regressao.
modelo = Pipeline(
    steps=[
        ("preprocessamento", preprocessamento),
        ("regressao", LinearRegression()),
    ]
)
""", "nb04-006"),
    md("""
## 3. Separar treino e teste

Treino e usado para aprender. Teste e usado para avaliar com dados que o modelo nao viu durante o treino.
""", "nb04-007"),
    code("""
# test_size=0.25 significa que 25% dos dados ficarao para teste.
# random_state fixa a aleatoriedade para o resultado ser reproduzivel.
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
)

# fit treina o modelo com os dados de treino.
modelo.fit(X_treino, y_treino)

# predict gera previsoes para os dados de teste.
previsoes = modelo.predict(X_teste)
""", "nb04-008"),
    md("""
## 4. Comparar real versus previsto

A tabela abaixo mostra, para cada vaga do teste, o valor real, o valor previsto e o erro absoluto.
""", "nb04-009"),
    code("""
# Criamos uma tabela para comparar resultados.
resultado = pd.DataFrame({
    "real": y_teste.values,
    "previsto": previsoes.round(1),
})

# Erro absoluto e a distancia entre real e previsto, ignorando sinal.
resultado["erro_absoluto"] = (resultado["real"] - resultado["previsto"]).abs().round(1)

resultado
""", "nb04-010"),
    md("""
## 5. Avaliar o modelo

Erro medio absoluto e facil de explicar: em media, quantos dias o modelo erra. R2 mede quanto da variacao foi explicada, mas e menos intuitivo para publico iniciante.
""", "nb04-011"),
    code("""
# mean_absolute_error calcula a media dos erros absolutos.
mae = mean_absolute_error(y_teste, previsoes)

# r2_score calcula o R2.
r2 = r2_score(y_teste, previsoes)

print(f"Erro medio absoluto: {mae:.1f} dias")
print(f"R2: {r2:.2f}")
""", "nb04-012"),
    md("""
## 6. Simular uma nova vaga

Agora criamos uma vaga ficticia e pedimos uma previsao. Isso ajuda a entender como o modelo seria usado, mas nao transforma o resultado em certeza.
""", "nb04-013"),
    code("""
# Criamos um DataFrame com uma unica nova vaga.
# As colunas precisam ter os mesmos nomes usados no treino.
nova_vaga = pd.DataFrame([
    {
        "candidatos": 70,
        "entrevistas": 12,
        "ofertas": 2,
        "custo_divulgacao": 800,
        "area": "RH",
        "senioridade": "Pleno",
        "source_of_hire": "LinkedIn",
        "recrutador": "Ana",
    }
])

# O modelo devolve uma previsao em dias.
previsao = modelo.predict(nova_vaga)[0]

print(f"Previsao didatica de time to hire: {previsao:.0f} dias")
""", "nb04-014"),
    md("""
## 7. Exercicios

1. Remova `recrutador` das variaveis e rode novamente.
2. Altere a `nova_vaga` para uma vaga de TI senior.
3. Compare o erro medio absoluto antes e depois.
4. Escreva uma frase executiva explicando o erro do modelo.
5. Escreva uma limitacao etica ou metodologica deste modelo.
""", "nb04-015"),
]

nb05 = [
    md("""
# 05 - Arvore de decisao: risco de turnover

Arvore de decisao e um modelo que cria regras para prever uma categoria. Aqui a categoria e `desligou_12m`: 1 significa desligou, 0 significa nao desligou.

Este notebook e didatico. Em uma empresa real, modelos de turnover exigem governanca, privacidade, validacao e revisao etica.
""", "nb05-001"),
    md("""
## Cuidado etico antes do codigo

Uma previsao de turnover nunca deve ser usada para punir uma pessoa. O uso responsavel e investigar condicoes de trabalho, carga, carreira, lideranca, apoio e oportunidades.
""", "nb05-002"),
    code("""
# pathlib localiza arquivos.
from pathlib import Path

# pandas trabalha com tabelas.
import pandas as pd

# Ferramentas de preprocessamento e modelagem.
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier, export_text

# Localizamos e abrimos a base.
BASE_DIR = Path.cwd().parent if Path.cwd().name == "notebooks" else Path.cwd()
colaboradores = pd.read_csv(BASE_DIR / "dados" / "colaboradores.csv")

# Conferimos as primeiras linhas.
colaboradores.head()
""", "nb05-003"),
    md("""
## 1. Escolher alvo e variaveis explicativas

O alvo e `desligou_12m`. As variaveis explicativas sao sinais historicos como absenteismo, horas extras, tempo de empresa e performance.
""", "nb05-004"),
    code("""
# Coluna que queremos prever.
alvo = "desligou_12m"

# Variaveis numericas usadas pelo modelo.
variaveis_numericas = [
    "idade",
    "tempo_empresa_meses",
    "salario_mensal",
    "horas_treinamento_ano",
    "absenteismo_dias_ano",
    "horas_extras_mes",
    "divergencias_ponto_mes",
    "nota_performance",
]

# Variaveis categoricas precisam ser convertidas com OneHotEncoder.
variaveis_categoricas = ["area", "nivel"]

# Lista completa de variaveis.
variaveis = variaveis_numericas + variaveis_categoricas

# X contem as informacoes usadas para prever.
X = colaboradores[variaveis]

# y contem o resultado real.
y = colaboradores[alvo]

# Vemos a proporcao de cada classe.
y.value_counts(normalize=True).rename("proporcao")
""", "nb05-005"),
    md("""
## 2. Criar pipeline e separar treino/teste

Usamos pipeline para garantir que o preprocessamento e o modelo sejam aplicados juntos. A arvore tem profundidade limitada para ficar mais interpretavel.
""", "nb05-006"),
    code("""
# Preprocessamento: categorias viram colunas numericas; numeros passam direto.
preprocessamento = ColumnTransformer(
    transformers=[
        ("categorias", OneHotEncoder(handle_unknown="ignore"), variaveis_categoricas),
        ("numeros", "passthrough", variaveis_numericas),
    ]
)

# Criamos uma arvore pequena.
# max_depth=3 limita a quantidade de perguntas em sequencia.
# min_samples_leaf=3 evita folhas com pouquissimos exemplos.
modelo = Pipeline(
    steps=[
        ("preprocessamento", preprocessamento),
        ("arvore", DecisionTreeClassifier(max_depth=3, min_samples_leaf=3, random_state=42)),
    ]
)

# stratify=y tenta manter a proporcao de desligou/nao desligou em treino e teste.
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y,
)

# Treinamos o modelo.
modelo.fit(X_treino, y_treino)

# Geramos previsoes para o conjunto de teste.
previsoes = modelo.predict(X_teste)
""", "nb05-007"),
    md("""
## 3. Avaliar resultados

Acuracia mostra o percentual geral de acertos. Matriz de confusao mostra onde o modelo acerta e erra. Em RH, os tipos de erro importam muito.
""", "nb05-008"),
    code("""
# Acuracia geral.
print(f"Acuracia: {accuracy_score(y_teste, previsoes):.2f}")

# Matriz de confusao.
# Linhas sao valores reais; colunas sao previsoes.
print("Matriz de confusao:")
print(confusion_matrix(y_teste, previsoes))

# Relatorio com precisao, recall e f1-score.
print("\nRelatorio de classificacao:")
print(classification_report(y_teste, previsoes, target_names=["Nao desligou", "Desligou"], zero_division=0))
""", "nb05-009"),
    md("""
## 4. Ler regras da arvore

Uma vantagem da arvore e que conseguimos imprimir regras. Isso ajuda na explicacao, mas nao elimina o cuidado etico.
""", "nb05-010"),
    code("""
# Recuperamos o preprocessador treinado dentro do pipeline.
preprocessador_treinado = modelo.named_steps["preprocessamento"]

# Pegamos os nomes das colunas depois do OneHotEncoder.
nomes_features = preprocessador_treinado.get_feature_names_out()

# Recuperamos a arvore treinada.
arvore = modelo.named_steps["arvore"]

# Imprimimos as regras em texto.
print(export_text(arvore, feature_names=list(nomes_features)))
""", "nb05-011"),
    md("""
## 5. Interpretar como RH

Uma interpretacao ruim seria: `a pessoa vai sair`.

Uma interpretacao melhor seria: `no historico didatico, determinados sinais aparecem associados a maior taxa de desligamento; isso pode orientar investigacao sobre carga, apoio, lideranca, carreira e condicoes de trabalho`.
""", "nb05-012"),
    md("""
## 6. Exercicios

1. Altere `max_depth` para 2 e compare as regras.
2. Remova `salario_mensal` das variaveis e rode novamente.
3. Observe se a matriz de confusao mudou.
4. Escreva uma recomendacao de RH que nao seja punitiva.
5. Escreva uma frase explicando por que este modelo nao deve ser usado para decidir desligamentos.
""", "nb05-013"),
]


def main() -> None:
    NOTEBOOKS.mkdir(exist_ok=True)
    write_notebook("00_fundamentos_python.ipynb", nb00)
    write_notebook("01_primeiros_passos_python.ipynb", nb01)
    write_notebook("02_analise_exploratoria_rh.ipynb", nb02)
    write_notebook("03_estatistica_e_testes.ipynb", nb03)
    write_notebook("04_regressao_linear_time_to_hire.ipynb", nb04)
    write_notebook("05_arvore_decisao_turnover.ipynb", nb05)


if __name__ == "__main__":
    main()
