import svgutils.transform as sg
from svgutils.compose import *

pi_scale = 3.1415926535897932384626433832795028841971693993751058209

t = SVG("./x.svg")
tw = t.width
th = t.height

myfigure = Figure(tw*4, th*4, 
                  t,
                  ).scale(pi_scale).rotate(15,tw//2,th//2)

myfigure.save('./new.svg')