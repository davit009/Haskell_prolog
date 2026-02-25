# Proyecto 1: Haskell + Python (Diagnóstico simple)

## 1. Objetivo del proyecto
Implementar una solución en dos capas:

- `Main.hs`: motor de diagnóstico en Haskell.
- `app_python.py`: interfaz de ejecución en Python.

El programa recibe síntomas, calcula una recomendación y devuelve un JSON para consumo en Python.

## 2. Evidencias que validan el proyecto
Este proyecto cumple con:

1. Generación de ejecutable de Haskell (`diagnostico.exe`).
2. Comunicación Haskell -> Python por salida estándar en formato JSON.
3. Registro de ejecución en logs acumulativos (modo append):
   - `haskell.log`
   - `python.log`
4. Manejo básico de errores en Python (si falta el `.exe` o hay error de ejecución).

## 3. Estructura de archivos
- `Main.hs`: reglas de diagnóstico y salida JSON.
- `app_python.py`: pide síntomas, llama al ejecutable y muestra resultado.
- `README.md`: guía de validación.

## 4. Requisitos
- GHC instalado (Haskell)
- Python 3 instalado

## 5. Pasos para ejecutar
### 5.1 Compilar Haskell
```powershell
cd "ruta"
ghc Main.hs -o diagnostico.exe
```

### 5.2 Ejecutar desde Python
```powershell
python app_python.py
```

## 6. Prueba sugerida
Entrada:

`fiebre,dolor`

Salida esperada (similar):

`Diagnostico: {'sintomas': ['fiebre', 'dolor'], 'recomendacion': 'Paracetamol'}`

