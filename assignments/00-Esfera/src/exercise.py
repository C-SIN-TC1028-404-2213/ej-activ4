import math

def main():
    #escribe tu código abajo de esta línea
    print("Area y Volumen de una esfera")
    print("============================")

    r=float(input("Dame el radio:"))

    area=4 * math.pi * r**2
    volumen=(4 * math.pi * r**3) / 3

    print(f"Area={area : 5.2f}")
    print(f"Volumen={volumen : 4.1f}")

if __name__=='__main__':
    main()
