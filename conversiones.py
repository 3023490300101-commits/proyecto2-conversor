VALORES_HEX = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}
DIGITOS_HEX = "0123456789ABCDEF"

def a_decimal(cadena, base_origen):
    """
    Algoritmo de Notación Posicional.
    Convierte una cadena en base 2, 8 o 16 a su valor decimal (entero),
    generando el texto del procedimiento paso a paso.
    """
    if base_origen == 10:
        # Interpretación manual carácter a carácter de una entrada decimal
        valor_dec = 0
        for digito in cadena:
            valor_dec = valor_dec * 10 + VALORES_HEX[digito]
        return valor_dec, ["Base de origen ya es Decimal. No requiere conversión intermedia."]
    
    procedimiento = []
    cadena_rev = cadena[::-1]
    total = 0
    
    for posicion in range(len(cadena_rev)):
        simbolo = cadena_rev[posicion]
        valor_simbolo = VALORES_HEX[simbolo]
        peso = base_origen ** posicion
        aporte = valor_simbolo * peso
        total += aporte
        procedimiento.append(f"{simbolo} (valor {valor_simbolo}) x {base_origen}^{posicion} = {aporte}")
        
    procedimiento.append(f"Suma de los aportes: {total}")
    return total, procedimiento


def desde_decimal(numero_decimal, base_destino):
    """
    Algoritmo de Divisiones Sucesivas.
    Convierte un entero decimal a base 2, 8 o 16,
    generando el texto del procedimiento paso a paso.
    """
    if base_destino == 10:
        return str(numero_decimal), ["Base de destino ya es Decimal."]
    
    if numero_decimal == 0:
        return "0", [f"El valor decimal es 0, por lo que su representación en base {base_destino} es 0."]
    
    procedimiento = []
    residuos = []
    actual = numero_decimal
    
    while actual > 0:
        cociente = actual // base_destino
        residuo = actual % base_destino
        digito_resultante = DIGITOS_HEX[residuo]
        residuos.append(digito_resultante)
        procedimiento.append(f"{actual} / {base_destino}: cociente = {cociente}, residuo = {residuo}, dígito = {digito_resultante}")
        actual = cociente
        
    residuos_invertidos = residuos[::-1]
    resultado_str = "".join(residuos_invertidos)
    procedimiento.append(f"Leer los residuos del último al primero: {resultado_str}")
    
    return resultado_str, procedimiento


def convertir(cadena_numero, base_origen, base_destino):
    """
    Ejecuta la conversión usando Decimal como base intermedia si es necesario.
    """
    nombres_bases = {2: "Binario", 8: "Octal", 10: "Decimal", 16: "Hexadecimal"}
    registro_pasos = []
    
    if base_origen == base_destino:
        return cadena_numero, ["Origen y destino son iguales."]
    
    # Etapa 1: Origen -> Decimal
    if base_origen != 10:
        registro_pasos.append(f"ETAPA 1: {nombres_bases[base_origen].upper()} A DECIMAL")
        val_decimal, pasos_etapa1 = a_decimal(cadena_numero, base_origen)
        registro_pasos.extend(pasos_etapa1)
    else:
        val_decimal, _ = a_decimal(cadena_numero, 10)
        
    # Etapa 2: Decimal -> Destino
    if base_destino != 10:
        etiqueta_etapa = "ETAPA 2" if base_origen != 10 else "ETAPA 1"
        registro_pasos.append(f"{etiqueta_etapa}: DECIMAL A {nombres_bases[base_destino].upper()}")
        resultado_final, pasos_etapa2 = desde_decimal(val_decimal, base_destino)
        registro_pasos.extend(pasos_etapa2)
    else:
        resultado_final = str(val_decimal)
        
    return resultado_final, registro_pasos