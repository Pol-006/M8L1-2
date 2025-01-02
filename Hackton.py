import random
def mensaje_random():
    mensajes = [
        "Recuerda que solo puedes poner 2 numeros",
        "Recuerda que solo tenemos las 4 operaciones basicas es decir suma, resta. multiplicación. division",
        "Pronto metere un historial",
        "No está la potenciacion así que multiplica el mismo numero 2 veces",
        "Tal vez meta logaritmos"
    ]
    return random.choice(mensajes)

print(mensaje_random())

class Calculadora:
    """Clase simple para realizar operaciones matemáticas básicas."""
    
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplica(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: División entre cero."

def main():
    calc = Calculadora()
    print("Calculadora con 4 operaciónes")
    print("1. Suma\n2. Resta\n3. Multiplicación\n4. División")
    
    try:
        opcion = int(input("Elige una operación (1-4): "))
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        if opcion == 1:
            print(f"Resultado: {calc.suma(num1, num2)}")
        elif opcion == 2:
            print(f"Resultado: {calc.resta(num1, num2)}")
        elif opcion == 3:
            print(f"Resultado: {calc.multiplica(num1, num2)}")
        elif opcion == 4:
            print(f"Resultado: {calc.divide(num1, num2)}")
        else:
            print("Opción no válida.")
    except ValueError:
        print("Error: Entrada no válida, ingresa números correctamente.")

if __name__ == "__main__":
    main()
