from delete_data import delete_row
from change_data import change_row
from add_data import add_row
from print_data import print_file


def check_number(n):
     while command <1 or command >5:
            command=int(input("Ошибка,такого номера команды "
                       "не сущуствует! Введите цифру от 1 до 5\n"       
                      "Выберите файл: \n"
                      "1.Добавить \n"
                      "2.Удалить \n"
                      "3.Изменить\n"
                      "4.Вывод\n"
                      "5.Выход\n"))


def start_menu():
    command=int(input("Доброго времени суток\n"
                      "Выберите файл: \n"
                      "1.Добавить \n"
                      "2.Удалить \n"
                      "3.Изменить\n"
                      "4.Вывод\n"
                      "5.Выход\n"))
   
    
    while command !=5:
        if command ==1:
             add_row()
        elif command ==2:
             delete_row()
        elif command ==3:
             change_row()
        elif command ==4:
             print_file()
        
        pass
