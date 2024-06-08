import tkinter as tk


class Window():
    def __init__(self, width, height):
        self.__root = tk.Tk()
        self.__root.title = "Maze Solver"
        self.__root.protocol("WM_DELETE_WINDOW",  self.close)
        self.canvas = tk.Canvas()
        self.canvas.pack()
        self.__window_running = False

    def draw_cell(self, cell, fill_color):
        cell.draw(self.canvas, fill_color)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__window_running = True
        while (self.__window_running):
            self.redraw()

    def close(self):
        self.__window_running = False
