add_library('controlP5')

matriz = []
#variables de los controles
r = 128
g = 128
b = 128
porcen = 60
c = 8
archivo1 = ""
archivo2 = ""
arch1 = None
arch2 = None

'''
# nombre de los controles
sr = None
sg = None
sb = None
sp = None
'''
lb =None

#variables del entorno
#tamaño y posicion del rectangulo

rectw = 0
recth = 0
rectx = 0
recty = 0

repintar = False
rellenarmatriz = False

tamGuiX= 0.150


def setup():
    global rectw,recth,btnr,arch1,arch2,lb
    # global sr,sg,sb,sp,

    fullScreen()
    background(0)
    strokeCap(PROJECT)
    noStroke()
    
    # Definicion GUI
    
    # reparto horizontal
    px =(1-tamGuiX)*width
    
    # tamaño rectangulo
    rectw = px -20
    recth = height -20
   
    puntoscol = 0
    
    # tamaño botones
    bw = int(tamGuiX*width) - 20    #el 20 para que quepa la letra
    bh = int(height * .03)
    # separacion de los botones
    sep = int( height * .04)

    
    fill(255)
    rectangulo(rectw,recth)
    
    cp5 =ControlP5(this)
    p = createFont("Verdana",11)
    cp5.setFont(p)
    
    cp5.setColorForeground(color(0,170,255)) #Azul claro
    cp5.setColorBackground(color(0,100,255)) #Azul
    cp5.setColorValueLabel(color(255,255,160)) # claro ¿amarillo? ver
    cp5.setColorActive(color(255,255,0))     #amarillo
    #cp5.setColorValue(color(255,255,255))
    
    checkbox = cp5.addCheckBox("checkBox").setPosition(px, sep).setSize(bh,bh).addItem("Aleatorio", 0)

     #cp5.addToggle("toggle")
     #.setPosition(px,sep)
     #.setSize(bh,bh)
     #.setValue(True)
     #.setMode(ControlP5.SWITCH)
     #.setMode(ControlP5.HORIZONTAL)
    
    sr = Slider(cp5,"R")
    sr.setPosition(px,sep*2).setSize(bw,bh).setRange(0,25).setValue(12).setNumberOfTickMarks(101).snapToTickMarks(True).showTickMarks(False)
    sg = Slider(cp5,"G")
    sg.setPosition(px,sep*3).setSize(bw,bh).setRange(0,25).setValue(12).setNumberOfTickMarks(101).snapToTickMarks(True).showTickMarks(False)
    sb = Slider(cp5,"B")
    sb.setPosition(px,sep*4).setSize(bw,bh).setRange(0,25).setValue(12).setNumberOfTickMarks(101).snapToTickMarks(True).showTickMarks(False)
    sp = Slider(cp5,"%")
    sp.setPosition(px,sep*5).setSize(bw,bh).setRange(0,100).setValue(60).setNumberOfTickMarks(101).snapToTickMarks(True).showTickMarks(False)
    sc = Slider(cp5,"C")
    sc.setPosition(px,sep*6).setSize(bw,bh).setRange(2,12).setValue(8).setNumberOfTickMarks(11).snapToTickMarks(True).showTickMarks(False)
    lb = Textfield(cp5,"")
    lb.setPosition(px,sep*9).setSize(bw,bh).setColorBackground(color(255,0,0)).setColorForeground(color(255,0,0))
    # cp5.addTextlabel("Archivo ").setPosition(px, sep*7).setSize(bw,bh).setText("ARCHIVO:")
    arch1 = Textfield(cp5,"Archivo").setPosition(px,sep*16).setSize(bw,bh)
    
    arch2 = Textfield(cp5,"Archivo3d").setPosition(px,sep*18).setSize(bw,bh)
    btnr = Button(cp5,"Dibujar").setPosition(px,sep*22).setSize(bw,bh).setColorBackground(color(255,0,0)).setColorForeground(color(255,100,100))
    btns = Button(cp5,"Guardar").setPosition(px,sep*24).setSize(bw,bh).setColorBackground(color(255,0,0)).setColorForeground(color(255,100,100))

    cp5.addCallback(controlDelEvento)
# Parte del programa     


 

def draw():
    '''
    global repintar,rellenarmatriz

    if (rellenarmatriz):  
        if (archivo1==""):
            rellenaMatriz()
        else :
            rellenadib()
        
        rellenarmatriz = False
    if (repintar):
        print "entro en repintar"
        cargaDibu()
        pintaMatriz()
        repintar = False
        
#    noLoop()
    
    
  pintaMatriz()    
//  imprime();
//  getsPuntos();
//  lineasRef();
//  salvaDibu();
    '''
    
def controlDelEvento(theEvent):
    global r,g,b,porcen,c,archivo2,archivo1
    
#    print "principio del evento"
        
    if(theEvent.getAction()==ControlP5.ACTION_RELEASE) :
#        print "se ha pulsado un control"
        ctrl = theEvent.getController()
        print "en el evento-",ctrl.getName()
        if(ctrl.getName()=="Dibujar"):
            archivo2=arch2.getText()
            lb.setVisible(True)
            redraw()
            dibuja()
        if(ctrl.getName()=="Guardar"):
            salvaDibu()
        if(ctrl.getName()=="R"):
            r = (theEvent.getController().getValue())*10
        if(ctrl.getName()=="G"):
            g = (theEvent.getController().getValue())*10
        if(ctrl.getName()=="B"):
            b = (theEvent.getController().getValue())*10
        if(ctrl.getName()=="%"):
            porcen =theEvent.getController().getValue()
            
           
        if(ctrl.getName()=="N3"):
            n3 = theEvent.getController().getValue()
        if(ctrl.getName()=="Grosor"):
            grosor = theEvent.getController().getValue()
        if(ctrl.getName()=="ejemplo 1"):
            setValores(5,2,7,7)
        if(ctrl.getName()=="ejemplo 2"):
            setValores(6,1,7,8)
        if(ctrl.getName()=="ejemplo 3"):
            setValores(5,1,1,1)
        if(ctrl.getName()=="ejemplo 4"):
            setValores(7,2,8,4)
        if(ctrl.getName()=="ejemplo 5"):
            setValores(8,.5,.5,8)
        if(ctrl.getName()=="ejemplo 6"):
            setValores(16,.5,.5,16)
        '''
        if(ctrl.getName()=="AGAP"):
            agapSal()
        btnagap.setVisible(False)
        '''    
  


# Funciones propias
def     rectangulo(w,h):
    global rectx, recty
    fill(255)
    rectx = ((1-tamGuiX)*width - w)/2
    recty = (height - h)/2
    rect(rectx,recty,w,h)

def dibuja():
    global lb
    
    lb.setText("Trabajando")
    redraw()
    print "dentro de dibuja"
    rectangulo(rectw,recth)
    rellenaMatriz()
    cargaDibu()
    pintaMatriz()
    
    #lb.setVisible(False)

def rellenaMatriz() :
    global matriz,puntoscol,porcen,r,g,b
#    print "Entro en rellena"
    j=0
    k=0
    matriz = []
    puntoscol = int(rectw/c) +1
    aa = puntoscol/2
    bb = recth/2

    
    while (j<=aa):
        m=[]
        k=0
        while (k<=bb):
            if (random(100)<porcen):
                m.append(color(random(40,r),random(40,g),random(40,b)))
            else:
                m.append(color(255,255,255))
            k=k+1
        matriz.append(m)
        j = j+1
    # print matriz

def rellenadib():
    pass

def pintaMatriz():
    global puntoscol
    columnas=0
    while (columnas<c):
        y =0
        while (y<recth):
            x=0
            while (x<puntoscol):
                gx=int (puntoscol*columnas+x+rectx)
                ge = get(gx,y+recty)              
                b = 10 - int(brightness(ge)/25.5)
                giraMatriz(x/2,y/2,b)
                fill(matriz[x/2][y/2])
                xx =(puntoscol*columnas+x) + rectx
                yy = y + recty
                rect(xx,yy,2,2)
                x=x+2
            y = y+2
        columnas = columnas +1

def cargaDibu():
  global archivo2
  print archivo2  
  if (archivo2==""):
      archivo2="pymiento.jpg"
      
  img = loadImage(archivo2)
  
  lx = (rectw - img.width)/2
  ly = (recth - img.height)/2

  image(img, lx, ly)

def salvaDibu():
    save ("3d"+archivo2)


def giraMatriz(x, y, b):
    global matriz
    xx = x;
    a=0;
    #  for (xx = x; xx <80;xx++){
    if (xx>(puntoscol/2-1-b)):
      a = xx- puntoscol/2
    else:
      a = xx
    matriz[x][y] = matriz[a+b][y]

def espera():
    t = millis()
    while (millis()-t<5000):
        print "espero en espera"

'''


//////// Depuration functions //////

void imprime(){
  int a;
  int b;
  int columnas;

  for (columnas=0; columnas<10; columnas++){
    for (a=0; a<600; a++){
      for (b=0; b<80; b++){
//        print (matriz[b][a]);
          print(80*columnas+b);
        print(" ");

      
      }
    }
  }
  println("final");
  
}

void getsPuntos(){
  println (gris);
  println (get(100,100));
  println (get(150,200));
}
void lineasRef(){
  int a=0;
  for (a= 1; a<11;a++){
    stroke(255,0,0);
    line(a*80,0,a*80,height);
  }
}
'''