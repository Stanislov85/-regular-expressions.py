# from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list

import re
import csv

Pattern = '(8|\+7)?\s*(\(*)(\d{3})(\)*)(\s*|-)(\d{3})(\s*|-)(\d{2})(\s*|-)(\d{2})\s*(\(*)(\w\w\w\.)*\s*(\d{4})*(\))*'
Substitution = r'+7(\3)\6-\8-\10 \12'

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# контакт лист
contacts_list_new = []
for contact in contacts_list:
    new_contact = []
    full_name = ",".join(contact[:3])
    full_name_list = re.findall(r'(\w+)', full_name)
    while len(full_name_list) < 3:
        full_name_list.append('')
    new_contact += full_name_list
    new_contact.append(contact[3])
    new_contact.append(contact[4])
    phone_pattern = re.compile(Pattern)
    changed_phone = phone_pattern.sub(Substitution, contact[5])
    new_contact.append(changed_phone)
    new_contact.append(contact[6])
    contacts_list_new.append(new_contact)
# pprint(new_contacts_list)


#удаление дубликатов
phone_book = {}
for contact in contacts_list_new:
    if contact[0] in phone_book:
        contact_value = phone_book[contact[0]]
        for i in range(len(contact_value)):
            if contact[i]:
                contact_value[i] = contact[i]
    else:
        phone_book[contact[0]] = contact
contact_book_values = list(phone_book.values())
# pprint(contact_book_values)


with open("phonebook.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerows(contact_book_values)