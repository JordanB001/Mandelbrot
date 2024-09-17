from math import sqrt

xmin = -2
xmax = 2
ymin = -2
ymax = 2

rangex = xmax-xmin
rangey = ymax-ymin

def setup():
    global xscl, yscl
    size(600,600)
    colorMode(HSB)
    
    noStroke()
    xscl = float(rangex)/width
    yscl = float(rangey)/height
    
def draw():
    #translate(width/2, height/2)
    
    for x in range(width):
        for y in range(height):
            z = [(xmin + x*xscl), (ymin + y*yscl)]
            
            col = mandelbrot(z,100)
            
            if col == 100:
                fill(0)
            else:
                fill(255)
            rect(x,y,1,1)
            
    

def complexAddition(z1,z2):
    return [z1[0]+z2[0],z1[1]+z2[1]]


def complexMultiplication(z1,z2):
    return [z1[0] * z2[0] - z1[1] * z2[1],z1[0] * z2[1] + z1[1] * z2[0]]

def valAbsolue(z):
    return sqrt(z[0]**2 + z[1]**2)
    
def mandelbrot(z, num):
    count = 0
    z1 = z
    
    while count <= num:
        if valAbsolue(z1) > 2.0:
            return count
        
        
        z1 = complexAddition(complexMultiplication(z1,z1),z)
        count += 1
    return num
