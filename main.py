import window
import shape

def main():
   win = window.Window(1920, 1080)

   cell1 = shape.Cell(30, 30, 200, 200, True, True, True, False)
   cell2 = shape.Cell(100, 100, 500, 500, True, False, True, False)
   cell3 = shape.Cell(150, 50, 250, 200, True, True, True, True)

   win.draw_cell(cell1,"black")
   win.draw_cell(cell2,"blue")
   win.draw_cell(cell3,"red")

   win.wait_for_close() 

if __name__  ==  "__main__":
    main()

