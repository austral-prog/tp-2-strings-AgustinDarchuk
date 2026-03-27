def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    pass

    
    nom_ape = input("Nombre y apellido: ")
    mail = input("Email: ").lower()
    nom = nom_ape.strip().title()
    nota1 = int(input("Nota 1: "))
    nota2 = int(input("Nota 2: "))
    nota3 = int(input("Nota 3: "))


    alumno = "    FICHA DEL ALUMNO"
    print("=" * (len(alumno) + 4))
    print(alumno)
    print("=" * (len(alumno) + 4))
    
    print(f"Nombre: {nom_ape.title().strip()}")
    print(f"Email: {mail.lower()}")
    print(f"Caracteres en nombre: {len(nom)}")
    espacio = nom.find(" ")
    print(f"Iniciales: {nom[0]}{nom[espacio + 1]}")
    print(f"Usuario: {nom.lower()[espacio + 1:]}.{nom.lower()[:espacio]}")
    print(f"Email valido: {"@" in mail}")
    arroba = mail.find("@")
    print(f"Dominio: {mail[arroba + 1:]}")
    print(f"Nombre para archivo: {nom.replace(' ', '_')}")
    print(f"Cantidad de a: {nom.count('a')}")
    print(f"Codigo secreto: {nom.upper()[-1::-1]}")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"Suma: {nota1 + nota2 + nota3}")
    print(f"Promedio: {(nota1 + nota2 + nota3)/3}")
    print(f"Promedio entero: {(nota1 + nota2 + nota3)//3}")
    
    print("=" * (len(alumno) + 4))
    
