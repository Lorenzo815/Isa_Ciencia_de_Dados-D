# Aula extra: Datasets publicos do Kaggle

## Objetivo da aula

Aprender a usar datasets publicos como ambiente de pratica, sem confundir dados didaticos com dados adequados para decisao real. O Kaggle e excelente para estudar, mas cada dataset precisa ser entendido em contexto.

## 1. O que e Kaggle

Kaggle e uma plataforma com datasets, notebooks e competicoes de ciencia de dados. Muitas pessoas usam Kaggle para praticar pandas, estatistica, visualizacao e modelos.

Para este curso, o Kaggle entra como laboratorio. A pessoa estudante pode pegar uma base maior, explorar colunas novas, comparar com os dados sinteticos do curso e treinar modelos com mais linhas.

## 2. Datasets publicos nao sao automaticamente bons

Um dataset publico pode ter problemas:

- Colunas mal documentadas.
- Dados antigos.
- Dados de outro pais ou contexto cultural.
- Variaveis sensiveis sem explicacao clara.
- Alvo mal definido.
- Dados ja muito tratados, distantes da realidade operacional.
- Licenca ou termos de uso restritivos.

Antes de analisar, leia a pagina do dataset, autor, descricao, licenca e discussoes quando existirem.

## 3. Como baixar os datasets sugeridos

Instale as dependencias do curso:

```bash
pip install -r requirements.txt
```

Depois execute:

```bash
python scripts/baixar_datasets_kaggle.py
```

O script tenta baixar datasets publicos relacionados a RH e salva copias locais em `dados_kaggle/`. O Kaggle pode exigir login e aceite dos termos na pagina do dataset.

## 4. Datasets sugeridos

Os slugs podem mudar com o tempo, mas sao bons pontos de partida:

- `pavansubhasht/ibm-hr-analytics-attrition-dataset`: attrition de colaboradores da IBM.
- `arashnic/hr-analytics-job-change-of-data-scientists`: mudanca de emprego em profissionais de dados.
- `rishikeshkonapure/hr-analytics-prediction`: base para previsao de attrition.

Use esses dados para praticar, nao para concluir como funciona o RH de uma empresa real brasileira.

## 5. Checklist antes de analisar um dataset externo

Antes de escrever codigo, responda:

1. Qual e a unidade de analise?
2. Qual coluna representa o resultado principal?
3. O que cada linha representa?
4. Existe dicionario de dados?
5. Existem dados sensiveis?
6. Ha valores ausentes?
7. As categorias fazem sentido no contexto brasileiro?
8. O dataset tem licenca adequada para estudo?
9. Qual pergunta de RH ele permite responder?
10. Qual pergunta ele nao permite responder?

## 6. Como comparar Kaggle com os dados do curso

Use `dados/colaboradores.csv` como referencia didatica. Compare:

- Quais colunas existem nos dois datasets?
- Como o alvo de desligamento e definido?
- Ha variaveis de salario, tempo de empresa, treinamento ou absenteismo?
- Existem dados sensiveis?
- O dataset e mais adequado para estatistica descritiva ou modelagem?

Essa comparacao ajuda a perceber que dados nunca chegam neutros. Eles carregam escolhas de coleta, definicao e contexto.

## 7. Risco de overfitting cultural

Um modelo treinado em um dataset publico pode aprender padroes de uma empresa, pais, periodo ou processo especifico. Aplicar esse modelo diretamente a outra organizacao seria arriscado.

Exemplo: fatores ligados a attrition em uma empresa global de tecnologia podem nao representar uma operacao industrial brasileira, uma rede de varejo ou um hospital.

Por isso, Kaggle e otimo para aprender tecnica. Para decisao real, precisamos de dados reais, governanca, validacao e contexto.

## Perguntas e respostas

**Posso usar qualquer dataset publico no curso?**

Pode usar para estudo, desde que respeite licenca e termos. Para publicar ou compartilhar resultados, leia as regras do dataset.

**Se o Kaggle mostra uma acuracia alta, o modelo e bom?**

Nao necessariamente. Pode haver vazamento de dados, divisao inadequada de treino e teste, alvo facil demais ou contexto irrelevante para outro uso.

**Por que comparar com os dados sinteticos do curso?**

Porque os dados sinteticos foram desenhados para ensinar conceitos de RH. Os dados do Kaggle podem ser maiores, mas nem sempre sao mais claros.

**O que fazer se o download falhar?**

Verifique login no Kaggle, aceite dos termos do dataset e conexao. Mesmo datasets publicos podem exigir autenticacao.

**Kaggle serve para portfolio?**

Sim, se a analise for bem explicada. Um bom portfolio mostra pergunta, limpeza, exploracao, modelo, limitacoes e comunicacao, nao apenas codigo.

## Exercicios

### Fixacao

1. Explique por que dataset publico nao e automaticamente confiavel.
2. Liste cinco itens do checklist de avaliacao de dataset externo.
3. Explique a diferenca entre usar Kaggle para estudo e usar dados reais para decisao.

### Aplicacao

1. Execute `python scripts/baixar_datasets_kaggle.py`.
2. Escolha um dataset baixado.
3. Liste todas as colunas.
4. Identifique a unidade de analise e a variavel alvo.
5. Compare tres colunas dele com `dados/colaboradores.csv`.

### Desafio

Escolha um dataset do Kaggle e escreva uma ficha critica com: origem, objetivo, unidade de analise, variavel alvo, possiveis vieses, dados sensiveis, uso adequado e uso inadequado.

## Fechamento

Datasets publicos sao um excelente treino, mas o bom senso analitico continua indispensavel. Antes de perguntar "qual modelo posso treinar?", pergunte "que realidade este dataset representa?".
