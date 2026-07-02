from datetime import datetime

# 1. Lê a data do usuário
entrada = input("Digite uma data no formato dd/mm/aaaa: ")

try:
    # 2. Tenta converter o texto para data (valida automaticamente dias e meses)
    data = datetime.strptime(entrada, "%d/%m/%Y")
    
    # 3. Verifica se o ano está entre 1900 e 2100
    if 1900 <= data.year <= 2100:
        print("A data informada é válida")
    else:
        print("A data informada não é válida")
        
except ValueError:
    # Cai aqui se o dia for inválido para o mês ou se o texto estiver errado
    print("A data informada não é válida")
