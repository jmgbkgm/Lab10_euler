import math
import matplotlib.pyplot as plt
import numpy as np
from sympy import isprime, factorint

class EulerSequence:
    def __init__(self):
        # Кэш для мемоизации (оптимизации вычислений)
        self._cache = {1: 1}

    def euler_sequence_optimized(self, n: int) -> int:
        """Оптимизированное вычисление E(n) с использованием рекуррентной формулы и кэша."""
        if n < 1:
            raise ValueError("n должно быть больше или равно 1")
        if n in self._cache:
            return self._cache[n]
        
        # E(n) = n * E(n-1) + (n-1)!
        e_n_minus_1 = self.euler_sequence_optimized(n - 1)
        result = n * e_n_minus_1 + math.factorial(n - 1)
        
        self._cache[n] = result
        return result

    def generate_euler_sequence(self, limit: int) -> list:
        """Генерация последовательности до limit."""
        return [self.euler_sequence_optimized(i) for i in range(1, limit + 1)]

    def find_euler_number(self, target: int, max_search: int = 100) -> int:
        """Поиск позиции (n) числа в последовательности."""
        for i in range(1, max_search + 1):
            if self.euler_sequence_optimized(i) == target:
                return i
        return -1

    def find_euler_numbers_in_range(self, start: int, end: int, max_search: int = 20) -> list:
        """Поиск чисел Эйлера в заданном диапазоне."""
        results = []
        for i in range(1, max_search + 1):
            val = self.euler_sequence_optimized(i)
            if start <= val <= end:
                results.append((i, val))
        return results

    def analyze_euler_properties(self, n: int) -> dict:
        """Анализ свойств числа E(n)."""
        e_num = self.euler_sequence_optimized(n)
        
        # Вычисление цифрового корня
        digital_root = 0
        temp = e_num
        while temp > 0:
            digital_root += temp % 10
            temp //= 10
            if digital_root > 9 and temp == 0:
                temp = digital_root
                digital_root = 0

        return {
            'n': n,
            'euler_number': e_num,
            'is_prime': isprime(e_num),
            'digital_root': digital_root,
            'factors': factorint(e_num) if e_num < 10**10 else "Слишком большое число для быстрой факторизации"
        }

    def euler_totient(self, n: int) -> int:
        """Вычисление функции Эйлера φ(n)."""
        if n == 0: return 0
        result = n
        p = 2
        temp_n = n
        while p * p <= temp_n:
            if temp_n % p == 0:
                while temp_n % p == 0:
                    temp_n //= p
                result -= result // p
            p += 1
        if temp_n > 1:
            result -= result // temp_n
        return result

    def euler_totient_sequence(self, limit: int) -> list:
        """Последовательность функции Эйлера φ(n)."""
        return [self.euler_totient(i) for i in range(1, limit + 1)]

    def find_perfect_numbers(self, limit: int) -> list:
        """Поиск совершенных чисел."""
        perfect_nums = []
        for i in range(2, limit + 1):
            divisors_sum = sum([j for j in range(1, i) if i % j == 0])
            if divisors_sum == i:
                perfect_nums.append(i)
        return perfect_nums

    def plot_euler_sequence(self, limit: int, save_path: str = None):
        """Визуализация последовательности Эйлера."""
        seq = self.generate_euler_sequence(limit)
        n_vals = list(range(1, limit + 1))
        
        fig, axes = plt.subplots(2, 2, figsize=(12, 8))
        
        # Основной график
        axes[0, 0].plot(n_vals, seq, marker='o', color='b')
        axes[0, 0].set_title('Последовательность Эйлера')
        axes[0, 0].set_xlabel('n')
        axes[0, 0].set_ylabel('E(n)')
        
        # Логарифмический масштаб
        axes[0, 1].semilogy(n_vals, seq, marker='s', color='g')
        axes[0, 1].set_title('Логарифмический масштаб')
        
        # Отношение E(n) / n!
        ratio = [seq[i] / math.factorial(n_vals[i]) for i in range(len(seq))]
        axes[1, 0].plot(n_vals, ratio,
