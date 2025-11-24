# plantas_storage.py

def guardar_plantas(plantas, archivo="plantas.txt"):
    """Guarda la lista de plantas en un archivo."""
    try:
        with open(archivo, "w") as f:
            for planta in plantas:
                f.write(planta + "\n")
        print("Plantas guardadas correctamente.")
    except Exception as e:
        print("Error guardando plantas:", e)


def cargar_plantas(archivo="plantas.txt"):
    """Carga plantas desde un archivo."""
    plantas = []
    try:
        with open(archivo, "r") as f:
            plantas = [line.strip() for line in f]
        print("Plantas cargadas correctamente.")
    except FileNotFoundError:
        print("Archivo no encontrado. Se creara al guardar.")
    except Exception as e:
        print("Error cargando plantas:", e)
    return plantas

if __name__ == "__main__":
    lista = ["Lilas", "Cactus", "Lilas Rosa"]
    guardar_plantas(lista)
    datos = cargar_plantas()
    print(datos)
