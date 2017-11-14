# -*- coding: utf-8 -*-
""" Repaso interactivo de python
"""

def lower_up(lower,upper):
	""" 1: Returns a list of numbers from the lower number to the upper number:
	>>>lower_up(5,15)
    5
    6
    7
    8
    9
    10
	11
	12
	13
	14
	15
	"""

def all_the_args(*args, **kwargs):

	""" 2: Return an array. Use * to expand positional args and use ** to expand keyword args

	>>>all_the_args(1, 2, a=3, b=4)
    (1, 2)
    {"a": 3, "b": 4}
	"""

def may_20 (tup):
	""" 3: Definir una tupla con 10 números. Imprimir la cantidad de números superiores a 20.
	
	>>>may_20(10, 16, 22, 26, 27, 30)
	22, 26, 27, 30

	"""

def word_filter(list_of_words, n):
    """ 4: Filtra las palabras que contienen más de n caracteres.

    >>>word_filter([hello, bye, computer, software, python], 5)
   [computer, software, python]

	"""

def string_length(list):
	""" 5: imprime el largo de una cadena de caracteres

	>>>string_length("popularity")
	10
	"""

def is_vocal(x):
	""" 6: Determines if it is vocal

	>>>is_vocal(a)
	True
	>>>is_vocal(b)
	False
	"""

def is_leap_year(year):
	""" 7: Determines if a year is a leap year.

	>>>is_leap_year(2016)
	True
	"""

def has_uppercase(word):
	""" 8: Evaluate if a word has uppercase letters

	>>>has_uppercase(MayuSculA)
	3
	"""

def contar_vocales(cadena):
	""" 9: Return number of vocales in a word.

	>>>contar_vocales(murcielago)
 	5
 	"""


def square(list):  
    """ 10: Calculate the square of the numbers in a list 

    >>> l = [0, 1, 2, 3] 
    >>> square(l) 
    [0, 1, 4, 9] 
    """ 

def is_prime(n):
    """ 11:  Return if n is prime.
    
    >>>is_prime(5)
    True
    >>>is_prime(6)
    False
    """

def factorial(n):
    """ 12: Return the factorial of n, an exact integer >= 0.
    If the result is small enough to fit in an int, return an int.
    Else return a long.

    >>>[factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>>[factorial(long(n)) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>>factorial(30)
    265252859812191058636308480000000L
    """

def to_roman(n):
    """ 13: Convert number integer to Roman numeral

    >>>to_roman(598)
    [DXCVIII]
    """

def rima(word1, word2):
	""" 14: Indica si dos palabrar riman. Si coinciden las 3 ultimas letras rima, 
	si ncoinciden solo 2 rima un poco, si coincide solo 1 no rima.

	>>>rima(flor, coliflor)
	rima
	>>>rima(amar, plantar)
	rima un poco.
	>>>rima(azucar, barrer)
	no rima
	"""

def capital(pesos, interes, anios):
	""" 15: Pide una cantidad de pesos, una tasa de interés y un numero de años. Muestra en cuanto se habrá convertido el 
	capital inicial transcurridos esos años si cada año se aplica la tasa de interés introducida.

	>>>capital(10000, 4.5, 20)
	24117.14
	"""





