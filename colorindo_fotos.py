import Algorithmia
import os

API_KEY = os.environ['API_KEY'] 

client = Algorithmia.client(API_KEY) # insera sua chave de API aqui
algo = client.algo('deeplearning/ColorfulImageColorization/1.1.5')
imagem = algo.pipe("data://Cloves/Imagens_brasil/Menininha_Gantois_1902.jpg")