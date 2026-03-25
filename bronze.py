import pandas as pd
import numpy as np
import os

# [span_2](start_span)Cria o diretório raw se não existir[span_2](end_span)
PATH_RAW = "data/raw/"
os.makedirs(PATH_RAW, exist_ok=True)

def ingestao_bronze():
    print("Gerando 1 milhão de linhas de dados de RH...")
    n_rows = 1000000
    
    # [span_3](start_span)Criando dados fictícios ricos em tipagem[span_3](end_span)
    data = {
        'ID_Colaborador': range(1, n_rows + 1),
        'Nome_Funcionario': [f'Colaborador {i}' for i in range(n_rows)],
        'Departamento': np.random.choice(['TI', 'RH', 'Vendas', 'Financeiro', 'Operações'], n_rows),
        'Salario_Base': np.random.uniform(3000, 15000, n_rows),
        'Horas_Extras': np.random.uniform(0, 40, n_rows),
        'Data_Admissao': pd.to_datetime(np.random.choice(pd.date_range('2018-01-01', '2023-12-31'), n_rows))
    }
    
    df = pd.DataFrame(data)
    
    # [span_4](start_span)Salva no diretório data/raw/ sem alterações[span_4](end_span)
    df.to_csv(os.path.join(PATH_RAW, 'dados_rh_brutos.csv'), index=False)
    print(f"Arquivo salvo com sucesso em {PATH_RAW}")

if __name__ == "__main__":
    ingestao_bronze()
