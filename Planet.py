

class Planet:
    
    def __init__(self, name = "none", distance = 10, description = "none", diameter = 0, weight = 0):
        self.name = name
        self.distance = distance
        self.description = description
        self.diameter = diameter
        self.weight = weight
       
    def get_name(self):
        return self.name
    
    def get_distance(self):
        return self.distance

    def get_description(self):
        return self.description
    
    def get_diameter(self):
        return self.diameter

    def get_weight(self):
        return self.weight

    def __str__(self):
        text = " "
        text += self.name 
        text += "\t"
        text += self.distance
        text += "\t"
        text += self.description
        text += "\t"
        text += str(self.diameter)
        text += "\t"
        text += str(self.weight)
        text += "\t"
        return text

    def if_word(self, value):
        while value.isalpha() == False:
            value = str(input("Opss... Input your value once more: "))
        return value
    
    def isfloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def if_weight(self, value):
        while self.isfloat(value) == False or value[0] == "-" or self.weight < 0 or self.weight > 120000000:
            value = str(input("Opss... Input your value once more weight: "))
        return value
    
    def if_number(self, value):
        while self.isfloat(value) == False or value[0] == "-":
            value = str(input("Opss... Input your value once more diameter: "))
        return float(value)
    
    def read(self, line):
        a = line.split()
        self.name = self.if_word(a[0])
        self.distance = self.if_number(a[1])
        self.description = self.if_word(a[3])
        self.diameter = self.if_number(a[5])
        self.weight = self.if_number(a[1])

    def to_print(self):
        print(self.name, self.distance, self.description, self.diameter, self.weight)

    def input_new(self):
        self.name = self.if_word(str(input("New name: ")))
        self.distance = self.if_number(str(input("New distance: ")))
        self.description = self.if_word(str(input("New description:")))
        self.diameter = self.if_number(str(input("New diameter: ")))
        self.weight = self.if_number(str(input("New weight: ")))



