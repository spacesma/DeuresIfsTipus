print("Juguem a pedra, paper i tissores!")

Jugadornúm1 = input("Pedra, paper o tissores:")
Jugadornúm2 = input("Pedra, paper o tissores:")

if Jugadornúm1 == Jugadornúm2:
    print("Empate")
elif (Jugadornúm2 == "pedra" and Jugadornúm2 == "tissores") or \
     (Jugadornúm2 == "paper" and Jugadornúm2 == "pedra") or \
     (Jugadornúm2 == "tissores" and Jugadornúm2 == "paper"):
    
    print("Guanya el Jugador 2!")
else:
    print("Guanya el Jugador 1!")