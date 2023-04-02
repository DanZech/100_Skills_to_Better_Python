values = input("Enter comma-separed numbers: ")
l = values.split(",")
t = tuple(l)
print(l)
print(t)
print(type(l), type(t))

'''Este é um exemplo de como ler valores separados por vírgulas como entrada do usuário
e convertê-los em uma lista e em um tuple em Python.

A primeira linha usa a função "input" para solicitar ao usuário
 que entre com uma sequência de números separados por vírgulas. 
 
 A entrada do usuário é armazenada na variável "values".

Na segunda linha, a função "split" é usada para dividir a string "values"
com base na vírgula e retornar uma lista de strings. 

Essa lista é armazenada na variável "l".

Na terceira linha, a função "tuple" é usada para converter a lista "l" em um tuple. 

O tuple é armazenado na variável "t".

Por fim, as variáveis "l" e "t" são impressas na tela, juntamente com o tipo de cada uma delas (lista ou tuple). 
Isso permite verificar se as conversões foram feitas corretamente.'''