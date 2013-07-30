#!/usr/bin/python
import math
import time

class Wing(object):
    def __init__(self, a, b, x_init = 0.1, y_init = 0):
        self.x_init = x_init
        self.y_init = y_init
        self.x = x_init
        self.y = y_init
        self.a = a
        self.b = b

    def next_generation_arbitorary(self,x,y):
       x2 = y + (self.a * x) - (5.0/(x*x +1)) + (0.2*math.exp(-y*y)) + 6
       y2 = -self.b*x
       return (x2,y2)

    def next_generation(self):
        x,y = self.x, self.y
        self.x = y + (self.a * x) - (5.0/(x*x +1)) + (0.2*math.exp(-y*y)) + 6
        self.y = -self.b*x
        return None

    def run_print(self,n):
        for i in xrange(n):
            print (self.x, self.y)
            self.next_generation()
        return None

    def run_write(self,n,filename,delimiter = '\t'):
        f = file(filename,'a')
        for i in xrange(n):
            f.write("%lf%s%lf\n"%(self.x,delimiter,self.y))
            self.next_generation()
        f.close()
        return None

def main():
    a = input('input a\n> ')
    b = input('input b\n> ')
    wing = Wing(a,b)
    wing.run_write(50000,'wing-%f.%f.dat'%(a,b))
    print "done"


if __name__ == '__main__':
    main()
