import random 

min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices..")
    print("the values are ...")
    print(random.randint(min, max)) 
    print(random.randint(min, max))
    roll_again = input("roll the dices again?")

'''
Este é um exemplo de um jogo de dados simulado em Python.

A primeira linha importa a biblioteca "random", que fornece funções para gerar números aleatórios. 
Em seguida, as variáveis "min" e "max" são definidas como 1 e 6, respectivamente. 
Essas variáveis representam o intervalo de valores que o dado pode ter (neste caso, de 1 a 6).

A seguir, a variável "roll_again" é inicializada com "yes". 
Isso é usado como um controle de loop para verificar se o usuário deseja rolar os dados novamente.

O loop "while" então verifica se "roll_again" é igual a "yes" ou "y". 
Enquanto for verdadeiro, o loop será executado.

Dentro do loop, a mensagem "Rolling the dices.." é impressa na tela, seguida pela mensagem "the values are...". 
Em seguida, a função "random.randint" é chamada duas vezes para gerar dois números aleatórios dentro
 do intervalo especificado por "min" e "max". 
Esses números são então impressos na tela como os valores dos dados.

Por fim, o usuário é perguntado se deseja rolar os dados novamente,
e a resposta é armazenada na variável "roll_again". Se "roll_again" continuar sendo "yes" ou "y", 
o loop será executado novamente. Caso contrário, o loop será interrompido e o programa terminará.
'''