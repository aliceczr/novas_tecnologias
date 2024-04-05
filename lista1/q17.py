def numero_conta_completo(numero_conta):
    soma_digitos = sum(int(digito) for digito in str(numero_conta))
    digito_verificador = soma_digitos % 10
    return f"00{numero_conta}-{digito_verificador}"

numero_conta = input("Digite o número da conta (até seis dígitos): ")
print("Número completo da conta:", numero_conta_completo(numero_conta))
