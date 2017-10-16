from tkinter import *
from tkinter import filedialog

root = Tk()
root.resizable(width=False, height=False)
root.title("Задача о выборе системы вооружения")
root.geometry('{}x{}'.format(400,150))


def quit(event):
    global root
    root.destroy()


def create_window():
    info_window = Toplevel(root)
    info_window.title("Документация по задаче")
    get_info(info_window,
             """Задача о выборе системы вооружения и объеме ее производства. Требуется определить, в каком количестве 
             следует производить комплексы оружия разных классов, чтобы обеспечить максимальную эффективность 
             системы вооружения при заданных ресурсах.""")


def get_info(frame, text):
    label = Label(frame, text = text)
    label.pack()


def save_tasks(event):
    fn = filedialog.SaveAs(root, filetypes=[('*.txt files', '.txt')]).show()
    if fn == '':
        return
    if not fn.endswith(".txt"):
        fn += ".txt"
    open(fn, 'wt').write("TODO")


def save_answers(event):
    print("hi")


def generate(event):
    print("generating..")


info_button = Button(root, text="Информация о задаче", bg="white", fg="black", command=create_window)
task_button = Button(root, text="Скачать задачи", bg="white", fg="black")
answer_button = Button(root, text="Скачать ответы", bg="white", fg="black")
generate_button = Button(root, text="Сгенерировать новые задачи", bg="white", fg="black")
close_button = Button(root, text="Завершить работу", bg="white", fg="black")

task_button.bind("<Button-1>", save_tasks)
answer_button.bind("<Button-1>", save_answers)
generate_button.bind("<Button-1>", generate)
close_button.bind("<Button-1>", quit)

info_button.pack()
generate_button.pack()
task_button.pack()
answer_button.pack()
close_button.pack()

root.mainloop()
