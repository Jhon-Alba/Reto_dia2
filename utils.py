def texto_a_numero(valor: str):
    """
    Metodo para validar caracteres
    """
    while True:
        if valor.isnumeric():
            return int(valor)
        else:
            console.print(f"El siguiente texto {valor} no se puede convertir a numero", style="bold red")
            console.print("Ingrese nuevamente un numero", style="bold red")
            valor = input()