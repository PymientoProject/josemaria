import controlP5.*;

ControlP5 cp5;

float angulo = 0;
float incremento = 1; // aumento en grados
float a =1;
float b =1;
float m =7;
float n1 =10;
float n2 =6;
float n3 =6;
float radio = 128;
float grosor = 6;
// Proporcion de la pantalla dedicada a los controles
float tamGuiX= 0.150;

Slider sradio,sm,sn1,sn2,sn3;

void setup(){
//  size (800,600);
  fullScreen();
  int h = int(height * .03);
  int w = int(width * tamGuiX);
  int sep = int( height * .04);
  background(0);
  stroke(255);
  smooth();
  cp5 = new ControlP5(this);
  
  PFont p = createFont("Verdana",9); 
//  cp5.setControlFont(p);
  
  // change the original colors
  cp5.setColorForeground(0xffaa0000);
  cp5.setColorBackground(0xff660000);
//  cp5.setColorLabel(0xffdddddd);
  cp5.setColorValueLabel(0xffff88ff);
  cp5.setColorActive(0xffff0000);
  
  sradio = new Slider(cp5,"Radio");
  sradio.setPosition(10.0,sep*1).setSize(w,h).setRange(0,255).setValue(128);
  
  cp5.addSlider("A",0,50,1,10,sep*2,w,h).setNumberOfTickMarks(51).snapToTickMarks(true).showTickMarks(false);
  cp5.addSlider("B",0,50,1,10,sep*3,w,h).setNumberOfTickMarks(51).snapToTickMarks(true).showTickMarks(false);

  sm = new Slider(cp5,"M");
  sm.setPosition(10,sep*4).setSize(w,h).setRange(0,25).setValue(7).setNumberOfTickMarks(251).snapToTickMarks(true).showTickMarks(false);

  sn1 = new Slider(cp5,"N1");
  sn1.setPosition(10,sep*5).setSize(w,h).setRange(0,25).setValue(10).setNumberOfTickMarks(101).snapToTickMarks(true).showTickMarks(false);
  sn2 = new Slider(cp5,"N2");
  sn2.setPosition(10,sep*6).setSize(w,h).setRange(0,25).setValue(6).setNumberOfTickMarks(101).snapToTickMarks(true).showTickMarks(false);
  sn3 = new Slider(cp5,"N3");
  sn3.setPosition(10,sep*7).setSize(w,h).setRange(0,25).setValue(6).setNumberOfTickMarks(101).snapToTickMarks(true).showTickMarks(false);


  //cp5.addSlider("M",0,25,7,10,sep*4,w,h).setNumberOfTickMarks(251).snapToTickMarks(true).showTickMarks(false);
  //cp5.addSlider("N1",0,10,10,10,sep*5,w,h).setNumberOfTickMarks(101).snapToTickMarks(true).showTickMarks(false);
  //cp5.addSlider("N2",0,10,6,10,sep*6,w,h).setNumberOfTickMarks(101).snapToTickMarks(true).showTickMarks(false);
  //cp5.addSlider("N3",0,10,6,10,sep*7,w,h).setNumberOfTickMarks(101).snapToTickMarks(true).showTickMarks(false);
  cp5.addSlider("Grosor",0,50,6,10,sep*8,w,h).setNumberOfTickMarks(51).snapToTickMarks(true).showTickMarks(false);
//  Button ejemp1 = new Button(cp5,"Ejemplo 1"); 
  cp5.addButton("ejemplo 1",1).setPosition(10,sep*10).setSize(w,h);
  cp5.addButton("ejemplo 2",1).setPosition(10,sep*11).setSize(w,h);
  cp5.addButton("ejemplo 3",1).setPosition(10,sep*12).setSize(w,h);
  cp5.addButton("ejemplo 4",1).setPosition(10,sep*13).setSize(w,h);
  cp5.addButton("ejemplo 5",1).setPosition(10,sep*14).setSize(w,h);
  cp5.addButton("ejemplo 6",1).setPosition(10,sep*15).setSize(w,h);
  
  
  
  }

void draw(){
  float ang,prim,seg,tot,xx,xxx,yy;
  // cada vuelta se aumenta en grados
  ang = m * angulo /4 * TWO_PI/ 360;
  
  prim = pow(abs(cos(ang/a)),n2);
  seg = pow(abs(sin(ang/b)),n3);

  tot = pow (prim+seg,-(1/n1)) * radio;
  xx = tot*cos(angulo*TWO_PI/360);
  yy = tot*sin(angulo*TWO_PI/360);
  strokeWeight(grosor);
  point(xx+ width*(1+tamGuiX)/2,yy+height/2);
  
  //println(tot);
  angulo = angulo + incremento;
}
void controlEvent(ControlEvent theEvent) {
  
  if(theEvent.isController()) { 
    
//    print("control event from : "+theEvent.getController().getName());
//    println(", value : "+theEvent.getController().getValue());
    
    if(theEvent.getController().getName()=="Radio") {
      radio = theEvent.getController().getValue(); 
      incremento = 128/radio;}
    if(theEvent.getController().getName()=="A") {
      a = theEvent.getController().getValue(); }
    if(theEvent.getController().getName()=="B") {
      b = theEvent.getController().getValue(); }
    if(theEvent.getController().getName()=="M") {
      m = theEvent.getController().getValue();
//      m = m/10; 
//      theEvent.getController().setValue(m);   
          }
    if(theEvent.getController().getName()=="N1") {
      n1 = theEvent.getController().getValue(); }
    if(theEvent.getController().getName()=="N2") {
      n2 = theEvent.getController().getValue(); }
    if(theEvent.getController().getName()=="N3") {
      n3 = theEvent.getController().getValue(); }
    if(theEvent.getController().getName()=="Grosor") {
      grosor = theEvent.getController().getValue(); }
    if(theEvent.getController().getName()=="ejemplo 1") {
      setValores(5,2,7,7);}
    if(theEvent.getController().getName()=="ejemplo 2") {
      setValores(6,1,7,8);}
    if(theEvent.getController().getName()=="ejemplo 3") {
      setValores(5,1,1,1);}
    if(theEvent.getController().getName()=="ejemplo 4") {
      setValores(7,2,8,4);}
    if(theEvent.getController().getName()=="ejemplo 5") {
      setValores(8,.5,.5,8);}
    if(theEvent.getController().getName()=="ejemplo 6") {
      setValores(16,.5,.5,16);}
    
    background(0);
    angulo = 0;
    
  }
}

void setValores(float setm, float setn1, float setn2, float setn3){
        sm.setValue(setm) ; sn1.setValue(setn1) ; sn2.setValue(setn2); sn3.setValue(setn3);
}

