def EvenGenerator(n):
    i=0
    while i <= n:
        if i % 2 == 0:
            yield i
        i += 1
n = int(input())
values = []
for i in EvenGenerator(n):
    values.append(str(i))
print(", ".join(values))

'''
Este código define uma função chamada "EvenGenerator" que recebe um número inteiro "n" 
como entrada e gera (ou retorna) números pares de 0 até "n".

A função utiliza um laço "while" para gerar cada número par. 
O operador "%" é usado para determinar se o número é par, 
e a instrução "yield" é usada para retornar o número par.

Depois, é criada uma lista vazia chamada "values" e um laço "for" é usado para adicionar cada número gerado pela função "EvenGenerator" na lista "values". Em seguida, a lista "values" é convertida em uma string separada por vírgulas e é impressa na tela usando a função "print".
'''