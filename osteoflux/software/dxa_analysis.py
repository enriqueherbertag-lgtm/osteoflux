#!/usr/bin/env python3
"""
DXA Analysis Module
Calcula frecuencia óptima de vibración basada en datos DXA
"""

import numpy as np
import pandas as pd
from dataclasses import dataclass
from typing import Dict, Tuple

@dataclass
class PatientProfile:
    """Perfil del paciente para cálculo personalizado"""
    age: int
    sex: str  # 'M' o 'F'
    bmi: float
    dxa_data: Dict[str, float]  # BMD, T-score, Z-score

class DXAFrequencyOptimizer:
    """Optimiza frecuencia de vibración basada en datos DXA"""
    
    def __init__(self):
        self.base_frequencies = {
            'normal': 50.0,      # T-score ≥ -1.0
            'osteopenia': 45.0,  # -2.5 < T-score < -1.0
            'osteoporosis': 40.0 # T-score ≤ -2.5
        }
        
    def calculate_optimal_frequency(self, patient: PatientProfile) -> float:
        """Calcula frecuencia óptima en Hz basada en datos DXA"""
        
        # 1. Obtener clasificación según T-score (criterios WHO)
        diagnosis = self._classify_diagnosis(patient.dxa_data['t_score'])
        
        # 2. Frecuencia base según diagnóstico
        base_freq = self.base_frequencies[diagnosis]
        
        # 3. Ajustes por características del paciente
        adjusted_freq = self._apply_patient_adjustments(base_freq, patient)
        
        # 4. Limitar rango seguro (30-90 Hz)
        optimal_freq = np.clip(adjusted_freq, 30.0, 90.0)
        
        return optimal_freq
    
    def _classify_diagnosis(self, t_score: float) -> str:
        """Clasifica según criterios WHO"""
        if t_score >= -1.0:
            return 'normal'
        elif t_score > -2.5:
            return 'osteopenia'
        else:
            return 'osteoporosis'
    
    def _apply_patient_adjustments(self, base_freq: float, patient: PatientProfile) -> float:
        """Ajusta frecuencia según perfil del paciente"""
        adjusted = base_freq
        
        # Ajuste por edad (mayor edad → frecuencia más baja)
        if patient.age > 60:
            adjusted -= 5.0
        if patient.age > 70:
            adjusted -= 5.0
        
        # Ajuste por sexo (mujeres pueden requerir frecuencias diferentes)
        if patient.sex == 'F':
            adjusted += 2.0
        
        # Ajuste por BMI (obesidad puede atenuar vibración)
        if patient.bmi > 30:
            adjusted += 3.0
        elif patient.bmi < 18.5:
            adjusted -= 2.0
        
        return adjusted
    
    def calculate_treatment_protocol(self, patient: PatientProfile) -> Dict:
        """Genera protocolo completo de tratamiento"""
        optimal_freq = self.calculate_optimal_frequency(patient)
        
        protocol = {
            'diagnosis': self._classify_diagnosis(patient.dxa_data['t_score']),
            'optimal_frequency_hz': round(optimal_freq, 1),
            'session_duration_min': 20,
            'sessions_per_week': 5,
            'treatment_phase': self._determine_treatment_phase(patient),
            'safety_limits': {
                'max_frequency_hz': 90.0,
                'min_frequency_hz': 30.0,
                'max_duration_min': 30
            }
        }
        
        return protocol
    
    def _determine_treatment_phase(self, patient: PatientProfile) -> str:
        """Determina fase del tratamiento"""
        t_score = patient.dxa_data['t_score']
        
        if t_score <= -3.0:
            return 'intensive'
        elif t_score <= -2.0:
            return 'therapeutic'
        else:
            return 'maintenance'
    
    def analyze_longitudinal_data(self, csv_file: str) -> pd.DataFrame:
        """Analiza datos longitudinales de DXA"""
        df = pd.read_csv(csv_file)
        
        results = []
        for _, row in df.iterrows():
            patient = PatientProfile(
                age=row['age'],
                sex=row['sex'],
                bmi=row['bmi'],
                dxa_data={
                    'bmd': row['bmd'],
                    't_score': row['t_score'],
                    'z_score': row['z_score']
                }
            )
            
            optimal_freq = self.calculate_optimal_frequency(patient)
            
            results.append({
                'patient_id': row['patient_id'],
                'visit_date': row['visit_date'],
                'bmd': row['bmd'],
                't_score': row['t_score'],
                'optimal_frequency_hz': optimal_freq,
                'diagnosis': self._classify_diagnosis(row['t_score'])
            })
        
        return pd.DataFrame(results)

# ============ EJEMPLO DE USO ============

if __name__ == "__main__":
    print("=== DXA FREQUENCY OPTIMIZER ===\n")
    
    # Crear optimizador
    optimizer = DXAFrequencyOptimizer()
    
    # Ejemplo 1: Paciente con osteoporosis
    patient1 = PatientProfile(
        age=68,
        sex='F',
        bmi=22.5,
        dxa_data={
            'bmd': 0.750,
            't_score': -2.8,
            'z_score': -1.5
        }
    )
    
    freq1 = optimizer.calculate_optimal_frequency(patient1)
    protocol1 = optimizer.calculate_treatment_protocol(patient1)
    
    print("PACIENTE 1 (Osteoporosis):")
    print(f"  Edad: {patient1.age}, Sexo: {patient1.sex}, BMI: {patient1.bmi}")
    print(f"  T-score: {patient1.dxa_data['t_score']}")
    print(f"  Frecuencia óptima: {freq1:.1f} Hz")
    print(f"  Protocolo: {protocol1['treatment_phase']}")
    print()
    
    # Ejemplo 2: Paciente con osteopenia
    patient2 = PatientProfile(
        age=55,
        sex='M',
        bmi=28.0,
        dxa_data={
            'bmd': 0.920,
            't_score': -1.8,
            'z_score': -0.5
        }
    )
    
    freq2 = optimizer.calculate_optimal_frequency(patient2)
    
    print("PACIENTE 2 (Osteopenia):")
    print(f"  Edad: {patient2.age}, Sexo: {patient2.sex}, BMI: {patient2.bmi}")
    print(f"  T-score: {patient2.dxa_data['t_score']}")
    print(f"  Frecuencia óptima: {freq2:.1f} Hz")
    print()
    
    # Ejemplo 3: Análisis de archivo CSV
    print("ANÁLISIS DE DATOS LONGITUDINALES:")
    print("(Simulación - requiere archivo CSV con datos DXA)")
    print("\n✅ Módulo listo para integración con sistema de vibración")
