def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:  # Certificando-se de não dividir por zero
            return num1 / num2
        else:
            return "Não é possível dividir por zero"
    else:
        return 0  # Retorno padrão se a operação não for reconhecida

# Exemplo de uso:
num1 = 10
num2 = 5
op = 3  # Escolha a operação: 1 para soma, 2 para subtração, 3 para multiplicação, 4 para divisão

resultado = calculadora(num1, num2, op)
print(f"Resultado da operação: {resultado}")
