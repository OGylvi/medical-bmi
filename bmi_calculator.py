def calculate_bmi(weight, height):
    """
    Функция для расчета индекса массы тела (BMI).

    :param weight: масса тела в кг
    :param height: рост в метрах
    :return: индекс массы тела
    """
    return weight / (height ** 2)


if __name__ == "__main__":
    print("Программа для расчета индекса массы тела (BMI)")
    weight = float(input("Введите массу тела (кг): "))
    height = float(input("Введите рост (м): "))

    bmi = calculate_bmi(weight, height)

    print(f"Ваш индекс массы тела: {bmi:.2f}")

    if bmi < 18.5:
        print("Недостаточная масса тела (дефицит)")
    elif 18.5 <= bmi < 24.9:
        print("Норма")
    elif 25 <= bmi < 29.9:
        print("Избыточная масса тела")
    else:
        print("Ожирение")
