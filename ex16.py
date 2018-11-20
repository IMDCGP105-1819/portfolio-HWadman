class Fraction(object):
    def __init__(self, num, denum):
        if type(num)!=int:
            raise Exception("The numerator must be a integer")

        if type(denum)!=float:
            raise Exception("The denominator must be a integer")

        self.num = num;
        self.denum = denum;

    def __str__(self):
        return str(f"{self.num}/{self.denum}")

    def __add__(self, other):
        LCD = self.num * other.num
        addNum = self.num + other.num
        return Fraction(addNum, LCD)

    def __sub__(self, other):
        LCD = self.num * other.num
        subNum = self.num - other.num
        return Fraction(subNum, LCD)

    def __mul__(self, other):
        mulNum = self.num * other.num
        mulDenum = self.denum * other.denum
        return Fraction(mulNum, mulDenum)

    def __truediv__(self, other):
        otherFlip = Fraction(other.denum, other.num)
        return self * otherFlip

    def Inverse(self):
        return Fraction(self.denum, self.num)



fract1 = Fraction(2,6)
fract2 = Fraction(2,4)
