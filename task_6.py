def fact(x):
    if x == 0 or x ==1:
        return 1
    return x * fact(x-1)

x = int(input())
print(fact(x))

'''
Esse é um exemplo de uma aplicação simples em Python que calcula o fatorial de um número inteiro. 
A função "fact" é definida para calcular o fatorial de um número "x".

A lógica da função é a seguinte:

Se "x" for igual a 0 ou 1, a função retorna 1, pois 0! e 1! são ambos iguais a 1.

Se "x" for diferente de 0 e 1, a função retorna "x" multiplicado pelo fatorial de "x-1". 
Isso é feito recursivamente, o que significa que a função chama a si mesma até que o valor de "x" 
seja igual a 0 ou 1.

Depois de definida a função "fact", o código pede para o usuário inserir um número inteiro "x". 
Este valor é então passado como argumento para a função "fact", que calcula o fatorial de "x" e o retorna. Finalmente, o resultado é impresso na tela.

'''