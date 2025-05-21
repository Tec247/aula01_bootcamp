# 1) Solicita ao usuário que digite seu nome
CONSTANTE_BONUS = 1000
nome = input("Digite seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante 
salario = float(input("Digite o seu salário: R$ "))
# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = float(input("Digite o percentual do seu bônus:"))
# 4) Calcule o valor do bônus final
kpi = CONSTANTE_BONUS + salario * bonus
# 5) Imprimir cálculo do KPI para usuário
print(f"{CONSTANTE_BONUS} + {salario} * {bonus}")
# 6) Imprimir a mensagem personalizada incluindo o nome do usuário, salário e bônus 
print(f"O usuário {nome} possui um salario como o bônus de R$ {kpi}")
# Bônus: Quantos bugs e riscos você consegue identificar nesse programa? 