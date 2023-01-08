# this is a class that will model an elliptic curve over a finite field with P elements
import math
import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse
from matplotlib.patches import Circle
from matplotlib.patches import Rectangle
from matplotlib.patches import Polygon
from matplotlib.patches import Arc
from matplotlib.patches import FancyArrowPatch
from matplotlib.patches import FancyBboxPatch
from matplotlib.patches import FancyArrowPatch
from matplotlib.patches import FancyBboxPatch
from matplotlib.patches import FancyArrowPatch

class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a 
        self.b = b
        self.p = p
        self.points = [] # which will be a list of points on the curve 
        self.number_of_points = 0
        if self.is_valid():
            self.generate_points()
            self.draw()
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
        if 4*self.a**3 + 27*self.b**2 != 0:
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
            # we use the multiplicative inverse function to find the inverse of 2y1
            # we want to reduce to modulo p to get them in the range of 0 to p - 1
            m = ((3*x1**2 + self.a) * self.multiplicative_inverse(2*y1)) % self.p
        else:
            m = ((y2 - y1) * self.multiplicative_inverse(x2 - x1)) % self.p

        x3 = (m**2 - x1 - x2) 
        y3 = (m*(x1 - x3) - y1) 
        return (x3 % self.p, y3 % self.p)
    
    def multiply(self, p, n):
        r = (None, None)
        for i in range(n):
            r = self.add(r, p)
        return r
    
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
        

        
        # show the plot
        plt.show()

ec = EllipticCurve(317689081251325503476317476413827693272746955927, 79052896607878758718120572025718535432100651934, 785963102379428822376694789446897396207498568951)









