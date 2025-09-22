
import pytest
import sys
sys.path.append(".")
from app_funcs import soma, subtracao, multiplicacao, divisao, saudacao


def test_soma():
    assert soma(2, 3) == 5

def test_subtracao():
    assert subtracao(10, 4) == 6

def test_multiplicacao():
    assert multiplicacao(3, 5) == 15

def test_divisao_normal():
    assert divisao(10, 2) == 5

def test_divisao_erro_zero():
    with pytest.raises(ValueError):
        divisao(5, 0)

def test_saudacao():
    assert saudacao("Rui") == "Olá, Rui!"
