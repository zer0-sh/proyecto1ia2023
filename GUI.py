import tkinter as tk
from PIL import Image, ImageTk
import leermatriz as lm

class GUI:
    def __init__(self, matrix):
        self.matrix = matrix
        self.root = tk.Tk()
        self.root.title("Pinocho Baretero")
        self.images = {
            "vacío": ImageTk.PhotoImage(Image.open("vacio.png").resize((100, 100))),
            "cigarrillo": ImageTk.PhotoImage(Image.open("cigarrillo.png").resize((100, 100))),
            "zorro": ImageTk.PhotoImage(Image.open("zorro.png").resize((100, 100))),
            "Gepetto": ImageTk.PhotoImage(Image.open("gepetto.png").resize((100, 100))),
            "pinocho": ImageTk.PhotoImage(Image.open("pinocho.png").resize((100, 100)))
        }
        self.canvas = tk.Canvas(self.root, width=800, height=500)
        self.canvas.pack()
        self.draw_board()
        
        self.buttton = tk.Button(self.root, text="Saludar")
                       
    def draw_board(self):
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                item_type = self.get_item_type(row, col)
                x0 = col * 100
                y0 = row * 100
                x1 = x0 + 100
                y1 = y0 + 100
                image = self.images[item_type]
                self.canvas.create_image(x0, y0, anchor=tk.NW, image=image)
                #Botones
                self.button1 = tk.Button(self.canvas, text="Amplitud")
                self.button1.place(x=600, y=120)
                self.button2 = tk.Button(self.canvas, text="Costo")
                self.button2.place(x=600, y=240)
                self.button3 = tk.Button(self.canvas, text="Profundidad")
                self.button3.place(x=600, y=360)
                

        
    def get_item_type(self, row, col):
        if self.matrix[row][col] == "0":
            return "vacío"
        elif self.matrix[row][col] == "C":
            return "cigarrillo"
        elif self.matrix[row][col] == "Z":
            return "zorro"
        elif self.matrix[row][col] == "G":
            return "Gepetto"
        elif self.matrix[row][col] == "P":
            return "pinocho"


gui = GUI(lm.read_matrix_from_file("matriz.txt"))
gui.root.mainloop()

