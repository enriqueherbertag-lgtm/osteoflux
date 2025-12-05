# 🦴 OsteoFlux  
### **Sistema Open-Source de Vibración Adaptativa para Salud Ósea**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Active Development](https://img.shields.io/badge/Status-Active_Development-brightgreen)]()
[![Platform: ESP32 + Python](https://img.shields.io/badge/Platform-Embedded_%2B_Python-blue)]()
[![Cost: < $100](https://img.shields.io/badge/Cost-<$100_Components-success)]()

---

## 🔬 **EL PROBLEMA REAL:**
Los dispositivos actuales de vibración para osteoporosis usan **frecuencias fijas** (ej: 35Hz para todos).  
No miden cuánta vibración llega realmente al hueso.  
**Resultado:** Funcionan para algunos, no para otros.

## 🎯 **NUESTRA SOLUCIÓN (QUE NADIE MÁS TIENE):**
**Doble acelerómetro + algoritmo adaptativo en tiempo real:**
1. **Acelerómetro 1:** Mide vibración GENERADA por el dispositivo
2. **Acelerómetro 2:** Mide vibración RECIBIDA por el hueso
3. **Algoritmo:** Ajusta frecuencia (30-90 Hz) para maximizar transmisión

## ⚙️ **CÓMO FUNCIONA:**
```python
# Algoritmo adaptativo (simplificado)
if transmision < 70%:
    aumentar_frecuencia()  # Mejorar penetración
elif transmision > 85%:
    disminuir_frecuencia()  # Evitar sobreestimulación
