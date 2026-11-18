
import os
from openai import OpenAI
from dotenv import load_dotenv


#Leser API-nøkkelen fra .env
load_dotenv()

#Lage en funksjon for chatbot med websøk
def start_web_chat():

    #Henter OpenAI API-nøkkelen
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    #lag en klient som kan snakke med OpenAI API-et.
    client = OpenAI(api_key=OPENAI_API_KEY)

    #lag en tom liste som skal huske samtalen.
    historikk = []

    #programmet skal gjenta seg
    while True:

        #les inn et spørsmål fra brukeren
        sporsmal = input("Du: ")   #sporsmal lagerer det du skriver inn i terminalen

        #Stopper chatten når brukeren skriver exit
        if sporsmal.lower() == "exit":
            break

        #Lagrer spørsmålet i historikken
        historikk.append({
            "role": "user",
            "content": sporsmal

        })

        try:
            #Sender samtalen til GPT-6 luna
            response = client.responses.create(
                #KI modellen som skal brukes
                model="gpt-6-luna",

                tools=[{"type": "web_search"}],
                #Sender tidligere meldinger
                input=historikk
            )

            #hent ut teksten fra svaret
            tekst = response.output_text

            #skriv ut til skjerm svaret til terminalen
            print("KI:", tekst)

            #lagre svaret i historikken
            historikk.append({
                "role": "assistant",
                "content": tekst
            })

        #except blokken fanger opp feil som kan oppstå under kjøringen av koden
        except Exception as feil:
            #fjern det siste spørsmålet fra historikken, slik at det ikke blir sendt på nytt
            historikk.pop()
            #skriv ut til skjerm noe gikk galt, og hva feilen var
            print("Noe gikk galt:", feil)


#Start bare hvis denne Python-filen kjører direkte
if __name__ == "__main__":
    start_web_chat()
