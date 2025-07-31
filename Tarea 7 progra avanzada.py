eventos = {}

def registrar_evento(nombre_evento, *asistentes):
    eventos[nombre_evento] = {
        "asistentes": list(asistentes),
        "detalles": {}
    }
    print(f"Evento '{nombre_evento}' registrado con {len(asistentes)} asistente(s).")

def agregar_detalles_evento(nombre_evento, **detalles):
    if nombre_evento in eventos:
        eventos[nombre_evento]["detalles"].update(detalles)
        print(f"Detalles agregados al evento '{nombre_evento}'.")
    else:
        print(f"El evento '{nombre_evento}' no existe.")

def mostrar_reporte(nombre_evento, **filtros):
    if nombre_evento not in eventos:
        print(f"El evento '{nombre_evento}' no se encuentra registrado.")
        return

    evento = eventos[nombre_evento]
    detalles = evento["detalles"]
    asistentes = evento["asistentes"]

    print(f"\nReporte del Evento: {nombre_evento}")
    print(f"Asistentes ({len(asistentes)}):")
    for i, a in enumerate(asistentes, 1):
        print(f"  {i}. {a}")

    if filtros.get("mostrar_presupuesto", False):
        presupuesto = detalles.get("presupuesto", "No especificado")
        print(f"Presupuesto: {presupuesto}")

    if filtros.get("mostrar_tematica", False):
        tematica = detalles.get("tematica", "No especificada")
        print(f"Temática: {tematica}")

    if filtros.get("mostrar_numero_asistentes", False):
        print(f"Número total de asistentes: {len(asistentes)}")

registrar_evento("Conferencia Tech", "Ana López", "Luis Pérez", "Carlos Gómez")

agregar_detalles_evento(
    "Conferencia Tech",
    lugar="Auditorio Central",
    fecha="2025-08-10",
    hora="09:00",
    presupuesto=5000,
    tematica="Innovación tecnológica"
)

mostrar_reporte(
    "Conferencia Tech",
    mostrar_presupuesto=True,
    mostrar_tematica=True,
    mostrar_numero_asistentes=True
)
