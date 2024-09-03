#include "max6675.h"

float temperatura1 = 0, temperatura2 = 0, temperatura3 = 0, temperatura4 = 0;

//Pines para los módulos MAX6675
int ktcSO = 11;  //Compartido para todos los módulos
int ktcCLK = 13; //Compartido para todos los módulos
int ktcCS1 = 12;
int ktcCS2 = 10;
int ktcCS3 = 9;
int ktcCS4 = 8;

int relayPin1 = 3;
int relayPin2 = 4;
int relayPin3 = 5;
int relayPin4 = 6;

//Pines para los botones de activación
int botonPin1 = 7; 
int botonPin2 = 2; 

MAX6675 ktc1(ktcCLK, ktcCS1, ktcSO);
MAX6675 ktc2(ktcCLK, ktcCS2, ktcSO);
MAX6675 ktc3(ktcCLK, ktcCS3, ktcSO);
MAX6675 ktc4(ktcCLK, ktcCS4, ktcSO);

void setup() {
  Serial.begin(9600);
  delay(500);

  pinMode(relayPin1, OUTPUT);
  pinMode(relayPin2, OUTPUT);
  pinMode(relayPin3, OUTPUT);
  pinMode(relayPin4, OUTPUT);

  pinMode(botonPin1, INPUT_PULLUP);
  pinMode(botonPin2, INPUT_PULLUP);
}

void loop() {
  //Leer las temperaturas
  temperatura1 = ktc1.readCelsius();
  temperatura2 = ktc2.readCelsius();
  temperatura3 = ktc3.readCelsius();
  temperatura4 = ktc4.readCelsius();

  // Leer el estado del botón
  int estadoBoton1 = digitalRead(botonPin1);
  int estadoBoton2 = digitalRead(botonPin2);

  //Controlar los relevadores COMPRESIÓN
  if (estadoBoton1 == LOW) { // Botón presionado
    digitalWrite(relayPin1, HIGH);
    digitalWrite(relayPin2, HIGH);
  } else { // Botón suelto
    if (temperatura1 >= 60) {
      digitalWrite(relayPin1, LOW);
    } else {
      digitalWrite(relayPin1, HIGH);
    }
    
    if (temperatura2 >= 60) {
      digitalWrite(relayPin2, LOW);
    } else {
      digitalWrite(relayPin2, HIGH);
    }
  }


  //Controlar los relevadores COCCIÓN
  if (estadoBoton2 == LOW) { // Botón presionado
    digitalWrite(relayPin3, HIGH);
    digitalWrite(relayPin4, HIGH);
  } else { // Botón suelto
    if (temperatura3 >= 180) {
      digitalWrite(relayPin3, LOW);
    } else {
      digitalWrite(relayPin3, HIGH);
    }
    
    if (temperatura4 >= 180) {
      digitalWrite(relayPin4, LOW);
    } else {
      digitalWrite(relayPin4, HIGH);
    }
  }
  
  //Mostrar temps en puerto serial
  Serial.print("Temperatura 1: ");
  Serial.print(temperatura1);
  Serial.println(" C");
  
  Serial.print("Temperatura 2: ");
  Serial.print(temperatura2);
  Serial.println(" C");
  
  Serial.print("Temperatura 3: ");
  Serial.print(temperatura3);
  Serial.println(" C");
  
  Serial.print("Temperatura 4: ");
  Serial.print(temperatura4);
  Serial.println(" C");
  
  Serial.println("--------------------");
  
  delay(5000);
}
