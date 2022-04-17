import json
import requests


def main():
    for i in range(100):
        response = requests.get('https://catfact.ninja/fact')

        facts = json.loads(response.text) #raw string from cat fact api
        with open("./Output Txt File/randomfile.txt", "a") as o: #sends the cat facts to a txt file
            for fact in facts["fact"]:
                o.write(fact)
            o.write("\n")
        i+=1

main()