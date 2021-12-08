import svgutils.transform as sg
from svgutils.compose import *

pi_scale = 3.1415926535897932384626433832795028841971693993751058209

t = SVG("./x.svg")
tw = t.width
th = t.height

myfigure = Figure(tw, th, 
                  t,
                  ).scale(pi_scale).move(50,50).rotate(45,75,75)

myfigure.save('./new.svg')