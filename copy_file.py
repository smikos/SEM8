import shutil
import os

def copy_file():
  number = int(input("Выберит файл, с которым Вы хотите работать\n"
                       "Введите цифру 1 или 2: "))
  while number < 1 or number > 2:
        number = int(input("Ошибка!!!\n"
                           "Введите цифру 1 или 2: "))
      
  if number == 1:
      file1 = r'C:\Users\sasha\Desktop\sem8Py\db\data_1.txt'
      fileA = open(file1, 'rb')
      file2 = r'C:\Users\sasha\Desktop\sem8Py\db\data_2.txt'
      fileB = open(file2,'wb')

      shutil.copyfileobj(fileA,fileB)
      print("удачно!")
  else:
      file1 = r'C:\Users\sasha\Desktop\sem8Py\db\data_2.txt'
      fileA = open(file1, 'rb')
      file2 = r'C:\Users\sasha\Desktop\sem8Py\db\data_1.txt'
      fileB = open(file2,'wb')
      shutil.copyfileobj(fileA,fileB)
  print("удачно!")
