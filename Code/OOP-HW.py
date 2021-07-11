
# Fill in the Line class methods to accept coordinates as a pair of tuples
# and return the slope and distance of the line.

class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        # Formula is square root of  [ (x2 – x1)^2 + (y2 – y1)^2]

        X = self.coor2[0] - self.coor1[0]
        Y = self.coor2[1] - self.coor1[1]
        return (X*X + Y*Y) ** 0.5

    def slope(self):

        # Formula for slope  m = (y2 – y1)/(x2 – x1)

        X = self.coor2[0] - self.coor1[0]
        Y = self.coor2[1] - self.coor1[1]
        slope = Y / X

        return slope


# EXAMPLE OUTPUT
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print(li.distance())
# 9.433981132056603

print(li.slope())
1.6