from time import sleep
import tweepy
from os import system

# Matheus Eduardo
# github.com/eumts

# - Definindo variáveis -

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)
user = api.me()

print("Logado como " + user.name)
print()

contaParaVerificar = input("Digite o @ da conta o qual você quer ver os followers: @")

# Função para salvar os followers

def init():
    contador = 0
    for user in tweepy.Cursor(api.followers, screen_name=contaParaVerificar).items():
        system("cls")
        print("O usuário @" + str(user.screen_name) + " foi adicionado à lista.")
        arquivo_contas = open('contas.txt', 'a')
        arquivo_contas.write("@" + str(user.screen_name) + "\n")
        arquivo_contas.close()
        contador += 1
        if(contador == 1):
            print(str(contador) + " conta no total.")
        else:
            print(str(contador) + " contas no total.")
        sleep(2)
        
init()
system("cls")
arquivo_contas = open('contas.txt', 'r')
linhas = arquivo_contas.readlines()
print(str(len(linhas)) + " contas foram adicionadas.")
print("Pressione enter para finalizar.")
input()