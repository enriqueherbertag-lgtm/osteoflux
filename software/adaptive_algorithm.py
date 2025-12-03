#!/usr/bin/env python3
"""
OsteoFlux - Algoritmo Adaptativo de Vibración
Analiza datos de doble acelerómetro y ajusta frecuencia óptima
"""

import numpy as np
import pandas as pd
from scipy import signal

class AdaptiveVibrationOptimizer:
    """Optimiza frecuencia de vibración basado en transmisión ósea"""
    
    def __init__(self):
        self.current_freq = 35.0  # Hz
        self.transmission_history = []
        self.frequency_history = []
        
    def calculate_transmission(self, device_accel, bone_accel):
        """Calcula porcentaje de transmisión dispositivo→hueso"""
        transmission = (np.mean(bone_accel) / np.mean(device_accel)) * 100
        return np.clip(transmission, 0, 100)
    
    def adaptive_frequency_adjustment(self, transmission):
        """Ajusta frecuencia basado en transmisión medida"""
        
        # REGLAS DE AJUSTE (al hueso, sin florituras)
        if transmission < 60:
            self.current_freq += 1.0  # Subir si poca transmisión
        elif transmission > 85:
            self.current_freq -= 1.0  # Bajar si mucha transmisión
        elif 70 < transmission < 80:
            self.current_freq += 0.2  # Ajuste fino si cerca de óptimo
            
        # Limitar rango (30-90 Hz)
        self.current_freq = np.clip(self.current_freq, 30.0, 90.0)
        
        return self.current_freq
    
    def find_optimal_frequency(self, patient_data):
        """Encuentra frecuencia óptima para un paciente específico"""
        frequencies = np.arange(30, 91, 5)  # 30-90 Hz en pasos de 5
        transmissions = []
        
        for freq in frequencies:
            # Simular transmisión (en real, se mide)
            simulated_transmission = self.simulate_transmission(freq, patient_data)
            transmissions.append(simulated_transmission)
        
        optimal_idx = np.argmax(transmissions)
        optimal_freq = frequencies[optimal_idx]
        
        return optimal_freq, transmissions[optimal_idx]
    
    def simulate_transmission(self, frequency, patient_profile):
        """Simula transmisión basado en perfil del paciente"""
        # Factores que afectan transmisión
        bmi_factor = patient_profile.get('bmi', 25) / 25
        age_factor = 1.0 - (patient_profile.get('age', 50) - 50) * 0.005
        
        # Transmisión base para 35Hz
        base_transmission = 75.0
        
        # Ajustar por frecuencia (modelo simplificado)
        if frequency < 35:
            freq_factor = 1.0 - (35 - frequency) * 0.02
        else:
            freq_factor = 1.0 - (frequency - 35) * 0.015
            
        transmission = base_transmission * freq_factor * bmi_factor * age_factor
        
        return np.clip(transmission, 20, 95)
    
    def analyze_patient_data(self, csv_file):
        """Analiza archivo CSV con datos de paciente"""
        df = pd.read_csv(csv_file)
        
        results = {
            'transmission_mean': df['transmission'].mean(),
            'transmission_std': df['transmission'].std(),
            'optimal_frequency': None,
            'recommendation': ''
        }
        
        # Determinar frecuencia óptima
        if results['transmission_mean'] < 60:
            results['optimal_frequency'] = 45.0
            results['recommendation'] = 'Aumentar frecuencia (transmisión baja)'
        elif results['transmission_mean'] > 80:
            results['optimal_frequency'] = 35.0
            results['recommendation'] = 'Mantener frecuencia actual'
        else:
            results['optimal_frequency'] = 40.0
            results['recommendation'] = 'Ajuste fino recomendado'
            
        return results

# EJEMPLO DE USO (al hueso)
if __name__ == "__main__":
    print("=== OSTEOFLUX ALGORITMO ADAPTATIVO ===\n")
    
    # 1. Crear optimizador
    optimizer = AdaptiveVibrationOptimizer()
    
    # 2. Datos de ejemplo
    device_vibration = np.array([1.0, 1.1, 0.9, 1.0, 1.2])
    bone_vibration = np.array([0.7, 0.75, 0.65, 0.7, 0.8])
    
    # 3. Calcular transmisión
    transmission = optimizer.calculate_transmission(device_vibration, bone_vibration)
    print(f"Transmisión medida: {transmission:.1f}%")
    
    # 4. Ajustar frecuencia
    new_freq = optimizer.adaptive_frequency_adjustment(transmission)
    print(f"Nueva frecuencia: {new_freq:.1f} Hz")
    
    # 5. Encontrar óptimo para perfil
    patient_profile = {'age': 65, 'bmi': 22, 'sex': 'F'}
    optimal_freq, optimal_trans = optimizer.find_optimal_frequency(patient_profile)
    print(f"Frecuencia óptima estimada: {optimal_freq} Hz ({optimal_trans:.1f}% transmisión)")
    
    print("\n✅ Algoritmo listo para usar")
