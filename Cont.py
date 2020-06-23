import Planet
import os

class Cont:

    def __init__(self):
        self.list = list()
    
    def create_list(self, f):
        i = 0
        line = 0
        for line in f:
            #line
            self.list.append(Planet.Planet())
            self.list[i].read(line)
            i += 1

    def delete_smth(self):
        val = str(input("number you want to delete:\t"))
        if int(val) > 0 and int(val) < len(self.list):
            del self.list[int(val)]

    def sort_by_name(self):
        self.list.sort( key = lambda x:(x.name.lower()))
        
    def sort_by_distance(self):
        self.list.sort( key = lambda x:(x.distance.lower()))

    def sort_by_diameter(self):
        self.list.sort( key = lambda x:(x.diameter))

    def sort_by_weight(self):
        self.list.sort( key = lambda x:(x.weight))

    def find_obj(self, word):
        m = 0
        for i in range(len(self.list)):
            if word.lower() in self.list[i].name.lower():
                self.list[i].to_print()
                m += 1
            elif word.lower() in self.list[i].distance.lower():
                self.list[i].to_print()
                m += 1
            elif word.lower() in self.list[i].description.lower():
                self.list[i].to_print()
                m += 1
        print()

    def print_all(self):
        print("\n")
        
        for i in range(len(self.list)):
            print(str(self.list[i]))
        print("\n")
    
    #def remove_smth(self, val):
    #    for i in self.list:
    #        if str(i).find(val) != -1:
    #            try:
    #                self.list.remove(self.list[i])
    #            except ValueError:
    #                print("Smth wrong...")

    def edit_smth(self, index, val, new_val):
        index = int(index)
        if index >= len(self.list) or index < 0:
            index = str(input("wrong index, once more: "))
        elif val == "name":
            self.list[index].name = Planet.Planet().if_word(new_val)
        elif val == "distance":
            self.list[index].distance = Planet.Planet().if_number(new_val)
        elif val == "diameter":
            self.list[index].diameter = Planet.Planet().if_number(new_val)
        elif val == "weight":
            self.list[index].weight = Planet.Planet().if_number(new_val)
        else:
            print("somthing wrong...")

class File:

    def __init__(self, name:str):
          self.name = name

    def file(self):
        def file_exist():
            if os.path.exists(self.name) and os.path.getsize(self.name) > 0:
                return True
            else:
                return False
        while file_exist() == False:
            f = str(input(" Opsss... Input new name of file  "))
        return self.name
  


