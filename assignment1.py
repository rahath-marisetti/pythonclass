hrs = raw_input("Enter Hours:")
h = float(hrs)
rpr = raw_input("Enter rate per hour:") 
r = float(rpr)
gross = h*r
if(h > 40):
    s =40*r
    f = h-40
    g = r*1.5
    newgross = s+(f*g)
    print newgross
    
else:
    print gross