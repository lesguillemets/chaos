#!/usr/bin/python
import math
import matplotlib.pyplot as plt

class Wing(object):
    def __init__(self, a, b, x_init = 0.1, y_init = 0):
        self.x_init = x_init
        self.y_init = y_init
        self.x = x_init
        self.y = y_init
        self.a = a
        self.b = b

    def reset(self):
        self.x = self.x_init
        self.y = self.y_init

    def set_x(self,x):
        self.x = x

    def set_y(self,y):
        self.y = y
    
    def set_a(self,a):
        self.a = a

    def set_b(self,b):
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

    def run_plot(self,n):
        x_coordinates = []
        y_coordinates = []
        for i in xrange(n):
            x_coordinates.append(self.x)
            y_coordinates.append(self.y)
            self.next_generation() 

        #plt.scatter(x_coordinates,y_coordinates,s=0.01,marker='.',c='b')
        plt.figure(dpi=200,figsize=(3.5,3.5))
        plt.plot(x_coordinates,y_coordinates,"b,")#,ms=1)
        plt.axis([-20,20,-20,20])
        plt.axis('equal')
        plt.show()
        """
        else:
            fig = plt.figure(dpi=200,figsize=(20,20))
            plt.plot(x_coordinates,y_coordinates,"b,")#,ms=0.1)
            plt.rc('xtick',labelsize=40)
            plt.rc('ytick',labelsize=40)
            plt.axis([-20,20,-20,20])
            plt.axis('equal')
            plt.axis('off')
            ax = fig.add_subplot(111)
            ax.text(-18,18,'%f,%f'%(self.a,self.b),fontsize=30)
            plt.savefig(filename,bbox_inches='tight') #pad_inches=0)
        """
        plt.close()
            
        return None

"""
def main():
    a = -1.77 #input('input a\n> ')
    b = 0.989 #input('input b\n> ')
    wing = Wing(a,b)
    wing.run_plot(100000,'plot.png')
    print "done"
"""
def main():
    a = -1.77 #input('input a\n> ')
    b = 0.989 #input('input b\n> ')
    for i in xrange(200):
        A = a+i/4000.0
        wing = Wing(A,b)
        wing.run_write(100000,'a.%lf.dat'%(A))
    print "done"


if __name__ == '__main__':
    main()
