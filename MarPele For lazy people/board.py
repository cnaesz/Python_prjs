
from tkinter import Tk, Canvas, Button, Label, StringVar, Entry, messagebox
from colors import get_colors
from marpele import Marpele_auto

# Constants
SIZE = 50
root = Tk()
root.title("MarPele For lazy people")
root.geometry("1920x1080")
root.config(bg="#f0f0f0")

canvas = Canvas(root)


class board(Marpele_auto):
    
    
    """Class to create a board with desire numbered squares."""


    def __init__(self, n ):
        super().__init__()
        self.n = n
        self.canvas = canvas
        self.draw_board()
        self.canvas.pack(padx=0, pady=0, fill='both', expand=True)


    def draw_board(self):
        numba = 0
        f = 15
        for y in range(self.n):
            for x in range(self.n):
                x1 = x * SIZE
                y1 = y * SIZE
                x2 = x1 + SIZE
                y2 = y1 + SIZE
                color = get_colors()
                numba += 1
                self.canvas.create_rectangle((x1, y1, x2, y2), fill=color)
                self.canvas.create_text((x1 + f, y1 + f), fill="black", font="Times 15 bold", text=f"{numba}", anchor="nw", justify="center")
    def Create_mar(self):
        """Create a button to start the game."""
        self.button = Button(root, text="Start Game", command=self.play, bg="lightblue", font=("Arial", 14))
        self.button.pack(pady=20)

        self.label = Label(root, text="Welcome to MarPele For lazy people!", font=("Arial", 20), bg="#f0f0f0")
        self.label.pack(pady=10)

        self.canvas.create_window(960, 540, window=self.button)
        self.canvas.create_window(960, 500, window=self.label)




s = board(10)

root.after(10000, lambda: root.destroy())
root.mainloop()