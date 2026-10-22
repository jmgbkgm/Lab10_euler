import math

def add_vectors(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Векторы должны быть одинаковой размерности!")
    return [a + b for a, b in zip(v1, v2)]

def vector_length(v):
    return math.sqrt(sum(x**2 for x in v))

def main():
    print("1. Ввод с консоли")
    print("2. Ввод из файла")
    choice = input("Выберите способ ввода (1 или 2): ")

    try:
        if choice == '1':
            n = int(input("Введите размерность векторов (N): "))
            v1 = list(map(float, input(f"Введите {n} координат первого вектора через пробел: ").split()))
            v2 = list(map(float, input(f"Введите {n} координат второго вектора через пробел: ").split()))
        elif choice == '2':
            filename = input("Введите путь к файлу (например, input.txt): ")
            with open(filename, 'r') as f:
                lines = f.read().splitlines()
                v1 = list(map(float, lines[0].split()))
                v2 = list(map(float, lines[1].split()))
        else:
            print("Неверный выбор.")
            return

        res = add_vectors(v1, v2)
        length = vector_length(res)

        print(f"\nРезультат сложения (координаты): {res}")
        print(f"Длина вектора: {length:.4f}")

        # Вывод в файл (по желанию)
        save = input("\nСохранить результат в файл? (y/n): ")
        if save.lower() == 'y':
            with open('result.txt', 'w') as f:
                f.write(f"Координаты: {res}\nДлина: {length:.4f}\n")
            print("Результат сохранен в result.txt")

    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
