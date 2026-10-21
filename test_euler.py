import unittest
from euler_sequence import EulerSequence
import time

class TestEulerSequence(unittest.TestCase):
    def setUp(self):
        self.euler = EulerSequence()

    def test_base_values(self):
        """Проверка базовых значений (первые 10 чисел)"""
        expected = [1, 3, 11, 50, 274, 1764, 13068, 109584, 1026576, 10628640]
        for i, val in enumerate(expected, 1):
            self.assertEqual(self.euler.euler_sequence_optimized(i), val)

    def test_euler_totient(self):
        """Проверка функции Эйлера φ(n)"""
        self.assertEqual(self.euler.euler_totient(10), 4)
        self.assertEqual(self.euler.euler_totient(1), 1)
        self.assertEqual(self.euler.euler_totient(7), 6)

    def test_generate_sequence(self):
        """Проверка генерации последовательности"""
        seq = self.euler.generate_euler_sequence(5)
        self.assertEqual(len(seq), 5)
        self.assertEqual(seq[-1], 274)

    def test_find_number(self):
        """Проверка поиска числа"""
        self.assertEqual(self.euler.find_euler_number(274), 5)
        self.assertEqual(self.euler.find_euler_number(9999), -1)

    def test_perfect_numbers(self):
        """Проверка поиска совершенных чисел"""
        self.assertEqual(self.euler.find_perfect_numbers(1000), [6, 28, 496])

    def test_performance_and_caching(self):
        """Проверка производительности и кэширования"""
        start_time = time.time()
        self.euler.euler_sequence_optimized(50)
        end_time = time.time()
        self.assertLess(end_time - start_time, 0.1) # Вычисление E(50) должно быть быстрым

if __name__ == '__main__':
    unittest.main()
