import pytest
from vector_calc import add_vectors, vector_length

def test_add_vectors_correct():
    # Тест 1: Обычное сложение
    v1 = [1.0, 2.0, 3.0]
    v2 = [4.0, 5.0, 6.0]
    expected = [5.0, 7.0, 9.0]
    assert add_vectors(v1, v2) == expected

def test_add_vectors_zero():
    # Тест 2: Сложение с нулевым вектором
    v1 = [0.0, 0.0]
    v2 = [1.5, -2.5]
    expected = [1.5, -2.5]
    assert add_vectors(v1, v2) == expected

def test_add_vectors_different_size():
    # Тест 3: Проверка на ошибку при разной размерности
    v1 = [1.0, 2.0]
    v2 = [1.0, 2.0, 3.0]
    with pytest.raises(ValueError):
        add_vectors(v1, v2)

def test_vector_length():
    # Тест 4: Проверка длины вектора (египетский треугольник 3-4-5)
    v = [3.0, 4.0]
    assert vector_length(v) == 5.0

def test_vector_length_1d():
    # Тест 5: Длина одномерного вектора
    v = [-5.0]
    assert vector_length(v) == 5.0
