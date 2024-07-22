import pyautogui
import requests

link = "https://gshow.globo.com/realities/bbb/bbb-24/voto-da-torcida/votacao/voto-da-torcida-quem-voce-quer-eliminar-do-bbb-24-h0Hsk3SKbB.ghtml"

url="https://globo.com"

pagina = requests.get(url)


if "caricato" in pagina.links:
    print("Ok")  