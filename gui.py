from tkinter import *
from tkinter import filedialog
import task_generator
import task_writer

root = Tk()
root.resizable(width=False, height=False)
root.title("Задача о выборе системы вооружения")
root.geometry('{}x{}'.format(400, 150))


def quit():
    global root
    root.destroy()


def create_window():
    info_window = Toplevel(root)
    info_window.title("Документация по задаче")
    info_window.resizable(width=False, height=False)
    get_info(info_window,
             """Задача о выборе системы вооружения и объеме ее производства. Требуется определить, в каком количестве 
             следует производить комплексы оружия разных классов, чтобы обеспечить максимальную эффективность 
             системы вооружения при заданных ресурсах.""")
    get_info(info_window,
             """При нажатии кнопки 'Скачать задания' необходимо выбрать, куда сохранить файл с вариантами заданий. 
             Ответы к задачам будут сохранены в ту же директорию (файл с добавлением '_ответы' в конце)""")

    quit_button = Button(info_window, text="Закрыть", bg="white", fg="black", command=info_window.destroy)
    quit_button.pack()


def get_info(frame, text):
    label = Label(frame, text=text)
    label.pack()


def save_tasks():
    fn = filedialog.SaveAs(root, filetypes=[('*.txt files', '.txt')]).show()
    if fn == '':
        return
    if not fn.endswith(".txt"):
        fn += ".txt"
    for i in range(20):
        c1, c2, b1, b2, b3, b4, a1, a2 = task_generator.generate_task()
        task_writer.write_task(fn, c1, c2, b1, b2, b3, b4, a1, a2, i + 1)
        save_answers(fn.replace(".txt", "_ответы.txt"), c1, c2, b1, b2, b3, b4, a1, a2, i + 1)


def save_answers(fn, c1, c2, b1, b2, b3, b4, a1, a2, i):
    task_writer.write_answer(fn, c1, c2, b1, b2, b3, b4, a1, a2, i)


info_button = Button(root, text="Информация о задаче", bg="white", fg="black", command=create_window)
task_button = Button(root, text="Скачать задания", bg="white", fg="black", command=save_tasks)
close_button = Button(root, text="Завершить работу", bg="white", fg="black", command=quit)

info_button.pack()
task_button.pack()
close_button.pack()

root.mainloop()
