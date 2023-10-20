import random 

tuple1 = tuple(random.randint(0,5) for _ in range(10))
tuple2 = tuple(range(-5,1))

tuple3 = tuple1 + tuple2
count = tuple3.count(0) 

print ('Кортеж:',tuple3 ,'\nКол-во нулей =' ,count )