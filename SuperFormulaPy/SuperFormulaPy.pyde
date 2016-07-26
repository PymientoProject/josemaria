add_library('controlP5')

#ControlP5 cp5

angulo = 0
incremento = 1
a = 1
b = 1
m = 7
n1 = 10
n2 = 6
n3 = 6
radio = 128
grosor = 6
# Proporcion de la pantalla dedicada a los controles
tamGuiX= 0.150
# cp5 = ControlP5(this)  
#sradio = Slider(cp5,"Radio")

#Slider sradio,sm,sn1,sn2,sn3

def setup():
    fullScreen()
    h = int(height * .03)
    w = int(width * tamGuiX)
    sep = int( height * .04)
    background(0)
    stroke(255)
    smooth()
    cp5 = ControlP5(this)  
    global sradio
    p = createFont("Verdana",9)

    cp5.setColorForeground(0xffaa0000)
    cp5.setColorBackground(0xff660000)
    cp5.setColorValueLabel(0xffff88ff)
    cp5.setColorActive(0xffff0000)
  
    sradio = Slider(cp5,"Radio")
    sradio.setPosition(10.0,sep*1).setSize(w,h).setRange(0,255).setValue(128)
  
    cp5.addSlider("A",0,50,1,10,sep*2,w,h).setNumberOfTickMarks(51).snapToTickMarks(True).showTickMarks(False)
    cp5.addSlider("B",0,50,1,10,sep*3,w,h).setNumberOfTickMarks(51).snapToTickMarks(True).showTickMarks(False)

    sm = Slider(cp5,"M")
    sm.setPosition(10,sep*4).setSize(w,h).setRange(0,25).setValue(7).setNumberOfTickMarks(251).snapToTickMarks(True).showTickMarks(False)

    sn1 = Slider(cp5,"N1")
    sn1.setPosition(10,sep*5).setSize(w,h).setRange(0,25).setValue(10).setNumberOfTickMarks(101).snapToTickMarks(True).showTickMarks(False)
    sn2 = Slider(cp5,"N2")
    sn2.setPosition(10,sep*6).setSize(w,h).setRange(0,25).setValue(6).setNumberOfTickMarks(101).snapToTickMarks(True).showTickMarks(False)
    sn3 = Slider(cp5,"N3")
    sn3.setPosition(10,sep*7).setSize(w,h).setRange(0,25).setValue(6).setNumberOfTickMarks(101).snapToTickMarks(True).showTickMarks(False)


    cp5.addSlider("M",0,25,7,10,sep*4,w,h).setNumberOfTickMarks(251).snapToTickMarks(True).showTickMarks(False)
    cp5.addSlider("N1",0,10,10,10,sep*5,w,h).setNumberOfTickMarks(101).snapToTickMarks(True).showTickMarks(False)
    cp5.addSlider("N2",0,10,6,10,sep*6,w,h).setNumberOfTickMarks(101).snapToTickMarks(True).showTickMarks(False)
    cp5.addSlider("N3",0,10,6,10,sep*7,w,h).setNumberOfTickMarks(101).snapToTickMarks(True).showTickMarks(False)
    cp5.addSlider("Grosor",0,50,6,10,sep*8,w,h).setNumberOfTickMarks(51).snapToTickMarks(True).showTickMarks(False)

    cp5.addButton("ejemplo 1",1).setPosition(10,sep*10).setSize(w,h)
    cp5.addButton("ejemplo 2",1).setPosition(10,sep*11).setSize(w,h)
    cp5.addButton("ejemplo 3",1).setPosition(10,sep*12).setSize(w,h)
    cp5.addButton("ejemplo 4",1).setPosition(10,sep*13).setSize(w,h)
    cp5.addButton("ejemplo 5",1).setPosition(10,sep*14).setSize(w,h)
    cp5.addButton("ejemplo 6",1).setPosition(10,sep*15).setSize(w,h)


def draw():
    global angulo, a, b, m, n1,n2,n3,radio,grosor,tamGuiX
#    float ang,prim,seg,tot,xx,xxx,yy
#cada vuelta se aumenta en grados
#    print a,b,m,n1,n2,n3,radio,grosor
    ang = m * angulo /4 * TWO_PI/ 360
  
    prim = pow(abs(cos(ang/a)),n2)
    seg = pow(abs(sin(ang/b)),n3)

    tot = pow (prim+seg,-(1/n1)) * radio
    xx = tot*cos(angulo*TWO_PI/360)
    yy = tot*sin(angulo*TWO_PI/360)
    
#    print angulo, ang,prim,seg,tot,xx,yy
    strokeWeight(grosor)
    point(xx+ width*(1+tamGuiX)/2,yy+height/2)
  
    angulo = angulo + incremento;


def controlEvent(theEvent):
    global angulo, a, b, m, n1,n2,n3,radio,grosor,incremento,sradio
    print "principio del evento"
    if(theEvent.isController()):
        print "entra en controler"
        if(theEvent.getController().getName()=="Radio"):
            radio = theEvent.getController().getValue() 
            incremento = 128/radio
            print radio
        if(theEvent.getController().getName()=="A"):
            a = theEvent.getController().getValue()
        if(theEvent.getController().getName()=="B"):
            b = theEvent.getController().getValue()
        if(theEvent.getController().getName()=="M"):
            m = theEvent.getController().getValue()
        if(theEvent.getController().getName()=="N1"):
            n1 = theEvent.getController().getValue()
        if(theEvent.getController().getName()=="N2"):
            n2 = theEvent.getController().getValue()
        if(theEvent.getController().getName()=="N3"):
            n3 = theEvent.getController().getValue()
        if(theEvent.getController().getName()=="Grosor"):
            grosor = theEvent.getController().getValue()
        if(theEvent.getController().getName()=="ejemplo 1"):
            setValores(5,2,7,7)
        if(theEvent.getController().getName()=="ejemplo 2"):
            setValores(6,1,7,8)
        if(theEvent.getController().getName()=="ejemplo 3"):
            setValores(5,1,1,1)
        if(theEvent.getController().getName()=="ejemplo 4"):
            setValores(7,2,8,4)
        if(theEvent.getController().getName()=="ejemplo 5"):
            setValores(8,.5,.5,8)
        if(theEvent.getController().getName()=="ejemplo 6"):
            setValores(16,.5,.5,16)
    background(0)
    angulo = 0
    
  


def setValores(self,setm,setn1,setn2,setn3):
    sm.setValue(setm)
    sn1.setValue(setn1)
    sn2.setValue(setn2)
    sn3.setValue(setn3)
