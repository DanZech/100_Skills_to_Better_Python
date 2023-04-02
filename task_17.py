li = [2,4,6,8]
for i in li:
    assert i % 2 == 0

'''
Esse código verifica se todos os elementos da lista "li" 
são divisíveis por 2, ou seja, se são números pares.

A declaração "assert" é usada para verificar uma condição e, 
se a condição for falsa, gera uma exceção "AssertionError".

Neste caso, se algum número da lista "li" não for par, 
o "assert" irá falhar e o programa lançará uma exceção, 
interrompendo sua execução. Caso contrário, se todos os números forem pares, 
a execução do programa continuará normalmente.
'''