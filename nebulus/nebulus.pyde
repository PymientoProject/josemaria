
angulo =  0
incremento = 1
a = 1
b = 1
m = 7
n1 = 10
n2 = 6
n3 = 6
radio = 128
tarjeta = True
agujero=[]
cero = 1.0
colorin = color (255,255,255)
gris = color (50,50,50,1)
transp = 5
rangulo =0
incrangulo =0
tradio = 0

def setup():
    global agujero,cero,rangulo,tradio,incrangulo
    cero =(width/2.0)-200.0 
    # fullScreen()
    size(800,600)
    background(0)
    for agu in range(0,31):
        agujero.append(False)
    rangulo = random(360)
    tradio = random (10,100)
    incrangulo = random (-1.0,1.0)
    
    
def draw():
    
    global cero
    
    if tarjeta :
        pintatar()
    else :
        pinta3()
                
def pintatar():
    global cero
    background(0)
    fill(255)
    stroke(0)
    
    fill(0,200,0)
    ellipse (width-70,height-70,40,40)
    fill(255)
    rect (cero,0,400,height)
    for ver in range(0,5):
        for hor in range(0,6):
            if agujero[ver*6+hor]== False :
                fill(100)
            else:
                fill(0)
            ellipse((hor+1)*60+cero,(ver+3)*60,40,40)
            
def pinta3():
    global angulo, colorin,rangulo,incrangulo
    blendMode(BLEND)
    ang = m * angulo /4 * TWO_PI/ 360
    prim = pow(abs(cos(ang/a)),n2)
    seg = pow(abs(sin(ang/b)),n3)
    tot = pow(prim+seg,-(1.0/n1)) * radio
   
    xx = tot*cos(angulo*TWO_PI/360)
    yy = tot*sin(angulo*TWO_PI/360)
    
    strokeWeight(2)
    punx = xx+ width/2
    puny = yy+height/2
    clr = 255 - angulo/10
    stroke (colorin)
#    point(punx,puny)
    punb = punx + radio * cos(radians(angulo*1.5))
    punc = puny + radio * sin(radians(angulo*1.5))
    pund = punb + tradio * cos(radians(rangulo*3.5))
    pune = punc + tradio * sin(radians(rangulo*3.5))
    line (punb,punc,pund,pune)
    
    if (angulo%360 == 0):
        colorin = blendColor(colorin, gris, ADD)
    
    angulo = angulo + incremento
    rangulo = rangulo + incrangulo
            
def mouseClicked():
    global tarjeta
    x = int(((mouseX -cero-30)/60) )
    y = int((mouseY-150)/60)
    if y*6+x > 30:
        tarjeta = not tarjeta
        pasadatos()
        background(0)
    else :
        agujero[y*6+x] = not agujero[y*6+x]
        print "Mouse clicked"
    
def pasadatos():
    global m,n1,n2,n3,colorin,transp
  
    if agujero[0]==True :
        m = 7
        colorin = color(0,0,200,transp)
        transp =20
    if agujero[1]==True :
        m = 9
    if agujero[2]==True :
        m = 11
    if agujero[3]==True :
        m = 13
        transp =15
    if agujero[4]==True :
        m = 15        
    if agujero[5]==True :
        m = 5
        colorin = color(0,0,200,transp)
    if agujero[6]==True :
        n1 = 1
        transp =25
    if agujero[7]==True :
        n1 = 3
    if agujero[8]==True :
        n1 = 7
    if agujero[9]==True :
        n1 = 9
        transp =35
    if agujero[10]==True :
        n1 = 0.5
    if agujero[11]==True :
        n1 = 16
    if agujero[12]==True :
        n2 = 1
    if agujero[13]==True :
        n2 = 3
    if agujero[14]==True :
        n2 = 7
        transp =40
    if agujero[15]==True :
        n2 = 9
    if agujero[16]==True :
        n2 = 0.5
    if agujero[17]==True :
        n2 = 16
        transp =30
    if agujero[18]==True :
        n3 = 1
    if agujero[19]==True :
        n3 = 3
    if agujero[20]==True :
        n3 = 7
    if agujero[21]==True :
        n3 = 9
    if agujero[22]==True :
        n3 = 0.5
    if agujero[23]==True :
        n3 = 16
    if agujero[24]==True :
        colorin = color(200,0,0,transp)
    if agujero[26]==True :
        colorin = color(0,200,0,transp)
    if agujero[26]==True :
        colorin = color(0,0,200,transp)
    if agujero[27]==True :
        colorin = color(150,200,0,transp)
    if agujero[28]==True :
        colorin = color(200,0,200,transp)
    if agujero[29]==True :
        colorin = color(0,150,200,transp)
    if agujero[30]==True :
        colorin = color(200,100,100,transp)                                                                      