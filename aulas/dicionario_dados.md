# Dicionário de dados

Este arquivo explica as principais colunas usadas no curso.

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

## Observação ética

Dados sensíveis como gênero e raça devem ser usados para medir equidade, barreiras e representatividade. Eles não devem ser usados para discriminar, punir ou automatizar decisões individuais sem governança adequada.
