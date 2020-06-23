
import Planet
import Cont
import operator
import os

name = str(input("naame:"))
name += ".txt"

name_of_file = Cont.File(name)
file2 = name_of_file.file()
f = open(file2)
l = Cont.Cont()
r = Planet.Planet()
l.create_list(f)
i = 0
    

act = 1
while act != 0:
    print(" 1 - print ")
    print(" 21 - sort by name")
    print(" 22 - sort by distance")
    print(" 23 - sort by diameter")
    print(" 24 - sort by traveller")
    print(" 25 - sort by weight")
    print(" 3 - find")
    print(" 4 - delete")
    print(" 5 - input new")
    print(" 6 - remove")
    print(" 7 - edit")
    print(" 0 \t exit")
    act = int(input(""))
    
    if(act == 1):
        l.print_all()
        print()
        
    elif(act == 21):
        l.sort_by_name()
        l.print_all()   

    elif(act == 22):
        l.sort_by_distance()
        l.print_all()

    elif(act == 23):
        l.sort_by_diameter()
        l.print_all()

    elif(act == 25):
        l.sort_by_weight()
        l.print_all()

    elif act == 3:
        name = str(input("input data for searching "))
        l.find_obj(name)

    elif act == 4:
        l.delete_smth()
        l.print_all()

    elif act == 5:
        l.create_list(Planet.Planet().input_new())
        l.print_all()

    #elif act == 6:
    #    val = sorted(input("what you want to remove:"))
    #    l.remove_smth(val)
    #    l.print_all()

    elif act == 7:
        index = str(input("index of elem, you want to change:  "))
        val = str(input("what you want to change:  "))
        new_val = str(input("your new value:  "))
        l.edit_smth(index, val, new_val)
        l.print_all()

    elif(act == 0):
        break

    else:
        print("incorrect number")
        continue

