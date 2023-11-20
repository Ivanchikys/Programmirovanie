import random

class Vegetable:
    states = { 0:'Отсутствует',
                1:'Цветение',
                2:'Зеленый',
                3:'Красный'
             }
    
    def __init__(self, index = 0):
        self._index = index
        self._state = self.states[0]

    def grow(self):
        self._index += 1
        self._state = self.states.get(self._index,  'Красный')
        return self._state
    
    def is_ripe(self):
        return self._state == 'Красный'
    
class Tomato(Vegetable):
    def __init__(self, index = 0, variety = ''):
        super().__init__(index)
        self._variety = variety 

    def give_variety(self):
        return self._variety
    
class TomatoBush:
    varieties = ['Агата','Черри','Аврора']
    def __init__(self,  countTomatoes):
        self.tomatoes = [Tomato(random.randint(0, 2), self.varieties[random.randint(0, 2)]) for _ in range(countTomatoes)]
        
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow() 

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)
    
    def give_away_all(self):
        self.tomatoes.clear()   

class Gardener:
    def __init__(self, plant, name):
        self._plant = plant
        self.name = name
    
    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print(self.name,'всё созрело. Собираем урожай')
            self.harvestVariet =[tomato.give_variety() for tomato in self._plant.tomatoes]
            self._plant.give_away_all()
        else:
            print(self.name, 'Урожай не созрел. Дождёмся созревания урожая')

    @staticmethod
    def knowledge_base():
        print('''Harvest time for tomatoes should ideally occur
when the fruit is a mature green and
then allowed to ripen off the vine.
This prevents splitting or bruising
and allows for a measure of control over the ripening process.''')  

bush = TomatoBush(countTomatoes = 3)                          #кол-во 
gardener = Gardener(name = 'Ivan', plant = bush )
gardener.work()

while not bush.all_are_ripe():
    gardener.work()
    gardener.harvest()

print('Сорты собранного урожая: ',(', '.join(gardener.harvestVariet)))



