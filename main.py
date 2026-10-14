from validaciones import validar_numero
from conversiones import convertir
from practica import ejecutar_modo_practica

def menu_base(titulo):
    opciones = {1: (2, "Binario"), 2: (8, "Octal"), 3: (10, "Decimal"), 4: (16, "Hexadecimal")}
    while True:
        print("\n" + "=" * 35)
        print(titulo)
        print("=" * 35)
        print("1. Binario")
        print("2. Octal")
        print("3. Decimal")
        print("4. Hexadecimal")
        print("0. Volver al menú principal")
        eleccion = input("Seleccione una opción: ").strip()
        
        if eleccion == "0":
            return None, None
        elif eleccion in ["1", "2", "3", "4"]:
            codigo = int(eleccion)
            return opciones[codigo][0], opciones[codigo][1]
        else:
            print("Opción inválida. Intente de nuevo.")

def modulo_conversion(historial):
    base_origen, nombre_origen = menu_base("SELECCIONE LA BASE DE ORIGEN")
    if base_origen is None:
        return
        
    base_destino, nombre_destino = menu_base("SELECCIONE LA BASE DE DESTINO")
    if base_destino is None:
        return
        
    if base_origen == base_destino:
        print("\nError: No se permite seleccionar la misma base como origen y destino.")
        input("Presione Enter para volver...")
        return
        
    while True:
        print("\n" + "=" * 45)
        print(f"CONVERSIÓN: {nombre_origen.upper()} A {nombre_destino.upper()}")
        print("=" * 45)
        print("Ingrese un entero no negativo de hasta 128 dígitos.")
        print("Escriba 'volver' para regresar al menú principal.")
        numero_ingresado = input("Número a convertir: ").strip()
        
        if numero_ingresado.lower() == "volver":
            return
            
        es_valido, valor_o_error = validar_numero(numero_ingresado, base_origen)
        if not es_valido:
            print(f"\n{valor_o_error}")
            input("Presione Enter para corregir...")
            continue
            
        num_limpio = valor_o_error
        resultado, pasos = convertir(num_limpio, base_origen, base_destino)
        
        # Mostrar resultado y procedimiento
        print("\n" + "=" * 30)
        print("RESULTADO")
        print("=" * 30)
        print(f"Número ingresado: {num_limpio}")
        print(f"Base de origen: {nombre_origen}")
        print(f"Base de destino: {nombre_destino}")
        print(f"Resultado: {resultado}")
        print("\nPROCEDIMIENTO PASO A PASO")
        print("-" * 30)
        for paso in pasos:
            print(paso)
        print("-" * 30)
        
        # Guardar en historial
        historial.append({
            "entrada": num_limpio,
            "origen": nombre_origen,
            "destino": nombre_destino,
            "resultado": resultado
        })
        print("Conversión agregada al historial.")
        input("Presione Enter para continuar...")
        break

def modulo_historial(historial):
    while True:
        print("\n" + "=" * 35)
        print("HISTORIAL DE CONVERSIONES")
        print("=" * 35)
        
        if not historial:
            print("El historial está vacío.")
            input("Presione Enter para volver al menú...")
            break
            
        for i, registro in enumerate(historial, start=1):
            print(f"Registro {i}")
            print(f"  Entrada: {registro['entrada']}")
            print(f"  Origen: {registro['origen']}")
            print(f"  Destino: {registro['destino']}")
            print(f"  Resultado: {registro['resultado']}\n")
            
        print(f"Total de registros: {len(historial)}")
        print("1. Eliminar un registro")
        print("2. Vaciar historial")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            pos = input("Ingrese el número de registro a eliminar: ").strip()
            if pos.isdigit():
                indice = int(pos) - 1
                if 0 <= indice < len(historial):
                    eliminado = historial.pop(indice)
                    print(f"Registro {pos} eliminado exitosamente.")
                else:
                    print("Error: El número de registro no existe.")
            else:
                print("Error: Ingrese un valor numérico válido.")
            input("Presione Enter para continuar...")
        elif opcion == "2":
            historial.clear()
            print("El historial ha sido vaciado.")
            input("Presione Enter para continuar...")
            break
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")
            input("Presione Enter para continuar...")

def main():
    historial = []
    while True:
        print("\n" + "=" * 35)
        print("CONVERSOR DE SISTEMAS NUMÉRICOS")
        print("=" * 35)
        print("1. Realizar una conversión")
        print("2. Consultar el historial")
        print("3. Iniciar el modo de práctica")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            modulo_conversion(historial)
        elif opcion == "2":
            modulo_historial(historial)
        elif opcion == "3":
            ejecutar_modo_practica()
        elif opcion == "4":
            print("\nGracias por usar el conversor. ¡Hasta pronto!")
            break
        else:
            print("Error: Opción inválida. Ingrese un número del 1 al 4.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()