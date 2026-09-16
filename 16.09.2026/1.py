#написать програму которая
#ввести с клавиатуры заметку, сохраняем для просмотра
#можем удалять заметки
#пользователь может просматривать заметки
#удаляем все заметки
def dobavit():
    zametka = input('Введите заметку')
    mas.append(zametka)
    print(f'вот такая {zametka} заметка добавлена')

def delit():
    n = int(input('Введите индекс заметки которую хотите удалить'))
    print('вы действительно хотите удалить заметку?')
    variant = input('Если да введите Yes, если нет введите No')
    if variant == 'Yes':
        print('заметка ' + mas[n-1] + ' удалена')
        mas.remove(mas[n-1])
    if variant == 'No':
        print(f"ничего не удалено {mas}")

def printt():
    if mas == []:
        print('У вас нет заметок')
    if mas != []:
        print('у вас есть такие заметки')
        for i in mas:
            print(i)

def delite_all():
    variant = input('Если да введите Yes, если нет введите No')
    if variant == 'Yes':
        mas = []
        print('вы удалили все заметки')
    if variant == 'No':
        print(f"ничего не удалено {mas}")


mas = []
while True:
    numer_deistvia = int(input('Введите\n 1 если хотите добавить заметку\n 2 если удалить заметку\n 3 елси просмотреть заметки\n 4 если удалить все заметки'))
    if numer_deistvia == 1:
        dobavit()
    if numer_deistvia == 2:
        delit()
    if numer_deistvia == 3:
        printt()
    if numer_deistvia == 4:
        delite_all()


# zametka = input('Введите заметку')
# print(f'вот такая {zametka} заметка добавлена')
# print('вот такая' + zametka + 'заметка добавлена')


# mas = [1,2,3,4,5]
# mas.remove(mas[4])
# print(mas)
# mas.remove(2)
# print(mas)



