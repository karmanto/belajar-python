"""

ini adalah program untuk menampilkan file json dalam terminal. Di bawah ini adalah contoh format file json nya :

[
    {
        "name":"Kategori",
        "childs":[
            {
                "name":"Sub Kategori 1",
                "childs":[
                    {
                        "name":"nama 1"
                    }
                ]
            },
            {
                "name":"Sub Kategori 2",
                "childs":[
                    {
                        "name":"nama 2"
                    }
                ]
            }
        ]
    }
]

untuk menghindari error "RecursionError: maximum recursion depth exceeded while calling a Python object" program ini
memecah fungsi recursive Untuk tiap Object Kategori nya.

"""

import json

data_induk = []
tabspace = "                    "

try:
    with open('json-file-tokopedia-kategori.json') as f:
        data_induk = json.load(f)

except:
    print("")
    print("data not exist")
    print("")
    exit()

if len(data_induk) == 0:
    print("")
    print("data empty")
    print("")
    exit()

print("")

def addressing_recursive(data, list_current_pointer, pointer2):
    if pointer2 >= len(list_current_pointer):
        return data

    else:
        if pointer2 == 0:
            return addressing_recursive(data[list_current_pointer[pointer2]], list_current_pointer, pointer2 + 1)
        else:
            return addressing_recursive(data["childs"][list_current_pointer[pointer2]], list_current_pointer, pointer2 + 1)

def split_data_recursive(data, fisrt_step, last_step):
    if fisrt_step < last_step:
        data_recursive(data, [fisrt_step], [fisrt_step + 1], 1, True)
        fisrt_step += 1
        split_data_recursive(data, fisrt_step, last_step)

def data_recursive(data, list_current_pointer, list_max_pointer, pointer1, firstRunStat):
    if firstRunStat == False:
        last_step = len(data)
        first_step = 0
        split_data_recursive(data, first_step, last_step)

    elif list_current_pointer[pointer1-1] >= list_max_pointer[pointer1-1]:
        list_current_pointer.pop()
        list_max_pointer.pop()
        pointer1 -= 1
        if pointer1 > 0:
            list_current_pointer[pointer1-1] += 1
            data_recursive(data, list_current_pointer, list_max_pointer, pointer1, firstRunStat)

    else:
        data_temp = addressing_recursive(data, list_current_pointer, 0)
        if "name" in data_temp:
            print(tabspace[0:pointer1*2] + data_temp["name"])
        else:
            print(tabspace[0:pointer1*2] + "no name")

        if "childs" in data_temp:
            list_current_pointer.append(0)
            list_max_pointer.append(len(data_temp["childs"]))
            pointer1 += 1
            data_recursive(data, list_current_pointer, list_max_pointer, pointer1, firstRunStat)
        else:
            list_current_pointer[pointer1-1] += 1
            data_recursive(data, list_current_pointer, list_max_pointer, pointer1, firstRunStat)

data_recursive(data_induk, [], [], 1, False)

print("")