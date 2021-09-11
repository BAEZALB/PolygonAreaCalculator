import math

class Rectangle:
  def __init__(self, width, height):
    self.set_height(height)
    self.set_width(width)

  def __str__(self):
    return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height
  
  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5
  
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."

    picture = ""

    for i in range (self.height):
      picture += "*" * self.width
      picture += "\n"

    return picture

  def get_amount_inside(self, shape):
    return math.floor(self.height / shape.height) * math.floor(self.width / shape.width)

class Square(Rectangle):
  def __init__(self, width):
    Rectangle.__init__(self, width, width)

  def __str__(self):
    return "Square(side=" + str(self.width) + ")"

  def set_side(self, side):
    Rectangle.set_height(self, side)
    Rectangle.set_width(self, side)