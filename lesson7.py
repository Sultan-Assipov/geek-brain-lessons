# task1
class Matrix:
    """the class accepts the list of lists, The lists are the rows"""

    def __init__(self, lists):
        self.matrix = lists

    def __str__(self):
        result = ""
        for rows in self.matrix:
            for el in rows:
                result += " " + str(el)
            result += "\n"
        return result

    def __add__(self, other):
        result = []
        for j in range(len(self.matrix)):
            result_row = [self.matrix[j][i] + other.matrix[j][i] for i in range(len(self.matrix[j]))]
            result.append(result_row)
        return Matrix(result)


mat1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mat1)
mat2 = mat1 + mat1
print(mat2)


# task2
class Clothes:
    pass


class Coat(Clothes):
    def __init__(self, size: float):
        self.size = size

    @property
    def material_use(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height: float):
        self.height = height

    @property
    def material_use(self):
        return self.height * 2 + 0.3


coat1 = Coat(2)
suit1 = Suit(3)
print(coat1.material_use + suit1.material_use)

class Cell:
    def __init__(self, unit_num : int):
        if unit_num<0:
            raise ValueError("positive number required")
        self.unit_num = unit_num

    def __add__(self, other):
        return Cell(self.unit_num + other.unit_num)

    def __sub__(self, other):
        if self.unit_num > other.unit_num:
            return Cell(self.unit_num - other.unit_num)
        else:
            print("cant get a negative value")

    def __mul__(self, other):
        return Cell(self.unit_num * other.unit_num)

    def __truediv__(self, other):
        return Cell(self.unit_num // other.unit_num)

    def make_order(self, items_in_row):
        row_num = self.unit_num // items_in_row
        return ("*" * items_in_row + "\n") * row_num + "*" * (self.unit_num % items_in_row)

    def __str__(self):
        return f"Cell has {self.unit_num} elements"


cell1 = Cell(5)
cell2 = Cell(20)
print(cell1/cell2)
print(cell2.make_order(3))

