# Programa de controle de níveis de água
# Autor: Maria Clara Lima

# Início
from colorama import Fore, Style

# Entrada
nivel=int(input("Digite o nível do reservatório, de 1 a 5: "))

#Processamento e Saída
if nivel ==1:
    print(Fore.RED + "Nível muito baixo - CRÍTICO")
elif nivel==2:
    print(Fore.YELLOW + "Nível baixo")
elif nivel==3:
    print(Fore.GREEN + "Nível médio")
elif nivel==4:
    print(Fore.CYAN + "Nível alto")
else:
    print(Fore.BLUE + "Nível muito alto - ALERTA")

print(Style.RESET_ALL)
