# Напишите класс Dragon (Дракон), экземпляр которого при инициализации принимaет аргументы:
# рост, огнеопасность, цвет.

# Класс обеспечивает выполнение методов (dr — экземпляр класса)
# экземпляры можно сравнивать: сначала по росту. затем по огнеопасности, затем по цвету по алфавиту

# экземпляры класса можно складывать: dr2 =dr + dr1. при этом возвращается новый экземпляр со значениями атрибутов:

# цвет меньший по алфавиту;
# рост - среднее арифметическое из двух округлённое до целого вниз,
# огнеопасность - большее из двух;

# из экземпляра класса можно вычесть число: dr -= number, из роста вычитается целая часть от деления роста на число, к
# огнеопасности прибавляется остаток от деления огнеопасности на число;

# Экземпляр можно вызвать с аргументом-строкой - возвращается строка-аргумент, повторенная количество раз, равное
# значению атрибута огнеопасность;

# change_color() - вызывается c аргументом - цветом, на который нужно поменять имеющийся цвет

# str- возвращает строку:
# Dragon with height «рост», danger <огнеопасность> and color «цвет».

# repr- возвращaет строку:
# Dragon(‹рост>, <огнеопасность>, <цвет>)

class Dragon():
    def __init__(self, height, danger, color):
        self.height = height
        self.danger = danger
        self.color = color
    
#__eq__() – для равенства ==
#__ne__() – для неравенства !=
#__lt__() – для оператора меньше <
#__le__() – для оператора меньше или равно <=
#__gt__() – для оператора больше >
#__ge__() – для оператора больше или равно >=

    def __lt__(self, other): # экземпляры можно сравнивать: рост. огнеопасность, цвет.
        if self.height < other.height and self.danger < other.danger and self.color < other.color:
            return True
        else:
            return False
    def __le__(self, other):
        if self.height <= other.height and self.danger <= other.danger and self.color <= other.color:
            return True
        else:
            return False 
    def __gt__(self, other):
        if self.height > other.height and self.danger > other.danger and self.color > other.color:
            return True
        else:
            return False 
    def __ge__(self, other):
        if self.height >= other.height and self.danger >= other.danger and self.color >= other.color:
            return True
        else:
            return False  
    def __eq__(self, other):
        if self.height == other.height and self.danger == other.danger and self.color == other.color:
            return True
        else:
            return False 
    def __ne__(self, other):
        if self.height != other.height or self.danger != other.danger or self.color != other.color:
            return True
        else:
            return False 
    def __add__(self, other):
        import math
        color2 = min(self.color, other.color)
        height2 = math.floor((self.height + other.height)/2)
        danger2 = max(self.danger, other.danger)
        dr2 = Dragon(height2,danger2, color2)
        return(dr2)
    
    def change_color(self):
        new_color = input('Введите новый цвет: ')
        self.color = new_color
        return self
    
    def __isub__(self, value):
        value = int(input('Введите число: '))
        self.height = self.height - int(self.height / value)
        self.danger = self.danger + self.danger % value
        return self
    
    def __mod__(self, value):
        new_height = self.height % value
        new_danger = self.danger // value
        new_color = self.color
        return [Dragon(new_height, new_danger, new_color) for _ in range(value)]
 
    def __call__(self, string):
        return string * self.danger
    
    def str1(self):
        string = input('Введите строку: ')
        print(string * self.danger)
    def __repr__(self) -> str:
        return f'Dragon {self.height}, {self.danger}, {self. color} '
    def str(self):
        return f'Dragon with height {self.height}, danger {self.danger} and color {self.color}'
    
dr = Dragon(69, 5, "brown")
dr1 = Dragon(69, 5, "gray")
print (dr > dr1, dr != dr1, dr <= dr1)
print(dr, dr1, sep="\n" )
print()

dr -= 23
dr1 -= 2
dr2 = dr + dr1
print(dr, dr1, dr2, sep="\n")
print(dr("Класс огнеопасности! "))