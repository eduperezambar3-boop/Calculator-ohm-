# Calculadora de la Ley de Ohm

Una calculadora interactiva de línea de comandos que implementa la Ley de Ohm para calcular voltaje, corriente y resistencia en circuitos eléctricos.

## 📋 Descripción

La Ley de Ohm establece la relación fundamental entre voltaje (V), corriente (I) y resistencia (R) en un circuito eléctrico: **V = I × R**.

Esta calculadora permite al usuario:
- Calcular el voltaje dado corriente y resistencia
- Calcular la corriente dado voltaje y resistencia
- Calcular la resistencia dado voltaje y corriente
- Mantener un historial de todos los cálculos realizados

## 🚀 Características

- **Cálculos precisos**: Implementación exacta de la Ley de Ohm
- **Validación de entrada**: Verificación de números válidos y prevención de divisiones por cero
- **Historial persistente**: Guarda automáticamente todos los cálculos en `history.txt`
- **Interfaz intuitiva**: Menú simple con opciones claras
- **Manejo de errores**: Mensajes informativos para entradas inválidas

## 🛠️ Requisitos

- Python 3.x
- No requiere dependencias externas

## ▶️ Uso

1. **Ejecutar la calculadora:**
   ```bash
   python calculadoraohm.py
   ```

2. **Seleccionar opción:**
   - `V` - Calcular Voltaje
   - `I` - Calcular Corriente
   - `R` - Calcular Resistencia
   - `Q` - Salir

3. **Ingresar valores:**
   - Para cada cálculo, ingresa los valores requeridos cuando se soliciten
   - La calculadora valida automáticamente que sean números válidos

4. **Ver resultados:**
   - El resultado se muestra en pantalla
   - Se guarda automáticamente en el historial

## 📊 Ejemplos de Uso

### Calcular Voltaje
```
Enter current (I): 2
Enter resistance (R): 10
Voltage: 20.0
```

### Calcular Corriente
```
Enter voltage (V): 12
Enter resistance (R): 4
Current: 3.0
```

### Calcular Resistencia
```
Enter voltage (V): 24
Enter current (I): 0.5
Resistance: 48.0
```

## 📁 Estructura del Código

### Funciones Principales
- `calculate_voltage(current, resistance)`: Calcula V = I × R
- `calculate_current(voltage, resistance)`: Calcula I = V / R
- `calculate_resistance(voltage, current)`: Calcula R = V / I

### Funciones de Soporte
- `get_float(prompt)`: Valida entrada numérica del usuario
- `save_history(text)`: Guarda cálculos en archivo de historial
- `main()`: Función principal con el bucle del programa

## 📝 Historial

Todos los cálculos se guardan automáticamente en el archivo `history.txt` con el formato:
```
V = corriente * resistencia = voltaje
I = voltaje / resistencia = corriente
R = voltaje / corriente = resistencia
```

## ⚠️ Consideraciones

- **Unidades**: Asegúrate de usar unidades consistentes (volts, amperes, ohms)
- **Precisión**: Los cálculos usan aritmética de punto flotante estándar
- **Errores**: La calculadora previene divisiones por cero con mensajes de error
- **Historial**: El archivo `history.txt` se crea automáticamente si no existe

## 🔧 Personalización

El código está estructurado modularmente, permitiendo:
- Modificar la interfaz de usuario
- Agregar nuevas funcionalidades
- Cambiar el formato del historial
- Integrar con otras aplicaciones

## 📄 Licencia

Este proyecto es de código abierto y puede ser usado libremente para fines educativos y prácticos.

---

**Nota**: Esta calculadora es una herramienta educativa para entender y aplicar la Ley de Ohm. Para aplicaciones profesionales en ingeniería eléctrica, se recomienda verificar los cálculos con software especializado.