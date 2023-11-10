class Parallelepiped:
    
    def __init__(self, a, b, c):
        self.a = a  
        self.b = b 
        self.c = c 

    def countArea (self):
        S = 2 * (self.a * self.b + self.b * self.c + self.a * self.c) 
        return S 
    
    def countVolume(self):
        V = self.a * self.b * self.c
        return V

figure = Parallelepiped(3, 1, 2)
print('Площадь = ', figure.countArea(), '\nОбъём = ', figure.countVolume())
