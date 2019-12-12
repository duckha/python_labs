import cProfile
import random
import Main3

cProfile.run('Main3.makeArrays(500, 500); Main3.makeArrays(100, 100); Main3.makeArrays(50, 50)')
cProfile.run('[[random.randint(0, 10) for j in range(500)] for i in range(500)]; [[random.randint(0, 10) for j in range(100)] for i in range(100)]; [[random.randint(0, 10) for j in range(50)] for i in range(50)]')


