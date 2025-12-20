/*
 * DXA Controller - Firmware para ESP32
 * Sistema de vibración adaptativa basado en datos DXA
 * 
 * ENTRADA: Datos DXA (densidad ósea, T-score)
 * SALIDA: Frecuencia optimizada a motor vibrador
 * 
 * Reemplaza acelerómetro por datos DXA para cálculo de frecuencia
 */

#include <Wire.h>

// Configuración del sistema
#define MOTOR_PWM_PIN 4      // Pin PWM para control de motor
#define DXA_DATA_READY_PIN 5 // Pin para señal de datos DXA disponibles

// Variables DXA (estas vendrían del sistema de análisis)
float bmd_value = 0.0;       // Densidad Mineral Ósea (g/cm²)
float t_score = 0.0;         // T-score del paciente
float z_score = 0.0;         // Z-score del paciente

// Variables de control
float optimal_frequency = 35.0;  // Frecuencia calculada (Hz)
float current_frequency = 35.0;  // Frecuencia actual del motor
float motor_intensity = 128;     // Intensidad PWM (0-255)

// Parámetros del paciente (para cálculo)
int patient_age = 50;
char patient_sex = 'F';          // 'M' o 'F'
float patient_bmi = 25.0;

void setup() {
  Serial.begin(115200);
  Serial.println("=== DXA VIBRATION CONTROLLER v1.0 ===");
  Serial.println("Sistema: Vibración optimizada por datos DXA");
  
  // Configurar pines
  pinMode(MOTOR_PWM_PIN, OUTPUT);
  pinMode(DXA_DATA_READY_PIN, INPUT);
  
  // Inicializar I2C para comunicación con módulo DXA (si aplica)
  Wire.begin();
  
  Serial.println("Controlador inicializado - Esperando datos DXA...");
}

void loop() {
  // 1. Verificar si hay nuevos datos DXA disponibles
  if (checkForNewDXAData()) {
    readDXAData();          // Leer datos DXA
    calculateOptimalFrequency(); // Calcular frecuencia óptima
    updateMotorControl();   // Ajustar motor
    displaySystemStatus();  // Mostrar estado
  }
  
  // 2. Mantener frecuencia actual
  maintainVibration();
  
  delay(50); // Control cada 50ms
}

bool checkForNewDXAData() {
  // Simular recepción de datos DXA
  // En sistema real: comunicación serial/I2C/Bluetooth con sistema DXA
  static unsigned long last_update = 0;
  
  if (millis() - last_update > 5000) { // Cada 5 segundos (simulación)
    last_update = millis();
    
    // Generar datos DXA simulados (en real vendrían del equipo)
    bmd_value = random(800, 1200) / 1000.0; // 0.8-1.2 g/cm²
    t_score = random(-35, 5) / 10.0;       // -3.5 a +0.5
    z_score = random(-20, 20) / 10.0;      // -2.0 a +2.0
    
    return true;
  }
  return false;
}

void readDXAData() {
  Serial.println("\n--- NUEVOS DATOS DXA RECIBIDOS ---");
  Serial.print("BMD: "); Serial.print(bmd_value, 3); Serial.println(" g/cm²");
  Serial.print("T-score: "); Serial.println(t_score, 1);
  Serial.print("Z-score: "); Serial.println(z_score, 1);
}

void calculateOptimalFrequency() {
  // ALGORITMO: Calcular frecuencia basada en datos DXA
  
  // Frecuencia base según T-score (WHO classification)
  if (t_score <= -2.5) {
    // Osteoporosis: frecuencia más baja
    optimal_frequency = 40.0;
  } else if (t_score <= -1.0) {
    // Osteopenia: frecuencia media
    optimal_frequency = 45.0;
  } else {
    // Normal: frecuencia estándar
    optimal_frequency = 50.0;
  }
  
  // Ajustar por edad
  if (patient_age > 60) optimal_frequency -= 5.0;
  if (patient_age > 70) optimal_frequency -= 5.0;
  
  // Ajustar por sexo
  if (patient_sex == 'F') optimal_frequency += 2.0;
  
  // Limitar rango seguro (30-90 Hz)
  optimal_frequency = constrain(optimal_frequency, 30.0, 90.0);
  
  Serial.print("Frecuencia calculada: ");
  Serial.print(optimal_frequency);
  Serial.println(" Hz");
}

void updateMotorControl() {
  // Suavizar transición de frecuencia
  float frequency_step = 0.5; // Hz por ciclo
  
  if (current_frequency < optimal_frequency) {
    current_frequency += frequency_step;
  } else if (current_frequency > optimal_frequency) {
    current_frequency -= frequency_step;
  }
  
  // Convertir frecuencia a PWM (30-90 Hz → 0-255)
  motor_intensity = map((int)current_frequency, 30, 90, 100, 255);
  motor_intensity = constrain(motor_intensity, 100, 255);
  
  // Aplicar al motor
  analogWrite(MOTOR_PWM_PIN, motor_intensity);
}

void maintainVibration() {
  // Mantener frecuencia constante entre ajustes
  analogWrite(MOTOR_PWM_PIN, motor_intensity);
}

void displaySystemStatus() {
  Serial.print("Motor: ");
  Serial.print(current_frequency, 1);
  Serial.print(" Hz | PWM: ");
  Serial.println(motor_intensity);
  Serial.println("-----------------------------");
}

// Función para recibir datos DXA reales (ej: via Serial/Bluetooth)
void receiveRealDXAData(float bmd, float tscore, float zscore) {
  bmd_value = bmd;
  t_score = tscore;
  z_score = zscore;
  
  calculateOptimalFrequency();
  updateMotorControl();
}

// Función para configurar paciente
void setPatientProfile(int age, char sex, float bmi) {
  patient_age = age;
  patient_sex = sex;
  patient_bmi = bmi;
  Serial.println("Perfil paciente actualizado");
}
