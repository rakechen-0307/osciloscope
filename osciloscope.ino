int sensorpin = A2;
float trig = 0.5;

void setup()
{
    // put your setup code here, to run once:
    Serial.begin(2000000);
}

int count = 0; // count of the radio ray
float sensorval = 0;
float last_val = 0;

void loop()
{
    // measuring period
    unsigned long start_time = millis();
    while (true)
    {
        last_val = sensorval;
        sensorval = analogRead(sensorpin) * 5.0 / 1023.0;
        if (last_val < trig and sensorval >= trig)
        {
            count++;
            Serial.println(1);
        }
    }
    //  Serial.print("count: ");
    //  Serial.println(count);
    //  delay(2000);
}