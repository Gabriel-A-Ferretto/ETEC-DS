

int sensor = 0;
int valor = 0;

void setup(){
  pinModel(10, OUTPUT);
  Serial.begin(9600);
}

void loop(){
  int valor = analogRead(sensoor);
  Serial.println(valor);
  // o valro 500 devera ser ajustado conforme ambiente de teste
  if(valor < 500){
    digitalWrite(10, HIGH);
  }else {
    digitalWrite(10, LOW);
  }

  // altere o delay para leituras mais rapidas se necessario
  delay(500);
}