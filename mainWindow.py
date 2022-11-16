from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

vetores = []


class MainWindow:
    def __init__(self, master):
        self.master = master

        # CONFIGURE WINDOW
        self.height = 500
        self.width = 500
        self.master.geometry(f'{self.width}x{self.height}')

        # MENU BAR
        self.menuBar = Menu(self.master, tearoff=False)

        self.master.config(menu=self.menuBar)

        self.file_menu = Menu(self.menuBar)

        self.subMenuVectore = Menu(self.file_menu, tearoff=False)

        self.menuBar.add_cascade(label='Dica', menu=self.file_menu)
        self.file_menu.add_cascade(label='Vetores usados', menu=self.subMenuVectore)

        # MAIN FRAME
        self.mainFrame = ttk.Frame(self.master, width=500, height=500)

        self.labelName = ttk.Label(self.mainFrame, text='Dados III', font='Terminal 24 italic')
        self.labelName.configure(anchor='center', padding=5)

        self.dataVar = StringVar()
        self.validateEntry = self.mainFrame.register(self.validate_number)
        self.dataEntry = ttk.Entry(self.mainFrame, width=10, justify='center', validate='focusout',
                                   validatecommand=self.validate_number, textvariable=self.dataVar)
        self.dataEntry.bind('<Return>', lambda a: self.enter_function())

        self.enterButton = ttk.Button(self.mainFrame, text='Enter   ', width=10, command=self.enter_function)
        self.enterImage = ImageTk.PhotoImage(Image.open('assets/plus.png').resize((20, 20)))
        self.enterButton.configure(image=self.enterImage, compound=RIGHT)

        self.resetButton = ttk.Button(self.mainFrame, text='Reset', command=self.reset_funtion)

        self.dataSpaceText = Text(self.mainFrame, width=40, height=15)
        self.dataSpaceText.configure(state=DISABLED)
        self.dataInVector = []

        self.submitButton = ttk.Button(self.mainFrame, text='Submeter  ', width=10, command=self.submit_function)
        self.submitImage = ImageTk.PhotoImage(Image.open('assets/right-arrow.png').resize((20, 20)))
        self.submitButton.configure(image=self.submitImage, compound=RIGHT)

        # DRAW WIDGETS
        self.draw_widgets()

        # FIRST ACTIONS
        self.dataEntry.focus()

    def draw_widgets(self):
        self.mainFrame.grid(row=0, column=0, padx=80)

        self.labelName.grid(row=0, column=0, columnspan=2, pady=(20, 0))

        self.dataEntry.grid(row=1, column=0, pady=(50, 20), sticky='e', padx=(0, 5))
        self.enterButton.grid(row=1, column=1, pady=(50, 20), sticky='w', padx=(5, 0))
        self.resetButton.grid(row=1, column=2, pady=(50, 20), sticky='w', padx=(0, 0))

        self.dataSpaceText.grid(row=2, column=0, columnspan=2)

        self.submitButton.grid(row=3, column=0, columnspan=2, pady=20)

    def validate_number(self):
        data = self.dataVar.get().replace(',', '.')
        if float(data) >= 0 or data == '0':
            return True
        else:
            return False

    def enter_function(self):
        self.dataSpaceText.configure(state=NORMAL)
        data = self.dataVar.get().replace(',', '.')
        try:
            if self.validate_number() or data == '0' and int(data) >= 0:
                data = data.replace('-', '')
                self.dataSpaceText.insert(INSERT, f'{data}; ')
                self.dataInVector.append(float(data))
                self.dataVar.set('')
            else:
                messagebox.showerror('Dado inválido', 'Você deve fornecer somente números')
                self.dataVar.set('')
                self.dataEntry.focus()
            self.dataSpaceText.configure(state=DISABLED)
            self.dataEntry.focus()
        except:
            messagebox.showerror('Dado inválido', 'Você deve fornecer somente números')
            self.dataVar.set('')
            self.dataEntry.focus()
        self.dataSpaceText.configure(state=DISABLED)
        self.dataEntry.focus()

    def reset_funtion(self):
        # self.dataSpaceText.configure(state=NORMAL)
        self.dataInVector.clear()
        self.dataSpaceText.edit_reset()
        self.dataEntry.focus()

    def submit_function(self):
        if len(self.dataInVector) >= 30:
            self.menuBar.destroy()
            self.mainFrame.destroy()
            self.add_vector_to_menu()
            WindowDataTable(self.master, self.dataInVector)
        else:
            messagebox.showwarning('Amostra incompleta', 'A amostra dos dados do tipo III deve ser maior ou igual a 30')
            self.dataEntry.focus()

    def add_vector_to_menu(self):
        pass


#########################################################################################################
from calculus import Calculus
import matplotlib.pyplot as plt


class WindowDataTable:
    def __init__(self, master, vector):
        self.master = master
        self.calculos = Calculus(vector)

        # CONFIGURE WINDOW
        self.height = 530
        self.width = 600
        self.master.geometry(f'{self.width}x{self.height}')

        # MAIN FRAME
        self.mainFrame = ttk.Frame(master)

        self.nameTable = ttk.Label(self.mainFrame, text='Resultados Estatísticos', font='Terminal 24 italic')

        self.atLabel = ttk.Label(self.mainFrame, text=f'AT = {self.calculos.get_at()}')
        self.numClassesLabel = ttk.Label(self.mainFrame, text=f'K = {self.calculos.get_k()}')
        self.interClassesLabel = ttk.Label(self.mainFrame, text=f'AC = {self.calculos.get_ac()}')

        # TABLE OF DATA
        self.dataTable = ttk.Treeview(self.mainFrame, columns=('No', 'Intervalos', 'Ci', 'Fi', 'Fa', 'Fi %', 'Fa %'),
                                      show='headings', height=10)
        ############### COLUMNS ###########################
        self.dataTable.column('No', width=70, minwidth=30)
        self.dataTable.column('Intervalos', width=130, minwidth=70, anchor='center')
        self.dataTable.column('Ci', width=70, minwidth=30, anchor='center')
        self.dataTable.column('Fi', width=70, minwidth=30, anchor='center')
        self.dataTable.column('Fa', width=70, minwidth=30, anchor='center')
        self.dataTable.column('Fi %', width=70, minwidth=30, anchor='center')
        self.dataTable.column('Fa %', width=70, minwidth=30, anchor='center')
        ############### HEADINGS ##########################
        self.dataTable.heading('No', text='No', anchor='center')
        self.dataTable.heading('Intervalos', text='Intervalos', anchor='center')
        self.dataTable.heading('Ci', text='Ci', anchor='center')
        self.dataTable.heading('Fi', text='Fi', anchor='center')
        self.dataTable.heading('Fa', text='Fa', anchor='center')
        self.dataTable.heading('Fi %', text='Fi %', anchor='center')
        self.dataTable.heading('Fa %', text='Fa %', anchor='center')
        ####################################################

        self.mediaLabel = ttk.Label(self.mainFrame, text=f'Média = {self.calculos.get_media()}')
        self.medianaLabel = ttk.Label(self.mainFrame, text=f'Mediana = {self.calculos.get_mediana()}')
        self.modaLabel = ttk.Label(self.mainFrame, text=f'Moda = {self.calculos.get_moda()}')

        self.medidasButton = ttk.Button(self.mainFrame, text='Medidas de dispersão', width=20,
                                        command=self.medidas_function)

        self.showHistButton = ttk.Button(self.mainFrame, text='Gerar gráfico em histograma', width=30,
                                         command=self.hist_function)
        self.showHistButton.configure(padding=5)
        self.showPolignButton = ttk.Button(self.mainFrame, text='Gerar gráfico de poligonos', width=25,
                                           command=self.polign_function)
        self.showState = False

        self.backButton = ttk.Button(self.mainFrame, text='Voltar', command=self.back_function)

        # DRAW WIDGETS
        self.draw_widgets()

        # FIRST ACTIONS
        self.print_data_sheet()

    def draw_widgets(self):
        self.mainFrame.grid(row=0, column=0)

        self.nameTable.grid(row=0, column=0, columnspan=3, padx=(20, 0), pady=(10, 20))

        self.atLabel.grid(row=1, column=0, padx=(50, 0), pady=(0, 10), sticky='we')
        self.numClassesLabel.grid(row=1, column=1, padx=(110, 0), pady=(0, 10), sticky='we')
        self.interClassesLabel.grid(row=1, column=2, padx=(40, 0), pady=(0, 10), sticky='we')

        self.dataTable.grid(row=2, column=0, columnspan=3, padx=(25, 0), pady=(0, 0), sticky='we')

        self.mediaLabel.grid(row=3, column=0, padx=(50, 0), pady=(10, 10), sticky='we')
        self.medianaLabel.grid(row=3, column=1, padx=(100, 0), pady=(10, 10), sticky='we')
        self.modaLabel.grid(row=3, column=2, padx=(40, 0), pady=(10, 10), sticky='we')

        self.medidasButton.grid(row=4, column=0, columnspan=3, padx=(50, 0), pady=(5, 10))

        self.showHistButton.grid(row=5, column=0, columnspan=2, padx=(20, 50), pady=(0, 10), sticky='w')
        self.showPolignButton.grid(row=5, column=1, columnspan=2, padx=(180, 0), pady=(0, 10), sticky='w')

        self.backButton.grid(row=6, column=0, columnspan=3, padx=(30, 0), pady=(10, 0))

    def print_data_sheet(self):
        intervalos = self.calculos.get_classes()
        ci = self.calculos.get_ci()
        fi = self.calculos.get_fi()
        fa = self.calculos.get_fa()
        fi_per = self.calculos.get_fi_per()
        fa_per = self.calculos.get_fa_per()

        try:
            for i in range(0, self.calculos.get_k()):
                self.dataTable.insert('', END, values=(
                    i + 1, f'[ {intervalos[i][0]} ; {intervalos[i][1]} [', ci[i], fi[i], fa[i], fi_per[i], fa_per[i]))
        except:
            messagebox.showerror('Erro', 'Algum erro ocorreu')

    def medidas_function(self):
        messagebox.showerror('Em desenvolvimento', 'Função não implementada')

    def back_function(self):
        self.mainFrame.destroy()
        MainWindow(self.master)

    def hist_function(self):
        if not self.showState:
            intervalos = self.calculos.get_classes()
            classes = [intervalos[x][0] for x in range(self.calculos.get_k())]
            classes.append(intervalos[self.calculos.get_k() - 1][1])

            plt.title('Histograma')
            plt.xlabel('Classes', fontsize=15)
            plt.ylabel('Frequência Absoluta', fontsize=15)
            plt.tick_params(labelsize=10)
            plt.rcParams["figure.figsize"] = (4, 4)
            plt.grid(visible=True, color='#607c8e')
            plt.margins(x=0, y=0)
            plt.yticks(self.calculos.get_fi())

            self.showState = True

            plt.hist(self.calculos.vector, bins=classes, rwidth=1, color='red', alpha=0.7, edgecolor='black')
            plt.show()

            self.showState = False

    def polign_function(self):
        if not self.showState:
            intervalos = self.calculos.get_classes()
            classes = [intervalos[x][0] for x in range(self.calculos.get_k())]

            plt.title('Gráfico de Poligonos')
            plt.xlabel('Classes', fontsize=15)
            plt.ylabel('Frequência Absoluta', fontsize=15)
            plt.tick_params(labelsize=10)
            plt.rcParams["figure.figsize"] = (4, 4)
            plt.grid(visible=True, color='#607c8e')
            plt.margins(x=0, y=0)
            plt.yticks(self.calculos.get_fi())

            self.showState = True

            plt.plot(classes, self.calculos.get_fi(), color='red', alpha=0.7)
            plt.show()

            self.showState = False
