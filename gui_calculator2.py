import tkinter as tk
from tkinter import messagebox
from math import sqrt

class CalcolatriceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calcolatrice Python")
        self.risultato_corrente = None

        # Numero 1
        self.label1 = tk.Label(root, text="Numero 1:")
        self.label1.grid(row=0, column=0)
        self.entry1 = tk.Entry(root)
        self.entry1.grid(row=0, column=1)

        # Numero 2
        self.label2 = tk.Label(root, text="Numero 2:")
        self.label2.grid(row=1, column=0)
        self.entry2 = tk.Entry(root)
        self.entry2.grid(row=1, column=1)

        # Operazione
        self.operazione = tk.StringVar(value="Addizione")
        opzioni = ["Addizione", "Sottrazione", "Moltiplicazione", "Divisione", "Radice quadrata"]
        self.menu_operazione = tk.OptionMenu(root, self.operazione, *opzioni, command=self.aggiorna_interfaccia)
        self.menu_operazione.grid(row=2, column=0, columnspan=2, sticky="ew")

        # Bottone calcola
        tk.Button(root, text="Calcola", command=self.calcola).grid(row=3, column=0, columnspan=2, sticky="ew")

        # Risultato
        tk.Label(root, text="Risultato:").grid(row=4, column=0)
        self.risultato = tk.StringVar()
        tk.Label(root, textvariable=self.risultato).grid(row=4, column=1)

        # Operazioni concatenate
        tk.Label(root, text="Operazione successiva:").grid(row=5, column=0)
        self.operazione2 = tk.StringVar(value="Addizione")
        self.menu_operazione2 = tk.OptionMenu(root, self.operazione2, *opzioni, command=self.aggiorna_interfaccia2)
        self.menu_operazione2.grid(row=5, column=1, sticky="ew")
        self.label3 = tk.Label(root, text="Numero:")
        self.label3.grid(row=6, column=0)
        self.entry3 = tk.Entry(root)
        self.entry3.grid(row=6, column=1)
        tk.Button(root, text="Applica al risultato", command=self.concatena).grid(row=7, column=0, columnspan=2, sticky="ew")

        # Bottone reset
        tk.Button(root, text="Reset", command=self.reset).grid(row=8, column=0, columnspan=2, sticky="ew")

        self.aggiorna_interfaccia("Addizione")
        self.aggiorna_interfaccia2("Addizione")

    def aggiorna_interfaccia(self, op):
        if op == "Radice quadrata":
            self.label1.config(text="Numero:")
            self.label2.grid_remove()
            self.entry2.grid_remove()
        else:
            self.label1.config(text="Numero 1:")
            self.label2.grid()
            self.entry2.grid()

    def aggiorna_interfaccia2(self, op):
        if op == "Radice quadrata":
            self.label3.grid_remove()
            self.entry3.grid_remove()
        else:
            self.label3.grid()
            self.entry3.grid()

    def calcola(self):
        try:
            op = self.operazione.get()
            n1 = self.entry1.get()
            n2 = self.entry2.get()
            if op == "Radice quadrata":
                if not n1:
                    messagebox.showerror("Errore", "Inserisci il numero!")
                    return
                n1 = float(n1)
                if n1 < 0:
                    messagebox.showerror("Errore", "Radice di numero negativo!")
                    self.risultato.set("")
                else:
                    res = sqrt(n1)
                    self.risultato.set(str(res))
                    self.risultato_corrente = res
            else:
                if not n1 or not n2:
                    messagebox.showerror("Errore", "Inserisci entrambi i numeri!")
                    return
                n1 = float(n1)
                n2 = float(n2)
                if op == "Addizione":
                    res = n1 + n2
                elif op == "Sottrazione":
                    res = n1 - n2
                elif op == "Moltiplicazione":
                    res = n1 * n2
                elif op == "Divisione":
                    if n2 == 0:
                        messagebox.showerror("Errore", "Divisione per zero!")
                        self.risultato.set("")
                        return
                    res = n1 / n2
                self.risultato.set(str(res))
                self.risultato_corrente = res
        except ValueError:
            messagebox.showerror("Errore", "Inserisci solo numeri validi!")
            self.risultato.set("")

    def concatena(self):
        if self.risultato_corrente is None:
            messagebox.showinfo("Info", "Prima esegui un calcolo!")
            return
        try:
            op = self.operazione2.get()
            if op == "Radice quadrata":
                if self.risultato_corrente < 0:
                    messagebox.showerror("Errore", "Radice di numero negativo!")
                    self.risultato.set("")
                else:
                    res = sqrt(self.risultato_corrente)
                    self.risultato.set(str(res))
                    self.risultato_corrente = res
            else:
                n3 = self.entry3.get()
                if not n3:
                    messagebox.showerror("Errore", "Inserisci il numero!")
                    return
                n3 = float(n3)
                if op == "Addizione":
                    res = self.risultato_corrente + n3
                elif op == "Sottrazione":
                    res = self.risultato_corrente - n3
                elif op == "Moltiplicazione":
                    res = self.risultato_corrente * n3
                elif op == "Divisione":
                    if n3 == 0:
                        messagebox.showerror("Errore", "Divisione per zero!")
                        self.risultato.set("")
                        return
                    res = self.risultato_corrente / n3
                self.risultato.set(str(res))
                self.risultato_corrente = res
        except ValueError:
            messagebox.showerror("Errore", "Inserisci solo numeri validi!")
            self.risultato.set("")

    def reset(self):
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.entry3.delete(0, tk.END)
        self.risultato.set("")
        self.risultato_corrente = None
        self.aggiorna_interfaccia(self.operazione.get())
        self.aggiorna_interfaccia2(self.operazione2.get())

if __name__ == "__main__":
    root = tk.Tk()
    app = CalcolatriceGUI(root)
    root.mainloop()