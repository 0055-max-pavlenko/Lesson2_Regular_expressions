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

#Приводим номера телефонов к нужному формату

for i in range(len(contacts_list)):
    pattern = r"(8|\+7)(\s|\()*(\d{3})(\)*)(\s|-)*(\d{3})(\s|-)*(\d{2})(\s|-)*(\d{2})(\s)*(\s|\()*(доб.)*(\s)*(\d+)*(\))*"
    substitution = r"+7(\3)\6-\8-\10 \13\15"
    contacts_list[i]['phone'] = re.sub(pattern, substitution, contacts_list[i]['phone'])

    

#Объединяем данные для людей с совпадающими Фамилией и Именем
contacts_list = sorted(contacts_list, key = lambda x:(x['lastname'], x['firstname']))
current_person = 0
total_persons = len(contacts_list)-1

while current_person < total_persons:
    if (contacts_list[current_person]['lastname'] == contacts_list[current_person+1]['lastname']) and (contacts_list[current_person]['firstname'] == contacts_list[current_person+1]['firstname']):
        if contacts_list[current_person]['surname'] != contacts_list[current_person+1]['surname']:
            contacts_list[current_person]['surname'] += contacts_list[current_person+1]['surname']

        if contacts_list[current_person]['organization'] != contacts_list[current_person+1]['organization']:
            contacts_list[current_person]['organization'] += contacts_list[current_person+1]['organization']
            
        if contacts_list[current_person]['position'] != contacts_list[current_person+1]['position']:
            contacts_list[current_person]['position'] += contacts_list[current_person+1]['position']
            
        if contacts_list[current_person]['phone'] != contacts_list[current_person+1]['phone']:
            contacts_list[current_person]['phone'] += contacts_list[current_person+1]['phone']
           
        if contacts_list[current_person]['email'] != contacts_list[current_person+1]['email']:
            contacts_list[current_person]['email'] += contacts_list[current_person+1]['email']
            
        contacts_list.remove(contacts_list[current_person+1])
        total_persons -=1
    else:
        current_person +=1


## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
columns = ['lastname','firstname','surname','organization','position','phone','email']
with open("phonebook.csv", "w", encoding = 'utf-8', newline='') as f:
 datawriter = csv.DictWriter(f, fieldnames=columns, delimiter=',')
 datawriter.writeheader()
 datawriter.writerows(contacts_list)
  

