Sistema DXA + Vibración Adaptativa
1. Componentes Electrónicos
1.1. Unidad de Control Principal
Cantidad	Componente	Especificación	Proveedor	Precio Aprox.
1	Microcontrolador ESP32	DevKit v1, 4MB Flash	Amazon/AliExpress	$8
1	Driver Haptic DRV2605L	Controlador motor LRA	Adafruit/SparkFun	$5
1	Motor Vibrador LRA	3V, 30-90Hz, lineal	Digi-Key/Mouser	$12
1	Pantalla OLED	0.96", 128×64, I2C	Amazon	$4
1	Regulador Voltaje	LM7805 5V, 1A	Local/Online	$1
1	Convertidor DC-DC	Step-down 5V→3.3V	Amazon	$2
1	Conector DC	5.5×2.1mm panel mount	Amazon	$2
1.2. Interfaz y Control
Cantidad	Componente	Especificación	Proveedor	Precio Aprox.
3	Botones táctiles	12mm, momentary	Amazon	$3
1	Zócalo batería	18650 holder	Amazon	$2
1	Batería 18650	3.7V, 3000mAh	Local	$6
1	Cargador TP4056	Módulo carga Li-ion	Amazon	$2
1	Buzzer pasivo	5V, 12mm	Amazon	$1
2	LEDs indicadores	5mm, rojo/verde	Amazon	$1
1.3. Conectores y Cableado
Cantidad	Componente	Especificación	Proveedor	Precio Aprox.
1	Conector JST-PH	2-pin, motor	Amazon	$2
1	Header pins	40-pin, macho/hembra	Amazon	$2
1	Protoboard	400 puntos	Amazon	$3
1	Cable dupont	20cm, 40 unidades	Amazon	$3
1	Cable USB-C	Programación ESP32	Amazon	$4
2. Componentes Mecánicos y Estructura
2.1. Carcasa y Montaje
Cantidad	Componente	Especificación	Método	Notas
1	Carcasa principal	ABS, 120×80×40mm	Impresión 3D	Archivo STP en /hardware
1	Tapa superior	Con orificios display/botones	Impresión 3D	Acoplable
1	Base inferior	Con slots ventilación	Impresión 3D	Pies antideslizantes
4	Tornillos M3	10mm, cabeza plana	Ferretería	Fijación
4	Separadores	Nylon, 15mm	Amazon	Aislamiento PCB
1	Panel frontal	Acrílico 3mm, grabado	Corte láser	Protección display
2.2. Interfaz con Paciente
Cantidad	Componente	Especificación	Propósito
1	Plataforma vibración	ABS, 200×150mm	Contacto con paciente
4	Almohadillas gel	Silicona médica	Acoplamiento cómodo
1	Correa ajustable	Nylon, 50cm	Fijación a silla/cama
1	Aislante térmico	Espuma neopreno	Protección temperatura
3. Herramientas Requeridas
3.1. Herramientas Básicas
Cantidad	Herramienta	Especificación	Notas
1	Soldador	60W, temperatura ajustable	Estación recomendada
1	Estaño	0.8mm, con flux	Calidad buena
1	Alicate	Corte diagonal	Para componentes
1	Pinzas	Punta fina	Para SMD
1	Multímetro	Digital, auto-ranging	Medición voltaje/resistencia
1	Destornillador	Set precision	Para tornillos M3
3.2. Herramientas Opcionales
Herramienta	Propósito	Prioridad
Osciloscopio	Verificación señales PWM	Media
Fuente alimentación	Pruebas voltaje variable	Baja
Impresora 3D	Fabricación carcasa	Alta (si no se encarga)
Cortador PCB	Para prototipos finales	Media
4. Software y Licencias
4.1. Software Libre
Software	Versión	Licencia	Propósito
Arduino IDE	2.3+	GPL	Programación ESP32
PlatformIO	6.1+	Apache 2.0	Entorno desarrollo
Python	3.9+	PSF	Análisis DXA
FreeCAD	0.21+	LGPL	Diseño 3D
KiCad	7.0+	GPL	Diseño PCB
4.2. Bibliotecas y Dependencias
Paquete	Versión	Licencia	Uso
pydicom	2.3+	MIT	Lectura archivos DICOM
numpy	1.24+	BSD	Cálculos numéricos
pandas	2.0+	BSD	Procesamiento datos
Adafruit_DRV2605	1.4+	MIT	Control motor
Adafruit_SSD1306	2.5+	MIT	Control display OLED
5. Costo Total Estimado
5.1. Prototipo Único
Categoría	Costo Estimado	Notas
Electrónica	$55	Todos componentes nuevos
Mecánica	$25	Impresión 3D + materiales
Herramientas	$50	Si no se tienen
Total	$130	Por unidad
5.2. Lote de 10 Unidades
Categoría	Costo/Unidad	Ahorro
Electrónica	$40	Compras al por mayor
Mecánica	$15	Producción batch
Total	$55	58% ahorro vs prototipo
5.3. Versión Comercial (Estimado)
Categoría	Costo Producción	Notas
PCB personalizado	$15	Incluye componentes SMD
Carcasa moldeada	$8	Inyección plástico
Ensamblaje	$12	Mano de obra
Certificaciones	$20	Por unidad (amortizado)
Total	$55	Similar a lote 10
6. Proveedores Recomendados
6.1. Internacionales (Envío global)
Proveedor	Fortalezas	Enlace
Digi-Key	Amplio stock, rápido	digikey.com
Mouser	Componentes especializados	mouser.com
LCSC	Precios bajos, envío China	lcsc.com
Amazon	Conveniente, rápido	amazon.com
6.2. Locales (Chile)
Proveedor	Productos	Notas
Electrocomponents	Componentes básicos	Varias ciudades
Impresión 3D local	Carcasas	Buscar en mercado libre
Ferreterías	Tornillos, herramientas	Sodimac, Easy
7. Plan de Adquisición
7.1. Fase 1: Prototipo Básico
bash
# Componentes esenciales (semana 1)
1. ESP32 DevKit v1
2. Motor LRA + DRV2605L
3. Display OLED
4. Protoboard y cables
5. Fuente 5V 2A

# Presupuesto: $35
7.2. Fase 2: Prototipo Funcional
bash
# Componentes adicionales (semana 2)
1. Batería y cargador
2. Botones y LEDs
3. Materiales carcasa
4. Herramientas soldadura

# Presupuesto: $45
7.3. Fase 3: Versión Final
bash
# Mejoras y profesionalización (semana 3-4)
1. PCB personalizado
2. Carcasa impresa profesional
3. Conectores calidad
4. Certificaciones seguridad

# Presupuesto: $50
8. Alternativas y Sustitutos
8.1. Motor Vibrador
Opción	Ventajas	Desventajas	Costo
LRA (Linear)	Precisión frecuencia, rápido	Más caro	$12
ERM (Eccentric)	Más barato, alta potencia	Menor control	$6
Piezoeléctrico	Exactitud máxima, silencioso	Muy caro, frágil	$25
8.2. Microcontrolador
Opción	Ventajas	Desventajas	Compatibilidad
ESP32	WiFi/BT, doble núcleo	Consumo medio	100%
Arduino Nano	Simple, amplia comunidad	Limitado I/O	70%
Raspberry Pi Pico	Potente, barato	Sin WiFi	80%
9. Consideraciones de Seguridad
9.1. Eléctricas
Aislamiento: 4000V entre partes paciente y alimentación

Corriente fuga: <100μA en modo normal

Protección polaridad: Diodos en entrada DC

Fusible: Reseteable 2A en entrada

9.2. Mecánicas
Temperatura superficie: <41°C en contacto continuo

Vibración máxima: 2.0g aceleración

Materiales contacto: Hipoaergénicos, no tóxicos

Bordes: Redondeados, sin filos

9.3. Electromagnéticas
Compatibilidad: Cumplir IEC 60601-1-2

Emisiones: Dentro límites clase B

Inmunidad: Resistir interferencias comunes

10. Mantenimiento y Repuestos
10.1. Consumibles
Componente	Vida útil	Stock recomendado
Almohadillas gel	6 meses	2 pares
Batería 18650	2 años	1 unidad
Correas ajustables	1 año	2 unidades
10.2. Reparables
Componente	Tiempo reparación	Herramientas necesarias
Motor LRA	15 minutos	Destornillador, soldador
Botones	10 minutos	Destornillador
Conector DC	5 minutos	Soldador
11. Referencias Técnicas
11.1. Documentación del Equipo
ESP32: Datasheet oficial Espressif

DRV2605L: Manual técnico Texas Instruments

LRA Motor: Especificaciones fabricante

OLED Display: Protocolo I2C SSD1306

11.2. Estudios de Referencia
Estudio sobre vibración ósea y densidad mineral

Investigaciones WBV en osteoporosis

Protocolos DXA estandarización

Guías seguridad dispositivos médicos

11.3. Normativas
IEC 60601-1: Seguridad equipos electromédicos

ISO 13485: Sistemas calidad dispositivos médicos

IEC 62304: Software dispositivos médicos

FDA 510(k): Proceso autorización EE.UU.

Elaborado por: Equipo técnico del proyecto
Revisión: Diciembre 2025
Estado: Lista preliminar, sujeto a cambios

Nota: Los precios son estimativos y pueden variar según región y proveedor. Verificar disponibilidad antes de comprar.
