def multiply():
    numbers = [1, 2, 3, 4, 5]
    result = 0

    for number in numbers:
        result *= numbers[number]

    return result


# numbers tem o input variável. Complexidade de tempo: 0(n)
# result esta em apenas 1 espaço de memória. Complexidade de espeço: 0(1)
