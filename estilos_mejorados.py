# estilos_mejorados.py
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
RESET = "\033[0m"

def titulo(texto):
    """Devuelve un texto formateado como titulo."""
    return f"{AZUL}{texto.upper()}{RESET}"

def exito(texto):
    """Devuelve texto formateado como mensaje de correcta ejecucion."""
    return f"{VERDE}✔ {texto}{RESET}"

def advertencia(texto):
    """Devuelve texto como advertencia."""
    return f"{AMARILLO}! {texto}{RESET}"
if __name__ == "__main__":
    print(titulo("Sistema de Plantas"))
    print(exito("La planta fue agregada correctamente"))
    print(advertencia("El nombre es muy corto"))
