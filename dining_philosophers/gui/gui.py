from pathlib import Path
import tkinter as tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets")

def rel(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class GUI():
    def __init__(self, size: str = "1389x891", bg: str = "#FFFFFF"):
        window = tk.Tk()
        window.geometry(size)
        window.configure(bg=bg)

        self.window = window
    
    def default_build(self):
        self.create_canvas()
        self.place_table()
        self.place_philosophers()
        self.create_terminal()
        self.create_btns()
        self.place_notations()

        self.window.resizable(False, False)
        self.window.mainloop()

    def create_canvas(self):
        self._canvas = tk.Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 891,
            width = 1389,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
            )
        self._canvas.place(x=0, y=0)
    
    def place_table(self, bg="table.png"):
        self._table_img = tk.PhotoImage(file=rel(bg))
        self._table = self._canvas.create_image(369, 454, image=self._table_img)

    def place_philosophers(self, bg="philosopher.png"):
        self._philosopher_img = tk.PhotoImage(file=rel(bg))
        phil_coors = [(596, 635), (259, 725), (101, 467), (596, 252), (259, 174)]
        self._philosophers = []
        for i in range(len(phil_coors)):
            philosopher = self._canvas.create_image(
                phil_coors[i][0],
                phil_coors[i][1],
                image=self._philosopher_img
            )
            self._philosophers.append(philosopher)
    
    def create_terminal(self, logo="thread.png"):
        self._canvas.create_rectangle(756.0, 122.0, 1331.0, 808.0, fill="#FFFDFD", outline="")

        self._thread_img = tk.PhotoImage(file=rel(logo))
        self._thread = self._canvas.create_image(834.0, 161.0, image=self._thread_img)
        self._logging = self._canvas.create_text(790.0, 200.0,
            anchor="nw",
            fill="#000000",
            font=("Inter", 12 * -1)
        )
    
    def create_btns(self):
        btn_w, btn_h = 136.21359252929688, 34.0
        btn_coors = [(902.2621459960938, 88), (1048.5242919921875, 88.0), (1194.786376953125, 88.0), (756.0, 88)]
        self._btn_imgs = [tk.PhotoImage(file=rel(f"button_{i+1}.png")) for i in range(len(btn_coors))]
        self._btns = []
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
    
    def place_notations(self):
        self._canvas.create_rectangle(841.0, 823.0, 861.0, 843.0, fill="#EE4537", outline="")
        self._canvas.create_text(865.0, 821.0,
            anchor="nw",
            text="HUNGRY",
            fill="#000000",
            font=("Lato Bold", 20 * -1)
        )

        self._canvas.create_rectangle(1151.0, 823.0, 1171.0, 843.0, fill="#B7AC44", outline="")
        self._canvas.create_text(1175.0, 821.0,
            anchor="nw",
            text="EATING",
            fill="#000000",
            font=("Lato Bold", 20 * -1)
        )

        self._canvas.create_rectangle(989.0, 823.0, 1009.0, 843.0, fill="#FFC300", outline="")
        self._canvas.create_text(1013.0, 821.0,
            anchor="nw",
            text="THINKING",
            fill="#000000",
            font=("Lato Bold", 20 * -1)
        )

if __name__ == "__main__":
    gui = GUI()
    gui.default_build()