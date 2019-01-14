import PIL.ImageDraw as ID, PIL.Image as Image, PIL.ImageShow as IS

im = Image.new("RGB", (640,480))
draw = ID.Draw(im)

def Bresenham(x1,y1,x2,y2):
    
    flag=0
    if(x1 > x2):
        x = x2
        y = y2
        xend = x1
        yend = y1
        startx = x
        starty = y
        
    elif(x1==x2):
        difference = abs(y1 - y2)
        if(y1>y2):
            y = y2
        else:
            y = y1
        for i in range(0,int(difference)):
            draw.point((x1, y),(255,255,255))
            y=y+1
        flag=1  
        
    else:
        x = x1
        y = y1
        xend = x2
        yend = y2
        startx = x
        starty = y

   
    while(flag != 1):
        slope = (float)(y2 - y1)/(float)(x2 - x1)
        yLine = (x - startx)*slope + starty
        diff = y - yLine
        if(diff >= 0.5):
            y=y-1
        elif(diff <= -0.5):
            y=y+1
        draw.point((x,y),(255,255,255))
        x=x+1
        if(x == xend + 1):
            flag = 1


draw.polygon(((10,10),(100,10),(100,100),(10,100)),outline=(255,255,255))
Bresenham(10,55,55,10)
Bresenham(10,55,55,100)
Bresenham(100,55,55,100)
Bresenham(100,55,55,10)
im.show()

    
