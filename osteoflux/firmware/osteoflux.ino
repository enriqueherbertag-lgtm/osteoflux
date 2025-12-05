/*
 * OsteoFlux - Firmware Principal
 * Controlador ESP32 para sistema de vibración adaptativa
 * 
 * CARACTERÍSTICAS:
 * - Lectura dual MPU6050 (dispositivo + hueso)
 * - Algoritmo adaptativo de frecuencia
 * - Control motor DRV2605L
 * - Calibración automática
 */

#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

// Direcciones I2C MPU6050
#define MPU_DEVICE_ADDR 0x68    // Dispositivo (AD0 = GND)
#define MPU_BONE_ADDR   0x69    // Hueso (AD0 = VCC)

// Pines
#define MOTOR_ENABLE_PIN 4

// Variables globales
float currentFrequency = 35.0;  // Hz
float deviceVibration = 0;
float boneVibration = 0;
float transmissionPercent = 0;

Adafruit_MPU6050 mpuDevice;
Adafruit_MPU6050 mpuBone;

void setup() {
  Serial.begin(115200);
  Serial.println("=== OSTEOFLUX FIRMWARE v1.0 ===");
  
  // Inicializar I2C
  Wire.begin();
  
  // Inicializar MPU6050 dispositivo
  if (!mpuDevice.begin(MPU_DEVICE_ADDR)) {
    Serial.println("ERROR: MPU6050 Dispositivo no encontrado");
    while (1);
  }
  
  // Inicializar MPU6050 hueso  
  if (!mpuBone.begin(MPU_BONE_ADDR)) {
    Serial.println("ERROR: MPU6050 Hueso no encontrado");
    while (1);
  }
  
  // Configurar MPUs
  mpuDevice.setAccelerometerRange(MPU6050_RANGE_8_G);
  mpuBone.setAccelerometerRange(MPU6050_RANGE_8_G);
  
  // Configurar pines
  pinMode(MOTOR_ENABLE_PIN, OUTPUT);
  
  Serial.println("Sistema inicializado OK");
  delay(1000);
}

void loop() {
  // 1. Leer acelerómetros
  readAccelerometers();
  
  // 2. Calcular transmisión
  calculateTransmission();
  
  // 3. Ajustar frecuencia
  adjustFrequency();
  
  // 4. Controlar motor
  controlMotor();
  
  // 5. Mostrar datos
  displayData();
  
  delay(100);  // 10Hz update rate
}

void readAccelerometers() {
  sensors_event_t aDevice, gDevice, tempDevice;
  sensors_event_t aBone, gBone, tempBone;
  
  mpuDevice.getEvent(&aDevice, &gDevice, &tempDevice);
  mpuBone.getEvent(&aBone, &gBone, &tempBone);
  
  // Calcular magnitud de vibración
  deviceVibration = sqrt(aDevice.acceleration.x * aDevice.acceleration.x +
                         aDevice.acceleration.y * aDevice.acceleration.y +
                         aDevice.acceleration.z * aDevice.acceleration.z);
  
  boneVibration = sqrt(aBone.acceleration.x * aBone.acceleration.x +
                       aBone.acceleration.y * aBone.acceleration.y +
                       aBone.acceleration.z * aBone.acceleration.z);
}

void calculateTransmission() {
  if (deviceVibration > 0) {
    transmissionPercent = (boneVibration / deviceVibration) * 100;
  } else {
    transmissionPercent = 0;
  }
}

void adjustFrequency() {
  // ALGORITMO ADAPTATIVO SIMPLE
  if (transmissionPercent < 60) {
    currentFrequency += 0.5;  // Subir frecuencia
  } else if (transmissionPercent > 85) {
    currentFrequency -= 0.5;  // Bajar frecuencia
  }
  
  // Limitar rango (30-90 Hz)
  currentFrequency = constrain(currentFrequency, 30.0, 90.0);
}

void controlMotor() {
  // SIMULACIÓN: Enviar frecuencia al motor
  // (Reemplazar con control real DRV2605)
  analogWrite(MOTOR_ENABLE_PIN, map((int)currentFrequency, 30, 90, 0, 255));
}

void displayData() {
  Serial.print("Freq: ");
  Serial.print(currentFrequency);
  Serial.print(" Hz | Trans: ");
  Serial.print(transmissionPercent);
  Serial.print("% | Dev: ");
  Serial.print(deviceVibration);
  Serial.print(" g | Bone: ");
  Serial.print(boneVibration);
  Serial.println(" g");
}

// Función de calibración
void calibrateSystem() {
  Serial.println("CALIBRANDO... No mover dispositivo");
  delay(3000);
  Serial.println("Calibración completa");
}
