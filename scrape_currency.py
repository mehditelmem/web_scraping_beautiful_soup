from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").getText()
    rate = float(rate[:-5])
    print(rate)
    

get_currency('INR', 'AUD')



#si vous voulez enregistrer votre contenu dans un fichier text

'''def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    response = requests.get(url)
    # Vérifier si la requête s'est effectuée avec succès
    if response.status_code == 200:
        # Utiliser l'encodage utf-8 pour éviter les erreurs d'encodage
        content = response.content.decode('utf-8', 'ignore')
        with open('currency_data.txt', 'w', encoding='utf-8') as file:
            file.write(content)
        print("Contenu enregistré dans currency_data.txt")
    else:
        print("Erreur lors de la requête")

get_currency('INR', 'USD')'''