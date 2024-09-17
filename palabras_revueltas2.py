print("\n¡Elige con que tamatica te gustaria jugar!\n")
print("1- Marcas de autos")
print("2- Cantantes Argentinos")
print("3- Comidas")
print("4- Deportes")
print("5- Jugadores de Futbol Argentinos")
print("6- Arte y Entretenimiento")
print("7- Peliculas")
print("8- Super Heroes")
print("9- Videojuegos")
print("10- Informatica\n")
opcion = input("Ingresa una opcion: ")

match opcion:
    case "1":
        print("Elegiste 1")
    case "2":
        print("Elegiste 2")
    case "3":
        print("Elegiste 3")
    case "4":
        print("Elegiste 4")
    case "5":
        print("Elegiste 5")
    case "6":
        print("Elegiste 6")
    case "7":
        print("Elegiste 7")
    case "8":
        print("Elegiste 8")
    case "9":
        print("Elegiste 9")
    case "10":
        print("Elegiste 10")
    case _:
        print("Opcion ingresada inexistente.")