value = input()
numbers = [str(int(x)**2) for x in value.split(',') if (int(x)%2!=0)]
print(numbers)
print(','.join(numbers))

'''
Este é um exemplo de como ler uma sequência de números separados por vírgulas como entrada do usuário, calcular o quadrado de cada número ímpar e retornar os resultados como uma string separada por vírgulas.

A primeira linha usa a função "input" para solicitar a entrada do usuário, que consiste em uma sequência de números separados por vírgulas. A entrada do usuário é armazenada na variável "value".

Na segunda linha, um compreensão de lista é usada para calcular o quadrado de cada número ímpar na sequência. A função "split" é usada para dividir a string "value" em uma lista de strings, cada uma representando um número. A compreensão de lista percorre a lista e usa a função "int" para converter cada string em um número inteiro. Em seguida, usa-se o operador de módulo ("%") para verificar se o número é ímpar. Se for, o quadrado desse número é calculado usando "int(x) ** 2". Todos os resultados são adicionados à lista "numbers".

Na terceira linha, a função "join" é usada para juntar todos os elementos da lista "numbers" em uma única string, separados por vírgulas. A string resultante é impressa na tela. Isso exibe todos os quadrados de números ímpares encontrados na sequência de entrada do usuário, separados por vírgulas.'''