import window
import shape

def main():
   win = window.Window(800, 600)

   point_a = shape.Point(0,0)
   point_b = shape.Point(300,300)

   line = shape.Line(point_a, point_b)

   win.draw_line(line,"black")
   win.wait_for_close() 

if __name__  ==  "__main__":
    main()


