# Função para gerar a sequência de Fibonacci até que ultrapasse o número informado
def pertence_fibonacci(numero):
    # Definindo os dois primeiros termos da sequência de Fibonacci
    a, b = 0, 1
    # Sequência inicial
    sequencia = [a, b]
    
    # Gerando a sequência até que o próximo número seja maior que o informado
    while b < numero:
        a, b = b, a + b
        sequencia.append(b)
    
    # Verifica se o número informado pertence à sequência
    if numero in sequencia:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} NÃO pertence à sequência de Fibonacci."

# Número a ser verificado
numero = int(input("Informe um número: "))
resultado = pertence_fibonacci(numero)
print(resultado)
