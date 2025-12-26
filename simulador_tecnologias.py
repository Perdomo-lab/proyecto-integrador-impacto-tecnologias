print("==============================================")
print("SIMULADOR DEL IMPACTO DE LAS NUEVAS TECNOLOGÍAS")
print("==============================================")

opcion = 0

# Ciclo principal que mantiene activo el programa hasta que el usuario decida salir
while opcion != 5:
    print("\nMENÚ PRINCIPAL")
    print("1. Inteligencia Artificial")
    print("2. Automatización del trabajo")
    print("3. Educación digital")
    print("4. Redes sociales")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    # Condicional para evaluar la opción seleccionada
    if opcion == 1:
        print("\nINTELIGENCIA ARTIFICIAL")
        print("Impactos positivos:")
        print("- Automatización de procesos")
        print("- Apoyo en la toma de decisiones")
        print("Impactos negativos:")
        print("- Dependencia tecnológica")
        print("- Riesgos éticos")
        print("Escenario futuro:")
        print("La inteligencia artificial será una herramienta clave si se usa de forma responsable.")

        volver = input("\n¿Desea volver al menú? (s/n): ")
        if volver != "s":
            break

    elif opcion == 2:
        print("\nAUTOMATIZACIÓN DEL TRABAJO")
        print("Impactos positivos:")
        print("- Mayor productividad")
        print("- Reducción de errores humanos")
        print("Impactos negativos:")
        print("- Pérdida de empleos")
        print("- Desigualdad laboral")
        print("Escenario futuro:")
        print("Será necesario adaptar las habilidades laborales a los cambios tecnológicos.")

        volver = input("\n¿Desea volver al menú? (s/n): ")
        if volver != "s":
            break

    elif opcion == 3:
        print("\nEDUCACIÓN DIGITAL")
        print("Impactos positivos:")
        print("- Acceso a educación a distancia")
        print("- Flexibilidad de aprendizaje")
        print("Impactos negativos:")
        print("- Brecha digital")
        print("- Falta de interacción social")
        print("Escenario futuro:")
        print("La educación combinará modelos presenciales y digitales.")

        volver = input("\n¿Desea volver al menú? (s/n): ")
        if volver != "s":
            break

    elif opcion == 4:
        print("\nREDES SOCIALES")
        print("Impactos positivos:")
        print("- Comunicación global")
        print("- Acceso rápido a información")
        print("Impactos negativos:")
        print("- Desinformación")
        print("- Problemas de privacidad")
        print("Escenario futuro:")
        print("Será importante regular el uso responsable de las redes sociales.")

        volver = input("\n¿Desea volver al menú? (s/n): ")
        if volver != "s":
            break

    elif opcion == 5:
        print("\nSaliendo del simulador...")

    else:
        print("\nOpción no válida, intente nuevamente.")
