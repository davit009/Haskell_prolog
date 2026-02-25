import re
from datetime import datetime
from pathlib import Path

try:
    from pyswip import Prolog
except ImportError as exc:
    raise SystemExit(
        "Instala pyswip para conectar Python con Prolog: pip install pyswip"
    ) from exc


LOG = Path(__file__).resolve().parent / "python_prolog.log"


def append_log(texto: str) -> None:
    with LOG.open("a", encoding="utf-8") as f:
        f.write(texto)


def normalizar_texto(texto: str) -> str:
    return " ".join(texto.strip().lower().split())


def to_prolog_atom(texto: str) -> str:
    # Usa atomos entre comillas para soportar mayusculas y espacios.
    limpio = normalizar_texto(texto).replace("'", "\\'")
    return f"'{limpio}'"


class Agente:
    def __init__(self):
        self.prolog = Prolog()
        try:
            self.prolog.consult("conocimiento.pl")
        except Exception as exc:
            raise SystemExit(f"No se pudo cargar conocimiento.pl: {exc}") from exc

    def procesar(self, texto: str) -> str:
        t = normalizar_texto(texto)

        m = re.match(r"hola,? soy (.+)$", t)
        if m:
            nombre = m.group(1)
            try:
                list(
                    self.prolog.query(
                        f"registrar_nombre(usuario,{to_prolog_atom(nombre)})"
                    )
                )
                append_log(f"{datetime.now().isoformat()} | nombre | {nombre}\n")
                return f"Hola, {nombre}. Encantado de conocerte."
            except Exception as exc:
                return f"Error al registrar nombre: {exc}"

        m = re.match(r"a (.+) le gusta el (.+)$", t)
        if m:
            persona, cosa = m.group(1), m.group(2)
            try:
                list(
                    self.prolog.query(
                        f"registrar_gusto({to_prolog_atom(persona)},{to_prolog_atom(cosa)})"
                    )
                )
                append_log(
                    f"{datetime.now().isoformat()} | gusto | {persona} -> {cosa}\n"
                )
                return "Dato guardado."
            except Exception as exc:
                return f"Error al guardar dato: {exc}"

        m = re.match(r"a quién le gusta el (.+)\??$", t)
        if m:
            cosa = m.group(1).rstrip("?").strip()
            try:
                q = list(self.prolog.query(f"quien_gusta({to_prolog_atom(cosa)},Quien)"))
                append_log(f"{datetime.now().isoformat()} | consulta | {cosa}\n")
                if q:
                    return f"A {q[0]['Quien']} le gusta el {cosa}."
                return f"No tengo registro de quién gusta del {cosa}."
            except Exception as exc:
                return f"Error al consultar Prolog: {exc}"

        return "No entendi la frase."


if __name__ == "__main__":
    agente = Agente()
    print("Agente conversacional (escribe 'salir' para terminar)")
    while True:
        entrada = input("> ")
        if entrada.strip().lower() == "salir":
            break
        print(agente.procesar(entrada))
