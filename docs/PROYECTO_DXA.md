# TECNICO_DXA.md
## Especificaciones Técnicas del Sistema DXA + Vibración

### 1. Arquitectura del Sistema

#### 1.1. Diagrama de Bloques
[EQUIPO DXA CLÍNICO] → Datos DICOM → [ANÁLISIS SOFTWARE] →
[BMD, T-score, Z-score] → [CONTROLADOR ESP32] →
[SEÑAL PWM] → [MOTOR VIBRADOR] → [PACIENTE]

text

#### 1.2. Especificaciones Hardware

##### 1.2.1. Unidad de Control
- **Microcontrolador:** ESP32-WROOM-32
- **CPU:** Dual-core 240MHz
- **Memoria:** 520KB SRAM, 4MB Flash
- **Comunicación:** WiFi, Bluetooth, I2C, UART
- **Entradas:** 18× ADC, 10× capacitives
- **Salidas:** 2× DAC, 16× PWM

##### 1.2.2. Módulo Vibrador
- **Tipo:** LRA (Linear Resonant Actuator) o ERM (Eccentric Rotating Mass)
- **Voltaje operación:** 3.0V DC
- **Frecuencia rango:** 30-90 Hz (±2Hz precisión)
- **Amplitud máxima:** 2.0g
- **Tiempo respuesta:** <100ms
- **Conector:** JST-PH 2-pin

##### 1.2.3. Alimentación
- **Fuente principal:** 5V DC @ 2A
- **Backup:** Batería 18650 (opcional)
- **Consumo típico:** 500mA @ 5V
- **Autonomía:** 4 horas (con batería)

##### 1.2.4. Interfaz
- **Display:** OLED 0.96" 128×64 (I2C)
- **Botones:** 3× táctiles capacitivos
- **LEDs indicadores:** Power, Active, Fault
- **Conectores:** USB-C, JST para motor

#### 1.3. Especificaciones Software

##### 1.3.1. Firmware ESP32
- **Lenguaje:** C++ (Arduino Framework)
- **Bibliotecas principales:**
  - ArduinoJSON para datos DXA
  - Adafruit_SSD1306 para display
  - ESP32 PWM Library
- **Tareas principales:**
  - Recepción datos DXA (Serial/Bluetooth)
  - Cálculo frecuencia óptima
  - Control PWM del motor
  - Monitoreo seguridad
  - Registro datos sesión

##### 1.3.2. Software de Análisis (Python)
- **Entorno:** Python 3.9+
- **Dependencias:**
  - pydicom (lectura DICOM)
  - numpy, pandas (procesamiento)
  - scipy (análisis señales)
  - matplotlib (visualización)
- **Funcionalidades:**
  - Parseo archivos DXA DICOM
  - Cálculo BMD, T-score, Z-score
  - Recomendación frecuencia
  - Generación reportes
  - Análisis longitudinal

##### 1.3.3. Protocolos Comunicación
- **DXA Data Format:** JSON estructurado
```json
{
  "patient_id": "P-001",
  "age": 65,
  "sex": "F",
  "bmi": 24.5,
  "dxa_data": {
    "bmd_lumbar": 0.812,
    "bmd_hip": 0.723,
    "t_score": -2.7,
    "z_score": -1.8,
    "scan_date": "2025-12-20"
  }
}
Comandos Control: Serial ASCII

text
SET_FREQ:45.5    # Establecer frecuencia Hz
SET_INT:80       # Intensidad 0-100%
START            # Iniciar sesión
STOP             # Detener sesión
STATUS           # Solicitar estado
2. Algoritmo de Cálculo de Frecuencia
2.1. Fórmula Base
text
f_optimal = f_base + Δ_age + Δ_sex + Δ_bmi + Δ_diagnosis
Donde:

f_base: 50Hz (normal), 45Hz (osteopenia), 40Hz (osteoporosis)

Δ_age: -5Hz si >60 años, -5Hz adicional si >70 años

Δ_sex: +2Hz si sexo femenino

Δ_bmi: +3Hz si BMI >30, -2Hz si BMI <18.5

Δ_diagnosis: según clasificación WHO

2.2. Tabla de Frecuencias Recomendadas
Diagnóstico (WHO)	T-score	Frecuencia Base	Rango Ajustado
Normal	≥ -1.0	50 Hz	45-60 Hz
Osteopenia	-2.5 a -1.0	45 Hz	40-55 Hz
Osteoporosis	≤ -2.5	40 Hz	35-50 Hz
2.3. Límites de Seguridad
Frecuencia mínima: 30 Hz (efecto terapéutico mínimo)

Frecuencia máxima: 90 Hz (límite seguridad)

Intensidad máxima: 2.0g aceleración

Duración máxima: 30 minutos/sesión

Pausa mínima: 60 minutos entre sesiones

3. Parámetros de Calidad
3.1. Precisión
Frecuencia: ±1.0 Hz

Intensidad: ±5% del valor nominal

Tiempo: ±1 segundo por hora

3.2. Repetibilidad
Variación entre sesiones: <3%

Estabilidad frecuencia: <1% drift en 30min

Consistencia intensidad: <5% variación

3.3. Seguridad Eléctrica
Aislamiento: 4000V paciente-parte

Corriente fuga: <100μA

Temperatura: <41°C en contacto

Sobre-corriente: Protección automática

4. Protocolos de Prueba
4.1. Pruebas Funcionales
Prueba frecuencia: Verificar rango 30-90 Hz

Prueba intensidad: Medir aceleración 0.1-2.0g

Prueba duración: Operación continua 60min

Prueba comunicación: Recepción/envió datos

4.2. Pruebas Clínicas (Fase)
Fase 1: n=10 voluntarios sanos

Fase 2: n=30 pacientes osteopenia

Fase 3: n=50 pacientes osteoporosis

Seguimiento: 6, 12, 24 meses

5. Documentación Asociada
5.1. Manuales
Manual de Usuario (clínico)

Manual Técnico (mantenimiento)

Protocolo Clínico (médico)

Guía Programación (desarrollador)

5.2. Certificaciones
Eléctrica: IEC 60601-1

EMC: IEC 60601-1-2

Software: IEC 62304

Calidad: ISO 13485

5.3. Archivos de Diseño
Esquemáticos electrónicos (PDF)

PCB layouts (Gerber)

Modelos 3D (STEP)

Lista de materiales (BOM)

6. Mantenimiento y Soporte
6.1. Calibración
Periódica: Cada 6 meses

Post-reparación: Siempre

Verificación: Con acelerómetro de referencia

6.2. Actualizaciones
Firmware: OTA (Over-The-Air)

Software: PyPI package

Documentación: GitHub Wiki

6.3. Diagnóstico
Autodiagnóstico: Al inicio cada sesión

Logs: Almacenamiento local 1000 sesiones

Alertas: Visuales y audibles

Versión: 1.0
Fecha: Diciembre 2025
Estado: En desarrollo activo
