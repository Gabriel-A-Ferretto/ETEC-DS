int valor;

int vermelho = 10;
int azul = 9;
int verde = 6;

void setup()
{
  pinMode(vermelho, OUTPUT);
  pinMode(azul, OUTPUT);
  pinMode(verde, OUTPUT);
}

void setColor(int r, int g, int b){
  analogWrite(vermelho, r);
  analogWrite(verde, g);
  analogWrite(azul, b);
}

void loop(){
  valor = analogRead(A0);

  if (valor < 170){
    setColor(0, 255, 0); // verde
  }
  else if (valor < 340){
    setColor(0, 0, 255); // azul
  }
  else if (valor < 510){
    setColor(255, 0, 0); // vermelho
  }
  else if (valor < 680){
    setColor(255, 0, 255); // roxo
  }
  else if (valor < 850){
    setColor(0, 255, 255); // ciano
  }
  else {
    setColor(200, 200, 200); // branco suave
  }
}
