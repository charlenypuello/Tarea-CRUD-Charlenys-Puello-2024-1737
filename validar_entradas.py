
# validar_entradas.py
# Validación de entrada para nombres de plantas

def validar_nombre(nombre):
    """Valida que el nombre de la planta no este vacio ni sea muy corto."""
    if not nombre.strip():
        return False, "El nombre no puede estar vacio."
    if len(nombre) < 3:
        return False, "El nombre debe tener al menos 3 caracteres."
    return True, "Nombre valido."

if __name__ == "__main__":
    pruebas = ["", "A", "Peoneas", "Zuculentas"]
    for p in pruebas:
        valido, mensaje = validar_nombre(p)
        print(f"{p} → {mensaje}")

