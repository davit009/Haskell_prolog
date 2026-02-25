# Proyecto 2: Prolog + Python (Sistema experto y agente conversacional)

## 1. Objetivo del proyecto
Construir un proyecto con Prolog como motor de inferencia y Python como interfaz.

Contiene dos partes:

1. `experto.pl`: sistema experto básico para recomendación por síntomas.
2. `app_python.py` + `conocimiento.pl`: agente conversacional que registra hechos y consulta conocimiento.

## 2. Evidencias que validan el proyecto
Este proyecto demuestra:

1. Uso de hechos y reglas en Prolog (`medicamento/1`, `recomendacion/1`).
2. Integración Python -> Prolog con `pyswip`.
3. Inserción dinámica de conocimiento con `assertz`.
4. Consultas desde Python con respuesta natural.
5. Log acumulativo en `python_prolog.log` (modo append).
6. Manejo básico de errores en consultas y carga de base de conocimiento.

## 3. Estructura de archivos
- `experto.pl`: reglas del diagnóstico médico.
- `conocimiento.pl`: base dinámica para nombres y gustos.
- `app_python.py`: interfaz conversacional en Python.
- `README.md`: guía de validación.

## 4. Requisitos
- SWI-Prolog instalado
- Python 3 instalado
- Dependencia Python:
```powershell
pip install pyswip
```

## 5. Parte A: validar sistema experto en Prolog
En consola de SWI-Prolog:

```prolog
consult('experto.pl').
assertz(sintoma(fiebre)).
assertz(sintoma(dolor)).
recomendacion(X).
```

Resultado esperado:

`X = paracetamol.`

## 6. Parte B: validar agente Python + Prolog
Desde terminal:

```powershell
cd "ruta"
python app_python.py
```

Flujo sugerido de prueba:

1. `Hola, soy Juan Perez`
2. `A Maria Lopez le gusta el cafe`
3. `A quién le gusta el cafe?`

Resultado esperado (similar):

`A maria lopez le gusta el cafe.`

