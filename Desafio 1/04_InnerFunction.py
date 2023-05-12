# Criar uma função externa que irá aceitar dois parametros, a e b
# Crie uma função interna dentro da função externa que irá retornar a soma os parametros a e b 
# Na função externa, adicione 5 ao retorno da funcao interna e escreva na tela este valor

def soma_externa(a, b):
    def soma_interna():
        return a+b;
    print(soma_interna() + 5)

a = input('a: ')
b = input('b: ')
soma_externa(float(a), float(b))