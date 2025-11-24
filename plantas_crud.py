
plantas = []


def agregar_planta(nombre):
    """Agrega una planta a la lista."""
    plantas.append(nombre)
    print(f"Planta agregada: {nombre}")


def listar_plantas():
    """Muestra la lista de plantas."""
    if not plantas:
        print("No hay plantas registradas.")
    else:
        print("Lista de plantas:")
        for i, planta in enumerate(plantas, 1):
            print(f"{i}. {planta}")


def editar_planta(indice, nuevo_nombre):
    """Edita el nombre de una planta existente."""
    if 0 <= indice < len(plantas):
        plantas[indice] = nuevo_nombre
        print(f"Planta actualizada a: {nuevo_nombre}")
    else:
        print("indice invalido.")


def eliminar_planta(indice):
    """Elimina una planta de la lista por indice."""
    if 0 <= indice < len(plantas):
        eliminada = plantas.pop(indice)
        print(f"Planta eliminada: {eliminada}")
    else:
        print("Índice inválido.")


# Pruebas (puedes borrarlas si no las necesitas)
if __name__ == "__main__":
    agregar_planta("Lilas")
    agregar_planta("Cactus")
    listar_plantas()

    editar_planta(0, "Lilas Rosas")
    listar_plantas()

    eliminar_planta(1)
    listar_plantas()

