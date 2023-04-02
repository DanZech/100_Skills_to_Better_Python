l = []
for i in range(1000, 1500):
    if (i % 7 == 0) and (i % 5 !=0):
        l.append(str(i))
t = ','.join(l)
print(t)

'''
Este é um exemplo de como encontrar todos os números divisíveis por 7, mas não divisíveis por 5, entre 1000 e 1500 e imprimi-los como uma string separada por vírgulas.

A primeira linha cria uma lista vazia, "l".

Em seguida, um loop "for" é usado para percorrer os números entre 1000 e 1500. A função "range" é usada para isso.

Dentro do loop, um teste de divisibilidade é feito para cada número. Se o número for divisível por 7 (verificado usando o operador de módulo, "%") e não for divisível por 5, ele é adicionado à lista "l" usando o método "append".

Após o loop, a função "join" é usada para juntar todos os elementos da lista "l" em uma única string, separados por vírgulas. A string resultante é armazenada na variável "t".

Por fim, a string "t" é impressa na tela. Isso exibe todos os números que atendem aos critérios mencionados acima, separados por vírgulas.'''
