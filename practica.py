import random
from conversiones import desde_decimal, a_decimal, convertir
from validaciones import validar_numero

def ejecutar_modo_practica():
    aciertos = 0
    total_ejercicios = 0
    nombres = {2: "Binario", 8: "Octal", 10: "Decimal", 16: "Hexadecimal"}
    bases_disponibles = [2, 8, 10, 16]
    
    while True:
        porcentaje = (aciertos / total_ejercicios * 100) if total_ejercicios > 0 else 0.0
        print("\n" + "=" * 40)
        print("MODO DE PRÁCTICA")
        print("=" * 40)
        print(f"Aciertos: {aciertos}")
        print(f"Ejercicios respondidos: {total_ejercicios}")
        print(f"Porcentaje de aciertos: {porcentaje:.1f}%")
        print("\n1. Resolver un nuevo ejercicio")
        print("2. Reiniciar puntuación")
        print("3. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            # Número decimal aleatorio entre 0 y 255
            val_dec = random.randint(0, 255)
            base_orig = random.choice(bases_disponibles)
            bases_posibles_dest = [b for b in bases_disponibles if b != base_orig]
            base_dest = random.choice(bases_posibles_dest)
            
            num_origen, _ = desde_decimal(val_dec, base_orig)
            res_esperado, _ = desde_decimal(val_dec, base_dest)
            
            while True:
                print("\n" + "=" * 40)
                print("EJERCICIO DE PRÁCTICA")
                print("=" * 40)
                print(f"Convierta {num_origen} de {nombres[base_orig]} a {nombres[base_dest]}.")
                print("Ingrese únicamente el número de la respuesta.")
                entrada = input("Su respuesta: ").strip()
                
                es_valido, msj_o_limpio = validar_numero(entrada, base_dest)
                if not es_valido:
                    print(msj_o_limpio)
                    print("Intente nuevamente.")
                    continue
                
                # Evaluación
                total_ejercicios += 1
                if msj_o_limpio == res_esperado:
                    aciertos += 1
                    print("\n¡Respuesta correcta!")
                else:
                    print(f"\nRespuesta incorrecta. La respuesta esperada era: {res_esperado}")
                    
                input("Presione Enter para continuar...")
                break
                
        elif opcion == "2":
            aciertos = 0
            total_ejercicios = 0
            print("Puntuación reiniciada a 0.")
            input("Presione Enter para continuar...")
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")