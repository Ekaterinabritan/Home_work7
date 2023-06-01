#Задача №1
poem = input('введите стихотворение: ')
st = poem.lower().split()
vowels_letter = lambda x: sum(1 for i in x if i in 'а')
phrase = vowels_letter(st[0])
if all([vowels_letter(i) == phrase for i in st]):
    print('Парам пам-пам')
else:
    print('Пам парам')

#Задача №2
def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        decision = []
        for j in range(1, num_columns + 1):
            decision.append(str(operation(i, j)))
        print("     ".join(decision))

print_operation_table(lambda x, y: x * y)