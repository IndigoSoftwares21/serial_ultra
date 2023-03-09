const int trigPin = 2;
const int echoPin = 3;

long duration;
int distance;

bool intruder = false;

void setup() {
  // put your setup code here, to run once:
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
}


void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance= duration*0.034/2;
  if(distance<50 && intruder == false)
  {
    Serial.println("DESKTOP");
    intruder = true;
    delay(300);
  }
  else if(distance>50 && intruder == true){
      Serial.println("APP");
      intruder = false;
      delay(300);
  }
  
  // Serial.print("Distance: ");
  // Serial.println(distance);
}