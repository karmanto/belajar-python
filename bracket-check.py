"""
Ini adalah program Check Bracket dari sebuah string.
Program berjalan dengan membaca input dari user.
Jika urutan bracket open-close tag tidak sesuai maka outputnya akan "false", dan jika sebaliknya maka outputnya akan "true".

Perhatikan contoh di bawah :

"{}()[itachi is the most wanted (shinobi ever)][]" --> outputnya "true"
"L beat kira { [ --- with tv broadcast + in Kanto Japan]" --> outputnya "false"
"{black frieza can easily beat{...[8x]} beerus}" --> outputnya "true"
"""

bracket_open = ["(","{","["]
bracket_close = [")","}","]"]
list_of_pointer = []

print("")
print("masukkan input")
input_key = input()
output = True

for x in input_key:
    if x in bracket_close and len(list_of_pointer) > 0:
        last_pointer = list_of_pointer.pop()
        index = bracket_close.index(x)
        if last_pointer != index:
            output = False
            break
        elif last_pointer == index and len(list_of_pointer) == 0:
            output = True
    elif x in bracket_close and len(list_of_pointer) <= 0:
        output = False
        break
    elif x in bracket_open:
        index = bracket_open.index(x)
        list_of_pointer.append(index)
        output = False

print("output " + str(output))   
print("")

exit()