class Vector:

    def __init__(self,d):
        self.coords = d * [0]

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, item):
        return self.coords[item]

    def __setitem__(self, key, value):
        self.coords[key] = value

    def __add__(self, other):
        if len(other) != len(self.coords):
            raise TypeError("Dimensions mismatch")
        else:
             result = Vector (len(self))
             for i in range(len(self.coords)):
                 result[i] = self.coords[i] + other[i]
        return result

    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return self.coords == other.coords

    def __str__(self):
        return "<" + str(self.coords[0:len(self)])+">"

if __name__ == '__main__':
    a = Vector(5)
    b = Vector (5)

    for i in range(5):
        a[i] = i*2
        b[i] = i*4

    print(a+b)

    print(a==b)

