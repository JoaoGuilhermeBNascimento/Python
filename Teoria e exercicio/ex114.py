import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.cap.seduh.df.gov.br/')
except urllib.error.URLError:
    print('O site da CAP não está acessível no momento')
else:
    print('Consegui acessar o site da CAP com sucesso')
    #print(site.read())#consegue ler o conteudo do site, o contéudo html