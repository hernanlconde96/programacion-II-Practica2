class ArithmeticException(Exception):
    pass

class NumeroInvalidoException(Exception):
    pass

class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b
    
    @staticmethod
    def restar(a, b):
        return a - b
    
    @staticmethod
    def multiplicar(a, b):
        return a * b
    
    @staticmethod
    def dividir(a, b):
        if b == 0:
            raise ArithmeticException("error: division por cero no permitida")
        return a / b
    
    @staticmethod
    def string_a_entero(texto):
        if not texto.strip():
            raise NumeroInvalidoException("error: texto vacio no es un numero")
        
        try:
            return int(texto)
        except ValueError:
            raise NumeroInvalidoException(f"error: '{texto}' no es un numero entero valido")







print("calculadora con entrada por teclado")
print("operaciones disponibles: sumar, restar, multiplicar, dividir")
print("escribe 'salir' para terminar\n")

while True:
    



    try:
        entrada1 = input("ingresa el primer numero: ")
        if entrada1.lower() == "salir":
            break
        
        num1 = Calculadora.string_a_entero(entrada1)
    except NumeroInvalidoException as e:
        print(e)
        continue

    





    try:
        entrada2 = input("ingresa el segundo numero: ")
        if entrada2.lower() == "salir":
            break
        
        num2 = Calculadora.string_a_entero(entrada2)
    except NumeroInvalidoException as e:
        print(e)
        continue

  
    operacion = input("ingresa la operacion (sumar/restar/multiplicar/dividir): ")
    if operacion.lower() == "salir":
        break

    


    try:
        if operacion == "sumar":
            resultado = Calculadora.sumar(num1, num2)
            print(f"resultado: {num1} + {num2} = {resultado}\n")
        elif operacion == "restar":
            resultado = Calculadora.restar(num1, num2)
            print(f"resultado: {num1} - {num2} = {resultado}\n")
        elif operacion == "multiplicar":
            resultado = Calculadora.multiplicar(num1, num2)
            print(f"resultado: {num1} * {num2} = {resultado}\n")
        elif operacion == "dividir":
            resultado = Calculadora.dividir(num1, num2)
            print(f"resultado: {num1} / {num2} = {resultado}\n")
        else:
            print("operacion no valida. usa: sumar, restar, multiplicar o dividir\n")
    except ArithmeticException as e:
        print(f"error: {e}\n")

print("programa terminado")