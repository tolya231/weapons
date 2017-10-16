import task_generator
from pulp import *


def write_task(filename, c1, c2, b1, b2, b3, b4, a1, a2, variant):
    f = open(filename, 'a', encoding="utf-8")
    f.write("Вариант " + str(variant) + "\n")
    f.write(
        "Имеются два комплекса вооружения K1 и К2. Обозначим через Х1 и X2 количество комплексов первого и второго типа; \n")
    f.write(str(c1) + " и " + str(c2) + " — среднее количество целей, поражаемых каждым комплексом соответственно; \n")
    f.write(str(b1) + " ," + str(b2) + " ," + str(b3) + " ," + str(
        b4) + " — количество ограниченных ресурсов (стоимость, рабочая сила, дефицитные материалы), которые отпускаются на производство комплексов; \n")
    f.write(str(a1) + ", " + str(
        a2) + " - количество единиц ресурсов, необходимых для производства одного комплекса первого и второго типа.\n")
    f.write(
        "Требуется определить количество комплексов первого и второго типа, при котором математическое ожидание числа пораженных целей максимально. \n\n")
    f.close()


def write_answer(filename, c1, c2, b1, b2, b3, b4, a1, a2, variant):
    tmp1 = list(a1)
    tmp2 = list(a2)
    solution = task_generator.solve_task(c1, c2, b1, b2, b3, b4, a1, a2)
    f = open(filename, 'a', encoding="utf-8")
    f.write("Вариант " + str(variant) + "\n")
    f.write(
        "Математически данная задача может быть записана в виде:\nL = " + str(c1) + "x1 + " + str(c2) + "x2 -> max;\n")
    # f.write((str(tmp1.pop()) + "x1 + " + str(tmp2.pop()) + "x2 <= " + str(b1) + "\n").replace(r"0x1", "").replace(r"1x1", "x1").replace(r"1x2", "x2"))
    f.write((str(tmp1.pop()) + "x1 + " + str(tmp2.pop()) + "x2 <= " + str(b1) + "\n"))
    f.write((str(tmp1.pop()) + "x1 + " + str(tmp2.pop()) + "x2 <= " + str(b2) + "\n"))
    f.write((str(tmp1.pop()) + "x1 + " + str(tmp2.pop()) + "x2 <= " + str(b3) + "\n"))
    f.write((str(tmp1.pop()) + "x1 + " + str(tmp2.pop()) + "x2 <= " + str(b4) + "\n"))
    f.write(
        "Tребуется среди неотрицательных (из смысла задачи ясно, что x1 ≥ 0, х2 ≥ 0) решений системы выбрать такое, при котором выражение принимает максимум.\n")
    f.write("Ответ:\n")
    for variable in solution.variables():
        f.write(str(variable.name) + " = " + str(variable.varValue) + "\n")
    f.write("Целевая функция: " + str(value(solution.objective)) + "\n\n\n")
