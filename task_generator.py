import random
from pulp import *

# K1 и K2 - комплексы вооружения
# с1 и с2 - среднее количество поражаемых целей каждым комплексом
# b1-b4 - количество ограниченных ресурсов
# ai1 и ai2 - количество едениц i-го есурса, необходимое для производства одного комплекса первого и второго типа

def generate_task():
    c1 = random.randint(3, 20)
    c2 = random.randint(3, 20)
    b1 = random.randint(50, 500)
    b2 = random.randint(50, 500)
    b3 = random.randint(50, 500)
    b4 = random.randint(50, 500)
    a1 = list()
    a2 = list()
    for i in range(4):
        a1.append(random.randint(0, 9))
        a2.append(random.randint(1, 9))
    return c1, c2, b1, b2, b3, b4, a1, a2


def solve_task(c1, c2, b1, b2, b3, b4, a1, a2):
    x1 = pulp.LpVariable("x1", lowBound=0)
    x2 = pulp.LpVariable("x2", lowBound=0)
    problem = pulp.LpProblem('0', pulp.LpMaximize)
    problem += c1 * x1 + c2 * x2, "Функция цели"
    problem += a1.pop() * x1 + a2.pop() * x2 <= b1, "1"
    problem += a1.pop() * x1 + a2.pop() * x2 <= b2, "2"
    problem += a1.pop() * x1 + a2.pop() * x2 <= b3, "3"
    problem += a1.pop() * x1 + a2.pop() * x2 <= b4, "4"
    problem.solve()
    return problem



