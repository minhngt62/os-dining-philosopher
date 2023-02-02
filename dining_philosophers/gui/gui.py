from pathlib import Path
import tkinter as tk
from typing import List, Any
from tkinter.scrolledtext import ScrolledText

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets")

def rel(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class GUI():
    def __init__(self, size: str = "879x741", bg: str = "#FFFFFF"):
        window = tk.Tk()
        window.geometry(size)
        window.configure(bg=bg)

        self.window = window
        
        from .events import EventHandler
        self.event_handler = EventHandler(self)
    
    def default_build(self):
        self.create_canvas()
        self.place_table()
        self.place_philosophers()
        self.create_terminal()
        self.create_btn_start()
        self.create_btns()
        self.place_notations()

        self.window.resizable(False, False)
        self.window.mainloop()

    def create_canvas(self):
        self._canvas = tk.Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 741,
            width = 879,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
            )
        self._canvas.place(x=0, y=0)
    
    def place_table(self, bg="table.png"):
        self._table_img = tk.PhotoImage(file=rel(bg))
        self._table = self._canvas.create_image(333, 374, image=self._table_img)

    def place_philosophers(self, bg="philosopher.png"):
        self._philosopher_img = tk.PhotoImage(file=rel(bg))
        phil_coors = [(560, 555), (551, 168), (223, 94), (65, 387), (223, 645)]
        self._philosophers = []
        for i in range(len(phil_coors)):
            philosopher = self._canvas.create_image(
                phil_coors[i][0],
                phil_coors[i][1],
                image=self._philosopher_img
            )
            self._philosophers.append(philosopher)
    
    def create_terminal(self, logo="thread.png"):
        self._canvas.create_rectangle(655.0, 147.0, 855.0, 475.0, fill="#FFFDFD", outline="black")

        self._thread_img = tk.PhotoImage(file=rel(logo))
        self._thread = self._canvas.create_image(749.0, 176.0, image=self._thread_img)

    def create_btn_start(self, bg="start.png"):
        self._btn_start_img = tk.PhotoImage(file=rel(bg))
        self._btn_start = tk.Button(
            image=self._btn_start_img,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: None,
            relief="flat"
        )
        self._btn_start.place(
            x=668.0,
            y=406.0,
            width=173,
            height=44.0
        )

        self.event_handler.btn_start()
    
    def create_btns(self):
        btn_w, btn_h = 173.0, 48.6048583984375
        btn_coors = [(668.0, 202.393310546875), (668, 348.2078857421875), (668, 250.9981689453125), (668, 299.60302734375)]
        self._btn_imgs = [tk.PhotoImage(file=rel(f"button_{i+1}.png")) for i in range(len(btn_coors))]
        self._btns: List[tk.Button] = []
        for i in range(len(btn_coors)):
            btn = tk.Button(
                image=self._btn_imgs[i],
                borderwidth=0,
                highlightthickness=0,
                command=lambda: None,
                relief="flat"
            )
            btn.place(
                x=btn_coors[i][0],
                y=btn_coors[i][1],
                width=btn_w,
                height=btn_h
            )
            self._btns.append(btn)
        
        self.event_handler.btn_select_method()
    
    def place_notations(self):
        self._canvas.create_rectangle(692.0, 497.0, 712.0, 517.0, fill="#FF0000", outline="")
        self._canvas.create_text(716.0, 493.0,
            anchor="nw",
            text="HUNGRY",
            fill="#000000",
            font=("Lato Bold", 20 * -1)
        )

        self._canvas.create_rectangle(692.0, 569.0, 712.0, 589.0, fill="#00FF00", outline="")
        self._canvas.create_text(716.0, 565.0,
            anchor="nw",
            text="EATING",
            fill="#000000",
            font=("Lato Bold", 20 * -1)
        )

        self._canvas.create_rectangle(692.0, 533.0, 712.0, 553.0, fill="#0000FF", outline="")
        self._canvas.create_text(716.0, 529.0,
            anchor="nw",
            text="THINKING",
            fill="#000000",
            font=("Lato Bold", 20 * -1)
        )

if __name__ == "__main__":
    gui = GUI()
    gui.default_build()