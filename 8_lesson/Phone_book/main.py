from os import path

file_base = "base.txt"
all_data = []
id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding = "utf-8") as _:
        pass


def read_records():
    global all_data, id

    with open(file_base) as f:
        all_data = [i.strip() for i in f]
        if all_data:
            id = int(all_data[-1][0])
        
        return all_data


def show_all():
    if not all_data:
        print("Empty date")
    else:
        print(*all_data, sep="\n")

def add_new_contact():
    global id
    array = ['surname:','name:','surname_2:','phone number:']
    string = ''
    for i in array:
        string += input(f"Enter {i} ") + " "
    id += 1
    # print(f'{id} {string}')

    with open(file_base, 'a', encoding = 'utf-8') as f:
        f.write(f'{id} {string}\n')

def search():
    search_param = input("Input search parameter: ")
    flag = False
    for string in all_data:
        string = string.split()
        for s in string:
            if search_param == s:
                print(*string)
                flag = True

    if flag == False:
        print("This contact is not in phone number")

def delete():
    delete_param = input("Input delete parameter: ")
    flag = False
    for string in all_data:
        if delete_param == string[0]:
            f = open(file_base, encoding = "utf-8").read()
            a = f.replace(f'{string}\n', '')
            with open(file_base, 'w', encoding = "utf-8") as f:
                f.write(a)
                flag = True
                print(a)
                break

    if flag == False:
        print("No id for deletion")

def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add new record\n"
                       "3. Search a record\n"
                       "4. Delete record\n"
                       "5. Exit\n")
        match answer:
                case "1":
                    show_all()
                case "2":
                    add_new_contact()
                case "3":
                    search()
                case "4":
                    delete()
                case "5":
                    play = False
                case _:
                    print("Try again!\n")    

main_menu()