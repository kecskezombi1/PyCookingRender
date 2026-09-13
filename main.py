import tkinter as tk

#Ablak
class App(tk.Tk):
    def __init__(root):
        super().__init__()
        root.geometry("500x800")
        root.resizable(width=False, height=False)
        root.title("Recept simulator")
        label = tk.Label(root, text="Üdvözöljünk a Recept simulatorban", font=("Arial", 15, "bold"))
        label.pack()
app = App()
app.mainloop()