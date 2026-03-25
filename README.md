# Lab01_PART1_4425860
# Lab01 - Ingestão de Dados End-to-End (People Analytics)

## 1. Arquitetura do Projeto
O projeto utiliza a **Arquitetura Medallion** para processar dados de RH:
- **[span_1](start_span)Camada Bronze:** Ingestão dos dados brutos em CSV[span_1](end_span).
- **[span_2](start_span)[span_3](start_span)Camada Silver:** Limpeza, padronização (snake_case) e conversão para Parquet[span_2](end_span)[span_3](end_span).
- **[span_4](start_span)[span_5](start_span)Camada Gold:** Carga dos dados tratados para o banco PostgreSQL (Star Schema)[span_4](end_span)[span_5](end_span).

## 2. Dicionário de Dados
| Coluna | Descrição |
| :--- | :--- |
| id_colaborador | Identificador único do funcionário. |
| departamento | Setor de atuação (TI, RH, Vendas, etc.). |
| salario_base | Valor do salário mensal fixo. |
| horas_extras | Quantidade de horas extras realizadas. |
| data_admissao | Data de entrada na empresa. |

## 3. Qualidade de Dados
[span_6](start_span)Durante o tratamento na Camada Silver, foram aplicadas as seguintes melhorias[span_6](end_span):
- Remoção de possíveis linhas duplicadas.
- Conversão da coluna `data_admissao` de texto para o formato Date.
- Padronização dos nomes das colunas para letras minúsculas.

## 4. Instruções de Execução
Para rodar este projeto localmente, siga a ordem:
1. [span_7](start_span)Instale as dependências: `pip install -r requirements.txt`[span_7](end_span).
2. Execute a ingestão inicial: `python bronze.py`.
3. Execute o tratamento: `python silver.py`.
4. Carregue os dados no banco: `python gold.py`.
Custo Total: Qual é o gasto total da empresa com salários base por departamento?  
Horas Extras: Qual departamento teve o maior volume de horas extras pagas?  
Investimento vs. Extra: Qual a relação percentual entre horas extras e salário base em cada setor? (Esta é a pergunta sugerida no PDF)   
Retenção: Quantos funcionários foram contratados em cada ano? (Para ver o crescimento da empresa)   
Média Salarial: Qual é o salário médio por departamento para identificar disparidades? 
