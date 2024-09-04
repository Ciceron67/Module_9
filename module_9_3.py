first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = [len(i) - len(j) for i, j in zip(first, second) if len(i) != len(j)]
second_result = [(len(first[i]) == len(second[i])) for i in range(min(len(first), len(second)))]
print(first_result)
print(second_result)
