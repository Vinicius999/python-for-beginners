import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except:
    print('\033[31mO site Pudim não está acessível no momento.\033[m')
else:
    print('\033[34mConsegui acessar o site Pudim com sucesso!\033[m')
    print(site.read())
