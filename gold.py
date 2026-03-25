import pandas as pd
from sqlalchemy import create_engine
import os

# Configuração de caminhos e conexão
PATH_SILVER = "data/silver/dados_rh_silver.parquet"
# IMPORTANTE: Ajuste 'usuario', 'senha' e 'nome_do_banco' conforme sua instalação do Postgres
CONN_STR = "postgresql://usuario:senha@localhost:5432/nome_do_banco"

def carregar_gold():
    if not os.path.exists(PATH_SILVER):
        print("Arquivo Silver não encontrado! Rode o silver.py primeiro.")
        return

    print("Lendo dados da Camada Silver...")
    df = pd.read_parquet(PATH_SILVER)

    print("Conectando ao PostgreSQL e carregando dados...")
    engine = create_engine(CONN_STR)
    
    # Salva os dados na tabela 'fato_rh' no Postgres
    df.to_sql('fato_rh', engine, if_exists='replace', index=False)
    
    print("Sucesso! Dados carregados na Camada Gold (Postgres).")

if __name__ == "__main__":
    carregar_gold()
