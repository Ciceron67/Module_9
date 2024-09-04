first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(i) for i in first_strings if len(i) > 5]
second_result = [(first_strings[i], second_strings[j]) for i in range(len(first_strings))
                 for j in range(len(second_strings)) if len(first_strings[i]) == len(second_strings[j])]
third_result = [{k: len(k) for k in first_strings + second_strings if len(k) % 2 == 0}]
print(first_result)
print(second_result)
print(third_result)
