# this is a class that will model an elliptic curve over a finite field with P elements where you can draw, add points and double points on the curve
import matplotlib.pyplot as plt
import numpy as np

class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a 
        self.b = b
        self.p = p
        self.points = [] # which will be a list of points on the curve 
        self.number_of_points = 0
        if self.is_valid():
            self.generate_points()
        else:
            print("This is not a valid elliptic curve")

    def reset(self):
        self.points = []
    
    # a function which generate a list of points on the curve
    # any point on the curve satisfies the equation y^2 = x^3 + ax + b
    def generate_points(self):
        for x in range(self.p):
            for y in range(self.p):
                if (y**2 - x**3 - self.a*x - self.b) % self.p == 0:
                    self.points.append((x,y))
        # add the point at infinity
        self.points.append((None, None))
        self.number_of_points = len(self.points)

    def print_points(self):
        print(self.points, self.number_of_points)

    # check if its a valid elliptic curve by checking if the discriminant is not 0 4a^3 + 27b^2 != 0
    def is_valid(self):
        if (4*self.a**3 + 27*self.b**2)  != 0:
            return True
        else:
            return False

    def multiplicative_inverse(self, a):
        return pow(a, self.p - 2, self.p)

    # a function which adds two points on the curve 
    def add(self, p1, p2):
        # if one of the points is the point at infinity, return the other point
        if p1 == (None, None):
            return p2
        if p2 == (None, None):
            return p1
        x1, y1 = p1
        x2, y2 = p2
        # if the points are the same, we return the point at infinity
        if x1 == x2 and y1 != y2:
            return (None, None)
        # if the points are the same, then its the slope of the tangent line
        if x1 == x2:
            # we want to reduce to modulo p to get them in the range of 0 to p - 1
            m = ((3*x1**2 + self.a) * self.multiplicative_inverse(2*y1)) % self.p
        else:
            m = ((y2 - y1) * self.multiplicative_inverse(x2 - x1)) % self.p

        x3 = (m**2 - x1 - x2) 
        y3 = (m*(x1 - x3) - y1) 
        return (x3 % self.p, y3 % self.p)
    
    def point_doubling(self, g, n):
        # if n is 0, we return the point at infinity
        if n == 0:
            return (None, None)
        # if n is 1, we return the point g
        if n == 1:
            return g
        # if n is even, we return the point g + g
        if n % 2 == 0:
            return self.point_doubling(self.add(g, g), n // 2)
        # if n is odd, we return the point g + g + g
        else:
            return self.add(g, self.point_doubling(self.add(g, g), (n - 1) // 2))

    def draw(self):
        # create a figure
        fig = plt.figure()
        ax = fig.add_subplot(111)
        # draw the curve
        # draw the points
        for point in self.points:
            if point != (None, None):
                ax.scatter(point[0], point[1], color = "red")
        # draw the point at infinity
        ax.scatter(None, None, color = "green")
        # set the axis limits
        ax.set_xlim(0, self.p)
        ax.set_ylim(0, self.p)

        # set the title
        ax.set_title("Elliptic Curve y^2 = x^3 + {}x + {} mod {}".format(self.a, self.b, self.p))
        ax.text(0.5, -0.1, "Number of points on the curve: {}".format(self.number_of_points), size = 12, ha = "center", transform = ax.transAxes)
        plt.xticks(np.arange(0, self.p, 1))
        plt.yticks(np.arange(0, self.p, 1))
        plt.tick_params(axis = "both", which = "major", labelsize = 8)
        plt.grid()
        plt.show()

if __name__ == "__main__":
    ec = EllipticCurve(90, 95, 80)
    double = ec.point_doubling((1, 5), 77)
    ec.draw()







