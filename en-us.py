from time import sleep
import tweepy
from os import system

# Matheus Eduardo
# github.com/eumts

# - Variables -

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)
user = api.me()

print("Logged as " + user.name)
print()

verifyAccount = input("Write the name of the account that you want to see the followers: @")

# Saving the followers

def init():
    contador = 0
    for user in tweepy.Cursor(api.followers, screen_name=verifyAccount).items():
        system("cls")
        print("O usuário @" + str(user.screen_name) + " foi adicionado à lista.")
        arquivo_contas = open('accounts.txt', 'a')
        arquivo_contas.write("@" + str(user.screen_name) + "\n")
        arquivo_contas.close()
        contador += 1
        if(contador == 1):
            print(str(contador) + " account in total.")
        else:
            print(str(contador) + " accounts in total.")
        sleep(2)
        
init()
system("cls")
arquivo_contas = open('accounts.txt', 'r')
linhas = arquivo_contas.readlines()
print(str(len(linhas)) + " accounts where added.")
print("Press enter to finish.")
input()