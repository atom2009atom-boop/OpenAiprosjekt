
from chat import start_chat
from websok import start_web_chat
from billde import start_bilde

while True:
    print("1. chat")
    print("2. Chat med websøk")
    print("3. Bildegenerering")
    print("4. Avslutt")

    valg = input("Velg 1-4: ")

    if valg == "1":
        start_chat()
    elif valg == "2":
        start_web_chat()
    elif valg == "3":
        start_bilde()
    elif valg == "4":
        print("Ha det!")
        break
    else:
        print("Prøv igjen.")
