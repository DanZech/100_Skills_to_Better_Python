import functools

def f(x): return x % 2 != 0 and x % 3 != 0
list(filter(f, range(2, 25)))

def cube(x): return x*x*x
list(map(cube, range(1, 11)))

def add(x, y): return x + y
functools.reduce(add, range(1, 11))

'''
A primeira função, "f(x)", recebe um número inteiro "x" como entrada e retorna "True" 
se o número não for divisível por 2 nem por 3. A função é usada como argumento para a função "filter()", 
que filtra os elementos de um iterável (no caso, a sequência de números de 2 a 24) 
de acordo com a função "f(x)". 

O resultado é uma lista dos números que satisfazem a condição definida na função "f(x)".

A segunda função, "cube(x)", recebe um número inteiro "x" como entrada e retorna o cubo desse número. 
A função é usada como argumento para a função "map()", que aplica a função "cube(x)" 
a cada elemento da sequência de números de 1 a 10. O resultado é uma lista dos cubos desses números.

A terceira função, "add(x, y)", recebe dois números "x" e "y" como entrada e retorna a soma desses números.
A função é usada como argumento para a função "functools.reduce()", que aplica a função "add(x, y)" 
aos elementos da sequência de números de 1 a 10, de forma que os elementos são reduzidos a um único valor,
que é a soma total desses elementos. O resultado é o valor 55, que é a soma de todos os números de 1 a 10.
'''