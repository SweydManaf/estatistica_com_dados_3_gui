from tkinter import *

import sv_ttk

from mainWindow import MainWindow


class MainApp:
    def __init__(self):
        self.root = Tk()
        self.root.title('Estatistíca de F. Beira')

        # CONFIGURING THE ROOT WINDOWS
        self.height = 500
        self.width = 500
        self.sys_height = int((self.root.winfo_screenheight() / 2) - (self.height / 2))
        self.sys_width = int((self.root.winfo_screenwidth() / 2) - (self.width / 2))
        self.root.geometry(f'{self.width}x{self.height}+{self.sys_width}+{self.sys_height}')
        self.root.resizable(False, False)

        # ADD THEME
        sv_ttk.set_theme('light')

        # CALL MAIN WINDOW
        MainWindow(self.root)

        # START THE APPLICATION
        self.root.mainloop()


if __name__ == '__main__':
    MainApp()
