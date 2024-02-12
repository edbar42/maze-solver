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

class Cell():
   # tl = top left   br = bottom right
   def __init__(
         self,
         tl_x,
         tl_y,
         br_x,
         br_y,
         has_left_wall,
         has_right_wall,
         has_top_wall,
         has_bottom_wall,
      ):

      self.has_left_wall = has_left_wall
      self.has_right_wall = has_right_wall
      self.has_top_wall = has_top_wall
      self.has_bottom_wall = has_bottom_wall
      self.__x1 = tl_x,
      self.__x2 = br_x,
      self.__y1 = tl_y,
      self.__y2 = br_y,
      self.center_x = (tl_x + br_x)/2
      self.center_y = (tl_y + br_y)/2
      self.center = Point(self.center_x,self.center_y)


   def draw(self, canvas, fill_color):
      if self.has_left_wall:
         top_left_point = Point(self.__x1, self.__y1)
         bottom_left_point = Point(self.__x1, self.__y2)
         left_wall = Line(top_left_point, bottom_left_point)
         left_wall.draw(canvas, fill_color)

      if self.has_right_wall:
         top_right_point = Point(self.__x2, self.__y1)
         bottom_right_point = Point(self.__x2, self.__y2)
         right_wall = Line(top_right_point, bottom_right_point)
         right_wall.draw(canvas, fill_color)

      if self.has_top_wall:
         top_left_point = Point(self.__x1, self.__y1)
         top_right_point = Point(self.__x2, self.__y1)
         top_wall = Line(top_left_point, top_right_point)
         top_wall.draw(canvas, fill_color)

      if self.has_bottom_wall:
         bottom_left_point = Point(self.__x1, self.__y2)
         bottom_right_point = Point(self.__x2, self.__y2)
         left_wall = Line(bottom_left_point, bottom_right_point)
         left_wall.draw(canvas, fill_color)

   def draw_path(self, to_cell, canvas, undo=False):
      # The undo flag wil be used to revert path colors
      # in a later implementation
      path = Line(self.center, to_cell.center)
      path.draw(canvas, "red")
