import tkinter as tk 
import random
import string

class MiApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.caracteres = list(string.ascii_letters+string.punctuation)
        self.password = ''
        self.ancho = 20
        self.pack()
        self.btnPassword()
        self.txtPassword()
        self.btnQuit()
        
    def btnPassword(self):
        self._btnPassword = tk.Button(self)
        self._btnPassword["text"] = "Nueva contraseña"
        self._btnPassword["command"] = self._nuevoPassword
        self._btnPassword.pack(side="left")
        
    def txtPassword(self):
        self.sv_txtPassword = tk.StringVar(self)
        self._txtPassword = tk.Entry(self, textvariable=self.sv_txtPassword)
        self._txtPassword['width'] = 32
        self._txtPassword.pack(side="left")

    def btnQuit(self):
        self._btnQuit = tk.Button(self)
        self._btnQuit["text"] = "Cerrar"
        self._btnQuit["fg"] = "red"
        self._btnQuit["command"] = self.master.destroy
        self._btnQuit.pack(side="right")

    def _nuevoPassword(self):
        self.password = ''.join(random.choices(self.caracteres, k=self.ancho))
        self.sv_txtPassword.set(self.password)
        print(self.password)


root = tk.Tk()
root.title('Generador de contraseñas')

ancho = root.winfo_reqwidth()
alto = root.winfo_reqheight()
pos_izquierda = int(root.winfo_screenwidth()/2 - ancho/2)
pos_superior = int(root.winfo_screenheight()/2 - alto/2)
root.geometry("+{}+{}".format(pos_izquierda, pos_superior))

app = MiApp(master=root)
app.mainloop()