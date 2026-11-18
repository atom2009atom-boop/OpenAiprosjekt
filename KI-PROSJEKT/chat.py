
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

#Lag en funksjon for chatbotten
def start_chat():
#lag en klient som kan snakke med OpenAI API-et.
    client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"]
    )
    #lag en tom liste som skal huske samtalen.
    historikk = []

    #programmet skal gjenta seg
    while True:
         
        #les inn et spørsmål fra brukeren
        sporsmal = input("Du: ") #sporsmal lagerer det du skriver inn i terminalen

        #sjekk om brukeren vil avslutte
        if sporsmal.lower() == "exit":
            break
        #lagre spørsmålet i historikken
        historikk.append({
        "role": "user",
        "content": sporsmal
        })
        #prøv å få svar fra KI-en
        
        try:
            #send en forespørsel til KI-en om å svare på spørsmålet
            svar = client.responses.create(
                model="gpt-6-luna",
                input=historikk,
            )
            #gå gjennom resultatene fra KI-en
            for melding in svar.output:
                if melding.type == "message":
                    tekst = melding.content[0].text
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
    start_chat()