""" Sum of Integers Up To n
    Write a function, add_it_up, which returns the sum of the integers from 0
    to the single integer input parameter.

    The function should return 0 if a non-integer is passed in.
"""


def add_it_up(n):
    if not isinstance(n, int):
        return 0
    elif n <= 0:
        return 0

    soma = 0
    for i in range(n + 1):
        soma += i
    return soma


def test_somar_numeros_positivos():
    assert add_it_up(5) == 15


def test_somar_numeros_negativos():
    assert add_it_up(-5) == 0
    # assert add_it_up(-5) == "Input deve ser um número não negativo."


def test_input_nao_inteiro():
    assert add_it_up("ciana") == 0


def test_somar_numeros_ate_zero():
    assert add_it_up(0) == 0