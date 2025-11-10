import boto3
import os

# --- Configuração ---
# !! MUDE OS DOIS !!
NOME_DO_BUCKET = "bucket-pdroozi-projeto-prouni"  # 1. Coloque o nome único do seu bucket
NOME_DA_REGIAO = "us-east-1"                       # 2. Coloque a região (ex: 'us-east-1', 'sa-east-1')
# --------------------

ARQUIVO_LOCAL = "dados/ProUniTrienio.csv"
NOME_NO_S3 = "dados/ProUniTrienio.csv"  # Pasta/nome que o arquivo terá no S3

# Inicia o cliente S3, especificando a região
s3_client = boto3.client('s3', region_name=NOME_DA_REGIAO)

# --- 1. Tentar Criar o Bucket ---
print(f"Verificando/Criando bucket: {NOME_DO_BUCKET} na região {NOME_DA_REGIAO}")
try:
    # Lógica especial para 'us-east-1' (não precisa de LocationConstraint)
    if NOME_DA_REGIAO == 'us-east-1':
        s3_client.create_bucket(Bucket=NOME_DO_BUCKET)
    else:
        location = {'LocationConstraint': NOME_DA_REGIAO}
        s3_client.create_bucket(
            Bucket=NOME_DO_BUCKET,
            CreateBucketConfiguration=location
        )
    print(f"Bucket '{NOME_DO_BUCKET}' criado com sucesso.")

except s3_client.exceptions.BucketAlreadyOwnedByYou:
    # Isso não é um erro, o bucket já existe e podemos usá-lo.
    print(f"Bucket '{NOME_DO_BUCKET}' já existe e pertence a você. Continuando.")
except s3_client.exceptions.BucketAlreadyExists:
    # Isso é um erro. O nome já foi pego por outra pessoa no mundo.
    print(f"Erro: O nome do bucket '{NOME_DO_BUCKET}' já existe globalmente e não pertence a você. Escolha outro nome.")
    exit() # Sai do script
except Exception as e:
    print(f"Erro desconhecido ao criar bucket: {e}")
    exit() # Sai do script

# --- 2. Fazer o Upload (só se o Passo 1 deu certo) ---
print(f"Iniciando upload do arquivo: {ARQUIVO_LOCAL}")
caminho_arquivo_local = ARQUIVO_LOCAL

try:
    s3_client.upload_file(
        caminho_arquivo_local, 
        NOME_DO_BUCKET, 
        NOME_NO_S3
    )
    print(f"Sucesso! Arquivo '{caminho_arquivo_local}' enviado para '{NOME_NO_S3}' no bucket '{NOME_DO_BUCKET}'.")

except Exception as e:
    print(f"Erro durante o upload: {e}")