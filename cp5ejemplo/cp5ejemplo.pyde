add_library('controlP5')
# cp5 = ControlP5(this)  
#sradio = Slider(cp5,"Radio")
#Slider sradio,sm,sn1,sn2,sn3

radio = 100

def setup():
    # print "Comienza"
    size (400,300)
    # background(0)
    stroke(255)
    smooth()
    cp5 = ControlP5(this)  
    global sradio
    
    sradio = Slider(cp5,"Radio")
    sradio.setPosition(10.0,10).setSize(50,10).setRange(0,255).setValue(128)
    cp5.addButton("ejemplo 1",1).setPosition(10,40).setSize(50,10)

    cp5.addCallback(controlDelEvento)

def draw():
    background(0)
    strokeWeight(6)
    ellipse (width/2, height/2,radio,radio)

def controlDelEvento(evento):
    global radio
    
    ''' 
    print "Principio del callback"
    print "El controlador señalado es:"
    evn = evento.getController()
    print evn
    print evn.getValue()
    '''    
    if (evento.getAction()==ControlP5.ACTION_RELEASE) :
        nombre = evento.getController().getName()
        if (nombre == "Radio"):
            radio = float(int(evento.getController().getValue()))
            
        # print evento.getController().getValue()
        background(0)
        angulo = 0
