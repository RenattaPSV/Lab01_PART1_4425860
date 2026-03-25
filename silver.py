import pandas as pd
import os

# Configuração de caminhos
PATH_RAW = "data/raw/dados_rh_brutos.csv"
PATH_SILVER = "data/silver/"
os.makedirs(PATH_SILVER, exist_ok=True)

def processar_silver():
    print("Iniciando tratamento na Camada Silver...")
    
    # 1. Leitura do dado bruto
    df = pd.read_csv(PATH_RAW)
    
    # 2. Padronização de nomes (snake_case)
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]
    
    # 3. Limpeza: Remover duplicatas e nulos
    df = df.drop_duplicates()
    df = df.dropna()
    
    # 4. Conversão de tipos (Garantir que data é data)
    df['data_admissao'] = pd.to_datetime(df['data_admissao'])
    
    # 5. Persistência em Parquet
    destino = os.path.join(PATH_SILVER, 'dados_rh_silver.parquet')
    df.to_parquet(destino, index=False)
    
    print(f"Sucesso! Relatório básico gerado:")
    print(df.info())
    print(f"Arquivo salvo em {destino}")

if __name__ == "__main__":
    processar_silver()
