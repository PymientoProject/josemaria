add_library('controlP5')

matriz = []
gris = color(100,100,100)
porcen = 60



def setup():

    size(800,600)
    fullScreen()
    background(255)
    strokeCap(PROJECT)
    noStroke()
    rellenaMatriz()
    cargaDibu()
 

def draw():
    noLoop()
    pintaMatriz()
'''    
//  imprime();
//  getsPuntos();
//  lineasRef();
//  salvaDibu();
'''

# Funciones propias

def rellenaMatriz() :
    global matriz
#    print "Entro en rellena"
    a=0
    b=0

    while (a<40):
        m=[]
        b=0
        while (b<300):
            if (random(100)<porcen):
                m.append(color(random(20,250),random(20,250),random(190)))
            else:
                m.append(color(255,255,255))
            b=b+1
        matriz.append(m)
        a = a+1
    # print matriz

def pintaMatriz():
    columnas=0
    while (columnas<10):
        y =0
        while (y<600):
            x=0
            while (x<80):
                ge = get(80*columnas+x,y)              
                b = 10 - int(brightness(ge)/25.5)
                giraMatriz(x/2,y/2,b)
                fill(matriz[x/2][y/2])
                xx =(80*columnas+x)
                # yy = y * 2 ;
                rect(xx,y,2,2)
                x=x+2
            y = y+2
        columnas = columnas +1

def cargaDibu():
    
  img = loadImage("pymiento.jpg")

  image(img, 0, 0)

'''
void salvaDibu(){
    save ("pymiento3D.jpg");
}
'''
def giraMatriz(x, y, b):
    global matriz
    xx = x;
    a=0;
    #  for (xx = x; xx <80;xx++){
    if (xx>(39-b)):
      a = xx- 40
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