# Dicionário de dados

Este arquivo explica as principais colunas usadas no curso. Use-o como consulta rápida sempre que cruzar com uma coluna desconhecida em um notebook ou exercício.

Convenções gerais:

- `*_id` é uma chave que identifica a linha de forma única.
- Datas estão no formato `AAAA-MM-DD`.
- Variáveis sensíveis (gênero, raça, salário) só devem ser usadas para análises agregadas e com finalidade clara.
- Os datasets são sintéticos: úteis para aprender, inadequados para conclusões reais sobre empresas, pessoas ou políticas públicas.

## `dados/vagas_recrutamento.csv`

| Coluna | Significado |
|---|---|
| `vaga_id` | Identificador da vaga |
| `cargo` | Nome do cargo |
| `area` | Área solicitante |
| `senioridade` | Nível da vaga |
| `source_of_hire` | Canal ou fonte de contratação |
| `data_abertura` | Data de abertura da vaga |
| `data_admissao` | Data de admissão da pessoa contratada |
| `time_to_hire_dias` | Dias entre abertura e admissão |
| `candidatos` | Total de candidaturas |
| `entrevistas` | Total de entrevistas realizadas |
| `ofertas` | Total de propostas feitas |
| `contratados` | Total de pessoas contratadas |
| `custo_divulgacao` | Custo aproximado de divulgação da vaga |
| `recrutador` | Pessoa responsável pela vaga |

## `dados/treinamentos.csv`

| Coluna | Significado |
|---|---|
| `colaborador_id` | Identificador da pessoa |
| `area` | Área da pessoa |
| `treinamento` | Nome do treinamento |
| `horas_treinamento` | Carga horária realizada |
| `obrigatorio` | Se o treinamento era obrigatório |
| `concluiu` | Se a pessoa concluiu |
| `nota_eficacia` | Avaliação percebida de eficácia, de 1 a 5 |
| `custo_coffee` | Custo associado a coffee break |
| `modalidade` | Presencial, online ou híbrido |

## `dados/colaboradores.csv`

| Coluna | Significado |
|---|---|
| `genero` | Gênero autodeclarado no exemplo didático |
| `raca` | Raça/cor autodeclarada no exemplo didático |
| `tempo_empresa_meses` | Tempo de empresa em meses |
| `salario_mensal` | Salário mensal bruto fictício |
| `horas_treinamento_ano` | Horas de treinamento no ano |
| `absenteismo_dias_ano` | Dias de ausência no ano |
| `horas_extras_mes` | Horas extras no mês de referência |
| `divergencias_ponto_mes` | Quantidade de divergências de ponto no mês |
| `nota_performance` | Avaliação fictícia de performance, de 1 a 5 |
| `desligou_12m` | 1 se desligou em até 12 meses, 0 caso contrário |

## `dados/distribuicoes_exercicio.xlsx` e `dados/distribuicoes_resolvido.xlsx`

Planilhas multi-abas usadas na Aula 2 para praticar distribuições e escolha de testes estatísticos. A aba `Dados` traz 1.200 colaboradores sintéticos com colunas numéricas de distribuições diferentes (lognormal, normal, exponencial, gamma, Poisson, bimodal) e categóricas (`area`, `genero`, `tipo_contrato`). O arquivo resolvido inclui estatísticas, histogramas, testes de normalidade, decisão entre paramétrico e não paramétrico, e testes prontos com interpretação.

Veja a aba `Dicionario` dentro do arquivo para descrição coluna a coluna.

## Observação ética

Dados sensíveis como gênero e raça devem ser usados para medir equidade, barreiras e representatividade. Eles não devem ser usados para discriminar, punir ou automatizar decisões individuais sem governança adequada.

Mesmo em dados sintéticos como os deste curso, é boa prática treinar o reflexo: pergunte sempre "que decisão essa análise pode influenciar?" e "quem pode ser prejudicado se eu interpretar mal?".
