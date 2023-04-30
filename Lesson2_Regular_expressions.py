from pprint import pprint
import re
import csv

## Читаем адресную книгу в формате CSV в список contacts_list:
with open("phonebook_raw.csv", encoding = 'utf-8') as f:
  rows = csv.DictReader(f, delimiter=",")
  contacts_list = list(rows)
  
# Если в данных больше разделителя запятой чем нужно удаляем лишние записи
for item in contacts_list:
    try:
        del item[None]
    except:
        pass



## 1. Выполните пункты 1-3 задания.
## Исправляем структуру данных ФИО
for i in range(len(contacts_list)):
    lastname_items = re.findall(r"\w+", contacts_list[i]['lastname'])
    firstname_items = re.findall(r"\w+", contacts_list[i]['firstname'])
    


    if len(lastname_items) != 1:
        contacts_list[i]['lastname'] = lastname_items[0]
        contacts_list[i]['firstname'] = lastname_items[1]
        try:
            contacts_list[i]['surname'] = lastname_items[2]
        except:
            pass
       

    if len(firstname_items) == 2:
        contacts_list[i]['firstname'] = firstname_items[0]
        contacts_list[i]['surname'] = firstname_items[1] 




## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
columns = ['lastname','firstname','surname','organization','position','phone','email']
with open("phonebook.csv", "w", encoding = 'utf-8', newline='') as f:
 datawriter = csv.DictWriter(f, fieldnames=columns, delimiter=',')
 datawriter.writeheader()
 datawriter.writerows(contacts_list)
  
## Вместо contacts_list подставьте свой список:
  #datawriter.writerows(contacts_list)
