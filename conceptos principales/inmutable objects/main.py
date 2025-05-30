# =============================================================================
# 📦 TUPLA CONTENIENDO ELEMENTOS MUTABLES E INMUTABLES
# =============================================================================
# Autor: Pythonista
# Fecha: 2023-10-10
# 
# Este código muestra cómo una tupla (inmutable) puede contener elementos mutables
# (listas, diccionarios) que sí pueden modificarse, y elementos inmutables
# (tuplas internas) que no pueden cambiarse.
# =============================================================================

def main():
    # 🔹 Definimos una tupla con:
    #   - Una lista (mutable)
    #   - Un diccionario (mutable)
    #   - Otra tupla (inmutable)
    mi_tupla = (
        [3, 5, 7],          # 🟢 Lista (puede modificarse)
        {"a": 100, "b": 202},  # 🟢 Diccionario (puede modificarse)
        (4, 5, 6)            # 🔴 Tupla interna (inmutable)
    )
    
    print("\n🔷 Estado Inicial de la Tupla:")
    print(f"Tupla completa: {mi_tupla}")
    print(f"Tipo de mi_tupla: {type(mi_tupla)}")
    print(f"Tipo de mi_tupla[0]: {type(mi_tupla[0])}")
    print(f"Tipo de mi_tupla[1]: {type(mi_tupla[1])}")
    print(f"Tipo de mi_tupla[2]: {type(mi_tupla[2])}")
    
    # =========================================================================
    # 🔄 MODIFICANDO ELEMENTOS MUTABLES DENTRO DE LA TUPLA
    # =========================================================================
    print("\n🔄 Modificando la Lista y el Diccionario (elementos mutables):")
    
    # ✅ Modificamos la lista (agregamos un elemento)
    mi_tupla[0].append(99)
    print(f"\n✔ Se añadió un 4 a la lista: {mi_tupla[0]}")
    
    # ✅ Cambiamos un valor en el diccionario
    mi_tupla[1]["c"] = 505
    print(f"✔ Se añadió 'c': 505 al diccionario: {mi_tupla[1]}")
    
    # ✅ Eliminamos una clave del diccionario
    del mi_tupla[1]["a"]
    print(f"✔ Se eliminó la clave 'a': {mi_tupla[1]}")
    
    print("\n🔷 Estado Actualizado de la Tupla:")
    print(f"Tupla modificada: {mi_tupla}")
    
    # =========================================================================
    # ❌ INTENTANDO MODIFICAR ELEMENTOS INMUTABLES (ERROR)
    # =========================================================================
    print("\n❌ Intentando modificar la tupla interna (inmutable):")
    
    try:
        mi_tupla[2][0] = 99  # 🔴 Esto generará un error
    except TypeError as e:
        print(f"✖ Error al modificar la tupla interna: {e}")
    
    # =========================================================================
    # ❌ INTENTANDO REEMPLAZAR UN ELEMENTO DE LA TUPLA (ERROR)
    # =========================================================================
    print("\n❌ Intentando reemplazar un elemento de la tupla principal:")
    
    try:
        mi_tupla[0] = "nuevo_valor"  # 🔴 Esto también generará un error
    except TypeError as e:
        print(f"✖ Error al modificar la tupla principal: {e}")
    
    # =========================================================================
    # 📌 CONCLUSIÓN
    # =========================================================================
    print("\n📌 Conclusión:")
    print("- La tupla principal es INMUTABLE: no se pueden añadir, eliminar o reemplazar sus elementos.")
    print("- Los elementos MUTABLES dentro de la tupla (listas, diccionarios) SÍ pueden modificarse.")
    print("- Los elementos INMUTABLES (tuplas internas) NO pueden modificarse.")

if __name__ == "__main__":
    main()