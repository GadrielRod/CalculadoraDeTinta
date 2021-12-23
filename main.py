from calculadora import Calculadora
from comodo import Comodo

calc = Calculadora()

comodo = Comodo(
    input('Qual a largura do cômodo? '),
    input('Qual a profundidade do cômodo? ')
)

# calc.area_paredes = 2 * (largura + profundidade) * altura

print( 
    'A area das paredes é: ', calc.calcular_area_paredes(
        comodo
        )
)

print(
    'A area da teto é: ', calc.calcular_area_teto(
        comodo
        )
)

print(
    'A litragem de tinta necessaria é: ', calc.calcular_litragem_necessaria()
)