import csv
import re
from Task_1 import logger


with open("phonebook_raw.csv", encoding="UTF-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


@logger
def split_data():
    book = []
    for info in contacts_list:
        split_list = " ".join(info[:3]).split(" ")
        book.append([split_list[0], split_list[1], split_list[2], info[3], info[4], info[5], info[6]])
    return book


@logger
def phone_changer():
    data = split_data()
    pattern = r"(\+7|8|7)?\s*\(?(\d{3})\)?\s*[-]?(\d{3})[-]?(\d{2})[-]?(\d{2})\s*\(?(\w+\.?)?\s*(\d+)?\)?"
    subst = r"+7(\2)\3-\4-\5 \6\7"
    for info in data:
        new_phones = re.sub(pattern, subst, info[5])
        info[5] = new_phones
    return data


@logger
def duplicates_remover():
    data = phone_changer()
    new_list = []
    for info in data:
        surname = info[0]
        name = info[1]
        for new_info in data:
            new_surname = new_info[0]
            new_name = new_info[1]
            if surname == new_surname and name == new_name:
                if info[2] == '':
                    info[2] = new_info[2]
                if info[3] == '':
                    info[3] = new_info[3]
                if info[4] == '':
                    info[4] = new_info[4]
                if info[5] == '':
                    info[5] = new_info[5]
                if info[6] == '':
                    info[6] = new_info[6]
        if info not in new_list:
            new_list.append(info)
    return new_list


with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    new_list = duplicates_remover()
    datawriter.writerows(new_list)
