from openai import OpenAI
from dotenv import load_dotenv
import base64
import uuid #ulike ID-er for å lage unike filnavn
import os

load_dotenv()


PROMPT = "En tabby katt i en skummel skog med grønne øyne og tåke"

def start_bilde():

    
    try:
        #send en forespørsel til KI-en om å generere et bilde basert på PROMPT
        svar = OpenAI().responses.create(
            model="gpt-6-luna",
            input=PROMPT,
            tools=[{"type": "image_generation", "model": "gpt-image-2.5-sunburst"}],
            
        )
        #Gå gjennom resltatene fra KI-en.
        for bilde in svar.output:
            if bilde.type == "image_generation_call":
                #for å være uniktig, lag et filnavn med en UUID
                filnavn = f"bilde_{uuid.uuid4().hex}.png" #hex gir id som tekst med bokstaver og tall. uuid4() lager en tilfeldig id. .png er filtype for bilder
                #Opprettet bidleif
                with open(filnavn, "xb") as fil:
                    fil.write(base64.b64decode(bilde.result))

                print("Lagret her:", os.path.abspath(filnavn))
                return

        print("Fant ikke bilde.")

    except Exception as feil:
        print("Feil:", feil)

if __name__ == "__main__":
    start_bilde()