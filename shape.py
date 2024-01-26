# Auxiliary class to Line
class Point():
   def __init__(self, x, y):
      self.x = x
      self.y = y
   
class Line():
   def  __init__(self, point_a, point_b):
      self.__point_a =  point_a
      self.__point_b =  point_b
   
   def draw(self, canvas, fill_color):
      canvas.create_line(
         self.__point_a.x,
         self.__point_a.y,
         self.__point_b.x,
         self.__point_b.y,
         fill =  fill_color,
         width =  2,
      )
