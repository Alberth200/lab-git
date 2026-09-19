
# ---------------------------------------------------------------------------
# Dominio del problema (evitar los  valores repetidos "quemados"
# dentro de las funciones y facilitan el mantenimiento)
# ---------------------------------------------------------------------------
TIPOS_CONSULTA_VALIDOS = ["matricula", "pagos", "constancia", "plataforma", "otro"]
LONGITUD_MINIMA_CODIGO = 6  # longitud minima definida por el equipo 

PRIORIDAD_POR_TIPO = {
    "plataforma": "Alta",   
    "pagos": "Alta",        
    "matricula": "Media",
    "constancia": "Media",
    "otro": "Baja",
}
# ---------------------------------------------------------------------------
# Funciones sin retorno 
# ---------------------------------------------------------------------------
def mostrar_menu():
    """Muestra el menu principal. No recibe parametros ni devuelve nada:
    solo presenta informacion (requerimiento 4 de la guia)"""
    print("\n===== SOPORTE ACADEMICO - MENU PRINCIPAL =====")
    print("1. Registrar solicitud")
    print("2. Ver resumen de la ultima solicitud")
    print("3. Listar solicitudes registradas")
    print("4. Salir")


def mostrar_resumen_solicitud(solicitud):
    """Imprime el resumen de UNA solicitud recibida por parametro.
    No usa variables globales (requerimientos 7 y 8)"""
    print("\n--- Resumen de la solicitud ---")
    print(f"Codigo de estudiante : {solicitud['codigo']}")
    print(f"Nombre               : {solicitud['nombre']}")
    print(f"Tipo de consulta     : {solicitud['tipo_consulta']}")
    print(f"Descripcion          : {solicitud['descripcion']}")
    print(f"Prioridad asignada   : {solicitud['prioridad']}")


# ---------------------------------------------------------------------------
# Funciones con retorno
# ---------------------------------------------------------------------------
def validar_texto_obligatorio(texto, longitud_minima=1):
    """Devuelve True si 'texto' no esta vacio y cumple una longitud minima.
    Funcion generica y reutilizable (requerimiento 6)"""
    texto_limpio = texto.strip() if texto else ""
    return len(texto_limpio) >= longitud_minima


def validar_codigo_estudiante(codigo):
    """Valida el codigo de estudiante reutilizando la funcion generica de
    texto obligatorio, con la longitud minima definida por el equipo
    (requerimiento 2)"""
    return validar_texto_obligatorio(codigo, LONGITUD_MINIMA_CODIGO)


def validar_tipo_consulta(tipo_consulta):
    """Devuelve True si el tipo de consulta pertenece a la lista basica
    permitida (requerimiento 3)"""
    if not validar_texto_obligatorio(tipo_consulta, 1):
        return False
    return tipo_consulta.strip().lower() in TIPOS_CONSULTA_VALIDOS


def calcular_prioridad(tipo_consulta):
    """Devuelve la prioridad de atencion segun el tipo de consulta
    (requerimiento 5). Si el tipo no es valido devuelve None; quien llama
    a la funcion decide que hacer con ese caso"""
    tipo_normalizado = tipo_consulta.strip().lower()
    return PRIORIDAD_POR_TIPO.get(tipo_normalizado)


def crear_solicitud(codigo, nombre, tipo_consulta, descripcion):
    """Construye y devuelve el registro (diccionario) de una solicitud.
    Todos los datos llegan por parametro; 'solicitud' es una variable
    LOCAL a esta funcion (requerimientos 1, 8 y 9)"""
    solicitud = {
        "codigo": codigo.strip(),
        "nombre": nombre.strip(),
        "tipo_consulta": tipo_consulta.strip().lower(),
        "descripcion": descripcion.strip(),
        "prioridad": calcular_prioridad(tipo_consulta),
    }
    return solicitud


# ---------------------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------------------
def registrar_solicitud_interactiva(lista_solicitudes):
    """Pide datos por teclado, valida y agrega la solicitud a la lista
    recibida por parametro. 'lista_solicitudes' se pasa explicitamente
    (no es global), cumpliendo el requerimiento 9"""
    codigo = input("Codigo de estudiante: ")
    if not validar_codigo_estudiante(codigo):
        print(f"Error: el codigo debe tener al menos {LONGITUD_MINIMA_CODIGO} caracteres.")
        return

    nombre = input("Nombre del estudiante: ")
    if not validar_texto_obligatorio(nombre, 2):
        print("Error: el nombre no puede estar vacio.")
        return

    tipo_consulta = input("Tipo de consulta (matricula/pagos/constancia/plataforma/otro): ")
    if not validar_tipo_consulta(tipo_consulta):
        print(f"Error: tipo de consulta invalido. Use uno de: {', '.join(TIPOS_CONSULTA_VALIDOS)}.")
        return

    descripcion = input("Descripcion breve: ")
    if not validar_texto_obligatorio(descripcion, 1):
        print("Error: la descripcion no puede estar vacia.")
        return

    nueva_solicitud = crear_solicitud(codigo, nombre, tipo_consulta, descripcion)
    lista_solicitudes.append(nueva_solicitud)
    print(f"Solicitud registrada correctamente. Prioridad asignada: {nueva_solicitud['prioridad']}")


def main():
    solicitudes = []  
    opcion = ""
    while opcion != "4":
        mostrar_menu()
        opcion = input("Elija una opcion: ").strip()

        if opcion == "1":
            registrar_solicitud_interactiva(solicitudes)
        elif opcion == "2":
            if not solicitudes:
                print("Todavia no hay solicitudes registradas.")
            else:
                mostrar_resumen_solicitud(solicitudes[-1])
        elif opcion == "3":
            print(f"\nTotal de solicitudes registradas: {len(solicitudes)}")
            for i, s in enumerate(solicitudes, start=1):
                print(f"{i}. {s['codigo']} - {s['nombre']} - {s['tipo_consulta']} - {s['prioridad']}")
        elif opcion == "4":
            print("Saliendo del sistema de soporte academico. Hasta pronto.")
        else:
            print("Opcion invalida. Intente nuevamente.")


if __name__ == "__main__":
    main()
