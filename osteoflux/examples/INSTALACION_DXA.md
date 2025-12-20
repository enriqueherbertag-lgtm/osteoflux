Guía de Instalación y Configuración del Sistema DXA + Vibración
1. Requisitos Previos
1.1. Hardware Requerido
Componentes Esenciales:
Unidad de Control ESP32

ESP32 DevKit v1 o equivalente

Conector USB-C para programación

Headers soldados para conexiones

Módulo Vibrador

LRA (Linear Resonant Actuator) 3V

DRV2605L Haptic Driver (recomendado)

Cables JST-PH 2-pin

Interfaz de Usuario

Pantalla OLED 0.96" 128×64 (I2C)

3× botones táctiles

Buzzer pasivo (opcional)

Alimentación

Fuente 5V 2A con conector DC

Batería 18650 + TP4056 (opcional)

Interruptor de potencia

Herramientas Necesarias:
Soldador y estaño

Alicates y cortadores

Multímetro digital

Osciloscopio (recomendado)

Impresora 3D (para carcasa, opcional)

1.2. Software Requerido
Para ESP32:
Arduino IDE 2.3+ o PlatformIO

ESP32 Board Support:

text
https://espressif.github.io/arduino-esp32/package_esp32_index.json
Bibliotecas:

Adafruit_SSD1306

Adafruit_GFX

ArduinoJSON

ESP32PWM

Para Análisis DXA:
Python 3.9+

Instalación de paquetes:

bash
pip install pydicom numpy pandas matplotlib scipy
pip install fastapi uvicorn  # Para API
2. Ensamblaje Hardware
2.1. Diagrama de Conexiones
text
ESP32 GPIO       Componente
---------       ----------
GPIO 21 (SDA) → OLED SDA
GPIO 22 (SCL) → OLED SCL
GPIO 4        → DRV2605L SDA
GPIO 15       → DRV2605L SCL
GPIO 18       → DRV2605L EN
GPIO 23       → Botón START
GPIO 19       → Botón STOP
GPIO 5        → Botón MENU
GPIO 2        → LED Status
GPIO 25       → Buzzer
VIN (5V)      → Alimentación componentes
GND           → Tierra común
2.2. Pasos de Ensamblaje
Paso 1: Preparar ESP32
bash
1. Soldar headers al ESP32 DevKit
2. Conectar cable USB para pruebas
3. Verificar que LED power se enciende
Paso 2: Conectar Display OLED
bash
1. Conectar SDA → GPIO 21
2. Conectar SCL → GPIO 22
3. Conectar VCC → 3.3V
4. Conectar GND → GND
5. Verificar con sketch de prueba OLED
Paso 3: Instalar DRV2605L y Motor
bash
1. Soldar DRV2605L a protoboard
2. Conectar I2C: SDA→GPIO4, SCL→GPIO15
3. Conectar EN → GPIO18
4. Conectar motor LRA a salida OUT+/OUT-
5. Conectar VDD → 3.3V, GND → GND
Paso 4: Conectar Botones
bash
1. Conectar botón START → GPIO23
2. Conectar botón STOP → GPIO19  
3. Conectar botón MENU → GPIO5
4. Todos con pull-down resistors 10kΩ
Paso 5: Alimentación
bash
1. Conectar fuente 5V a VIN del ESP32
2. Conectar interruptor en línea positiva
3. Verificar voltajes: 5V en VIN, 3.3V en salida
2.3. Pruebas Iniciales Hardware
Test 1: Alimentación
bash
1. Medir 5V en VIN del ESP32
2. Medir 3.3V en pin 3V3
3. Verificar que todos GND están conectados
Test 2: Comunicación I2C
arduino
// Ejecutar I2C Scanner
#include <Wire.h>
void setup() {
  Serial.begin(115200);
  Wire.begin();
}
void loop() {
  byte error, address;
  for(address=1; address<127; address++) {
    Wire.beginTransmission(address);
    error = Wire.endTransmission();
    if(error==0) Serial.print("Dispositivo: 0x"); Serial.println(address,HEX);
  }
  delay(5000);
}
Test 3: Motor Vibrador
arduino
// Test básico del motor
#include <Wire.h>
#include <Adafruit_DRV2605.h>
Adafruit_DRV2605 drv;

void setup() {
  drv.begin();
  drv.selectLibrary(1);
  drv.setMode(DRV2605_MODE_INTTRIG);
}

void loop() {
  drv.setWaveform(0, 14);  // Forma de onda básica
  drv.setWaveform(1, 0);   // Fin
  drv.go();
  delay(1000);
}
3. Instalación Software
3.1. Configurar Arduino IDE
Paso 1: Instalar soporte ESP32
text
1. Archivo → Preferencias → URLs adicionales:
   https://espressif.github.io/arduino-esp32/package_esp32_index.json
2. Herramientas → Placa → Gestor de tarjetas
3. Buscar "esp32" → Instalar "ESP32 by Espressif Systems"
Paso 2: Instalar Bibliotecas
text
1. Programa → Incluir librería → Gestionar bibliotecas
2. Instalar:
   - Adafruit SSD1306 by Adafruit
   - Adafruit GFX Library by Adafruit
   - ArduinoJSON by Benoit Blanchon
   - Adafruit DRV2605 Library by Adafruit
Paso 3: Subir Firmware
bash
1. Descargar dxa_controller.ino del repositorio
2. Abrir en Arduino IDE
3. Seleccionar placa: "ESP32 Dev Module"
4. Puerto: /dev/ttyUSB0 (Linux) o COMx (Windows)
5. Subir → Verificar que compila sin errores
3.2. Configurar Python para Análisis DXA
Paso 1: Crear entorno virtual
bash
# Linux/macOS
python3 -m venv osteoflux-env
source osteoflux-env/bin/activate

# Windows
python -m venv osteoflux-env
osteoflux-env\Scripts\activate
Paso 2: Instalar dependencias
bash
pip install --upgrade pip
pip install pydicom numpy pandas matplotlib scipy
pip install jupyter notebook  # Para desarrollo
pip install fastapi uvicorn python-multipart
Paso 3: Probar instalación
python
# test_installation.py
import pydicom
import numpy as np
import pandas as pd

print("✅ PyDICOM version:", pydicom.__version__)
print("✅ NumPy version:", np.__version__)
print("✅ Pandas version:", pd.__version__)

# Test básico
data = {"bmd": 0.85, "t_score": -1.5}
df = pd.DataFrame([data])
print("✅ Test DataFrame:", df.head())
3.3. Configurar Comunicación Serial
Paso 1: Identificar puerto ESP32
bash
# Linux
ls /dev/ttyUSB*

# macOS
ls /dev/cu.usbserial*

# Windows
# Ver en Administrador de dispositivos → Puertos (COM y LPT)
Paso 2: Configurar permisos (Linux)
bash
sudo usermod -a -G dialout $USER
sudo chmod 666 /dev/ttyUSB0
Paso 3: Test comunicación
python
# serial_test.py
import serial
import time

# Configurar puerto
ser = serial.Serial(
    port='/dev/ttyUSB0',  # Ajustar según sistema
    baudrate=115200,
    timeout=1
)

# Enviar comando de prueba
ser.write(b'STATUS\r\n')
response = ser.readline()
print("Respuesta:", response.decode())
ser.close()
4. Configuración del Sistema
4.1. Calibración Inicial
Calibración Motor:
arduino
// Ejecutar en ESP32
void calibrateMotor() {
  Serial.println("Calibrando motor...");
  
  // Barrido de frecuencias 30-90Hz
  for(int freq=30; freq<=90; freq+=5) {
    setMotorFrequency(freq);
    delay(1000);
    Serial.print("Freq: "); Serial.print(freq); 
    Serial.println(" Hz - OK");
  }
  
  Serial.println("Calibración completa");
}
Calibración Display:
arduino
void calibrateDisplay() {
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(0,0);
  display.println("Calibracion OK");
  display.display();
}
4.2. Configuración Parámetros DXA
Archivo de configuración: dxa_config.json
json
{
  "patient_defaults": {
    "age": 50,
    "sex": "F",
    "bmi": 25.0
  },
  "frequency_limits": {
    "min_hz": 30,
    "max_hz": 90,
    "default_hz": 45
  },
  "session_settings": {
    "duration_min": 20,
    "max_sessions_per_day": 2,
    "min_interval_hours": 6
  },
  "safety_limits": {
    "max_acceleration_g": 2.0,
    "max_temperature_c": 41,
    "emergency_stop": true
  }
}
4.3. Integración con Sistema DXA
Opción 1: Archivo CSV
python
# Cargar datos DXA desde CSV
import pandas as pd
dxa_data = pd.read_csv('patient_dxa_data.csv')

# Formato esperado:
# patient_id,age,sex,bmi,bmd_lumbar,bmd_hip,t_score,z_score
Opción 2: API REST
python
# API para recibir datos DXA
from fastapi import FastAPI
app = FastAPI()

@app.post("/dxa-data")
async def receive_dxa_data(data: dict):
    # Procesar datos DXA
    bmd = data.get('bmd')
    t_score = data.get('t_score')
    
    # Calcular frecuencia óptima
    frequency = calculate_optimal_frequency(bmd, t_score)
    
    # Enviar a ESP32
    send_to_esp32(frequency)
    
    return {"status": "success", "frequency_hz": frequency}
5. Pruebas del Sistema Completo
5.1. Secuencia de Prueba
bash
# 1. Iniciar ESP32
-> Verificar que display muestra "Sistema Listo"

# 2. Enviar datos DXA de prueba
python send_test_data.py

# 3. Verificar que motor vibra a frecuencia correcta
-> Usar acelerómetro para medir frecuencia real

# 4. Probar controles manuales
-> Botón START inicia sesión
-> Botón STOP detiene inmediatamente
-> Botón MENU muestra configuración

# 5. Verificar registro de datos
-> Los datos de sesión se guardan en ESP32
-> Posibilidad de exportar por USB
5.2. Script de Prueba Automatizada
python
# test_system.py
import subprocess
import serial
import time

def test_full_system():
    print("=== PRUEBA SISTEMA COMPLETO ===")
    
    # 1. Iniciar API
    print("1. Iniciando API DXA...")
    api_process = subprocess.Popen(["uvicorn", "api:app", "--port", "8000"])
    time.sleep(3)
    
    # 2. Conectar a ESP32
    print("2. Conectando a ESP32...")
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=2)
    
    # 3. Enviar datos de prueba
    print("3. Enviando datos DXA de prueba...")
    test_data = {
        "bmd": 0.82,
        "t_score": -2.3,
        "z_score": -1.5
    }
    
    # 4. Verificar respuesta
    print("4. Verificando respuesta del sistema...")
    ser.write(b'STATUS\r\n')
    response = ser.read(100)
    
    if b'Freq:' in response:
        print("✅ Sistema funcionando correctamente")
    else:
        print("❌ Error en la respuesta")
    
    # 5. Limpiar
    ser.close()
    api_process.terminate()

if __name__ == "__main__":
    test_full_system()
6. Solución de Problemas
6.1. Problemas Comunes
Motor no vibra:
text
1. Verificar conexiones motor
2. Medir voltaje en salida DRV2605L
3. Verificar que EN está en HIGH
4. Probar con ejemplo básico DRV2605
No hay comunicación serial:
text
1. Verificar puerto correcto
2. Comprobar baudrate (115200)
3. Reiniciar ESP32
4. Probar con otro cable USB
Display no muestra nada:
text
1. Verificar conexiones I2C
2. Comprobar voltaje 3.3V en OLED
3. Ejecutar I2C scanner
4. Cambiar dirección I2C (0x3C o 0x3D)
6.2. Logs de Diagnóstico
ESP32 Logs:
arduino
// Habilitar logs detallados
void setup() {
  Serial.begin(115200);
  Serial.setDebugOutput(true);
  
  // Inicializar componentes
  Serial.println("=== INICIANDO SISTEMA ===");
  Serial.println("Componentes inicializados:");
  Serial.println("- OLED: OK");
  Serial.println("- DRV2605: OK");
  Serial.println("- Botones: OK");
}
Python Logs:
python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
logger.info("Sistema DXA iniciado")
logger.debug("Datos recibidos: %s", dxa_data)
7. Actualizaciones y Mantenimiento
7.1. Actualizar Firmware
bash
# Método 1: Arduino IDE
1. Descargar nueva versión .ino
2. Subir normalmente

# Método 2: OTA (Over-The-Air)
1. ESP32 debe estar en WiFi
2. Acceder a http://esp32-ip/update
3. Subir archivo .bin
7.2. Actualizar Software Python
bash
# Actualizar desde repositorio
git pull origin main
pip install -r requirements.txt --upgrade

# Actualizar solo nuestro paquete
pip install dxa-analysis --upgrade
7.3. Backup de Configuración
bash
# Exportar configuración actual
python -c "import json; import dxa_config; print(json.dumps(dxa_config.settings))" > backup_config.json

# Importar configuración
python -c "import json; import dxa_config; dxa_config.settings = json.load(open('backup_config.json'))"
8. Recursos Adicionales
8.1. Documentación
ESP32 Datasheet

DRV2605L Manual

Protocolo DICOM DXA

8.2. Comunidad
Foro ESP32

GitHub Issues

[Discord/Slack del proyecto]

8.3. Soporte
Issues técnicos: GitHub Issues

Problemas clínicos: Consultar con médico

Emergencias: Desconectar dispositivo inmediatamente

Nota: Este sistema es para uso bajo supervisión médica. Seguir siempre protocolos de seguridad.

Última actualización: Diciembre 2025
Versión: 1.0
