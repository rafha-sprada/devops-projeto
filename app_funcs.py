
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("divisao por zero")
    return a / b

def saudacao(nome):
    return f"Olá, {nome}!"
