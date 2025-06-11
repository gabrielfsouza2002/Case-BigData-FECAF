# scripts/backup_restore.py

import os
import subprocess
from datetime import datetime

# Configurações do MongoDB
MONGO_HOST = "localhost"
MONGO_PORT = "27017"
DB_NAME = "eshop_db"
MONGO_USER = "eshopuser"
MONGO_PASS = "eshoppassword" # Usar variáveis de ambiente em produção!

BACKUP_DIR = "./backups" # Diretório onde os backups serão salvos

def run_command(command):
    """Executa um comando de shell e imprime a saída."""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar comando: {e}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        return False

def backup_mongodb():
    """Realiza um backup do banco de dados MongoDB."""
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = os.path.join(BACKUP_DIR, f"{DB_NAME}_{timestamp}")
    
    # Comando mongodump
    # Para usar o container MongoDB diretamente, substitua 'mongodump' por 'docker exec mongodb_eshop mongodump ...'
    command = (
        f"mongodump --host {MONGO_HOST} --port {MONGO_PORT} "
        f"--username {MONGO_USER} --password {MONGO_PASS} "
        f"--authenticationDatabase admin --db {DB_NAME} --out {output_dir}"
    )
    print(f"Iniciando backup para: {output_dir}...")
    if run_command(command):
        print("Backup concluído com sucesso!")
    else:
        print("Falha no backup.")

def restore_mongodb(backup_path: str):
    """Restaura um banco de dados MongoDB a partir de um backup."""
    if not os.path.exists(backup_path):
        print(f"Erro: Caminho do backup '{backup_path}' não encontrado.")
        return

    # Comando mongorestore
    # Para usar o container MongoDB diretamente, substitua 'mongorestore' por 'docker exec mongodb_eshop mongorestore ...'
    command = (
        f"mongorestore --host {MONGO_HOST} --port {MONGO_PORT} "
        f"--username {MONGO_USER} --password {MONGO_PASS} "
        f"--authenticationDatabase admin --drop {backup_path}" # --drop para dropar o DB existente antes de restaurar
    )
    print(f"Iniciando restauração de: {backup_path}...")
    if run_command(command):
        print("Restauração concluída com sucesso!")
    else:
        print("Falha na restauração.")

if __name__ == "__main__":
    print("--- Gerenciamento de Backup/Restauração do MongoDB ---")
    print("1. Fazer backup do banco de dados")
    print("2. Restaurar o banco de dados")
    
    choice = input("Escolha uma opção (1 ou 2): ")
    
    if choice == '1':
        backup_mongodb()
    elif choice == '2':
        available_backups = [d for d in os.listdir(BACKUP_DIR) if os.path.isdir(os.path.join(BACKUP_DIR, d))]
        if not available_backups:
            print("Nenhum backup encontrado para restaurar.")
        else:
            print("\nBackups disponíveis:")
            for i, backup in enumerate(available_backups):
                print(f"{i+1}. {backup}")
            
            try:
                backup_choice = int(input("Escolha o número do backup para restaurar: ")) - 1
                if 0 <= backup_choice < len(available_backups):
                    selected_backup_path = os.path.join(BACKUP_DIR, available_backups[backup_choice], DB_NAME)
                    restore_mongodb(selected_backup_path)
                else:
                    print("Escolha inválida.")
            except ValueError:
                print("Entrada inválida. Digite um número.")
    else:
        print("Opção inválida.")