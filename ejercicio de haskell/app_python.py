import json
import subprocess
from pathlib import Path
from datetime import datetime

BASE = Path(__file__).resolve().parent
EXE = BASE / "diagnostico.exe"
LOG = BASE / "python.log"


def append_log(texto: str) -> None:
    with LOG.open("a", encoding="utf-8") as f:
        f.write(texto)


def ejecutar_haskell(sintomas):
   
    try:
        resultado = subprocess.run(
            [str(EXE), *sintomas],
            capture_output=True,
            text=True,
            check=True,
        )
        data = json.loads(resultado.stdout)
        append_log(
            f"{datetime.now().isoformat()} | {sintomas} -> {data['recomendacion']}\n"
        )
        return data
    except FileNotFoundError:
        mensaje = f"No se encontro el ejecutable: {EXE}"
        append_log(f"{datetime.now().isoformat()} | ERROR | {mensaje}\n")
        return {"error": mensaje}
    except (subprocess.CalledProcessError, json.JSONDecodeError) as exc:
        mensaje = f"Error al ejecutar Haskell: {exc}"
        append_log(f"{datetime.now().isoformat()} | ERROR | {mensaje}\n")
        return {"error": mensaje}


if __name__ == "__main__":
    entrada = input("Escribe sintomas separados por coma: ").strip()
    sintomas = [x.strip().lower() for x in entrada.split(",") if x.strip()]
    respuesta = ejecutar_haskell(sintomas)
    if "error" in respuesta:
        print("Error:", respuesta["error"])
    else:
        print("Diagnostico:", respuesta)
