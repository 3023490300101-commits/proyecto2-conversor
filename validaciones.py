def validar_numero(cadena, base):
    """
    Valida que la cadena no esté vacía, no pase de 128 caracteres,
    no tenga espacios ni caracteres inválidos según la base.
    Bases permitidas: 2 (binario), 8 (octal), 10 (decimal), 16 (hexadecimal).
    """
    if not cadena:
        return False, "Error: La entrada no puede estar vacía."
    
    if len(cadena) > 128:
        return False, "Error: La longitud máxima permitida es de 128 dígitos."

    caracteres_validos = {
        2: "01",
        8: "01234567",
        10: "0123456789",
        16: "0123456789ABCDEF"
    }
    
    permitidos = caracteres_validos.get(base, "")
    cadena_mayus = cadena.upper()
    
    for caracter in cadena_mayus:
        if caracter not in permitidos:
            return False, f"Error: El carácter '{caracter}' no es válido para base {base}."
            
    return True, cadena_mayus