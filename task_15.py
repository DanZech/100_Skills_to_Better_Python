class Circle(object):
    def __init__(self, r):
        self.radius = r
    
    def area(self):
        return (self.radius**2)*3.14

aCircle = Circle(2)
print(aCircle.area())

'''
Este é um programa Python que define uma classe chamada Circle que representa um círculo. 
A classe tem um construtor __init__() que recebe um parâmetro r, 
que representa o raio do círculo. 

O construtor inicializa uma variável de instância radius com o valor do parâmetro r.

A classe também possui um método area(), 
que calcula e retorna a área do círculo usando a fórmula A = πr^2. 

O método usa a variável de instância radius para realizar o cálculo.

Em seguida, o programa cria uma instância da classe Circle com um raio de 2, 
chamada aCircle. O programa chama o método area() da instância aCircle e imprime o resultado.

A saída do programa será o valor da área do círculo com raio 2, 
calculado usando a fórmula A = πr^2. O valor será aproximadamente 12.56, 
já que a constante π é aproximadamente igual a 3.14.
'''