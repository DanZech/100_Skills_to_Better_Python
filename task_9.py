def printDict():
    d=dict()
    for i in range(1, 21):
        d[i] = i **2
    for (k,v) in d.items():
        #print(v)
        print(k,v)
printDict()

'''
Este é um exemplo de como criar um dicionário em Python e imprimir seus valores.

A função "printDict" define um dicionário vazio "d" e, em seguida, usa um laço "for" 
para percorrer os números de 1 a 20. 

Para cada número, o quadrado desse número é calculado e adicionado ao dicionário como 
o valor correspondente à chave "i".

Em seguida, outro laço "for" é usado para percorrer as pares chave-valor no dicionário "d". 
Cada par chave-valor é desempacotado nas variáveis "k" e "v", respectivamente, usando a sintaxe " 
for (k, v) in d.items()". Em seguida, o valor "v" é impressa na tela.

Ao final, a função "printDict" é chamada para executar o código e imprimir os valores
 dos quadrados de 1 a 20.
'''

'''O método ".items()" é um método de dicionários em Python que retorna 
uma lista de pares chave-valor presentes no dicionário. 

Cada par chave-valor é representado como uma tupla (chave, valor).

Por exemplo, suponha que você tenha um dicionário "d" com as seguintes chaves e valores:

d = {'key1': 1, 'key2': 2, 'key3': 3}

Se você chamar o método "d.items()", ele retornará uma lista de tuplas, 
onde cada tupla representa uma par chave-valor no dicionário:

[('key1', 1), ('key2', 2), ('key3', 3)]

Esse método é útil para iterar sobre todas as pares chave-valor no dicionário
 e fazer alguma operação com eles. Por exemplo, você pode usar um laço "for" 
 para percorrer a lista retornada pelo método "d.items()" 
 e imprimir cada par chave-valor no dicionário.

Além disso, você também pode desempacotar cada par chave-valor em duas variáveis separadas, 
como mostrado no exemplo acima, para fazer operações mais avançadas com cada par chave-valor.
'''