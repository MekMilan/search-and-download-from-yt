# itag 140 = apenas o audio (mp4 - 128 kbps)
# itag 22 = video e audio (30fps - 720p)

import os
from youtube_search import YoutubeSearch
import pytube

i = -1
urls = []
titleVideos = []

os.system("cls")

print('+-------------------------------+\n|    Youtube Downloader Tool    |\n+-------------------------------+\n')

# inicia a pesquisa por termos no youtube
term = input("Pesquisar por qual termo: ")
results = YoutubeSearch(term, max_results=10).to_dict()

os.system("cls")

for item in results:
    i += 1
    print(f"{i} " + item['title'])
    urls.append(item['url_suffix'])
    titleVideos.append(item['title'])

print('')

# define qual da lista vai ser usado
choose = int(input('Escolha um numero para download: '))
os.system('cls')

# print do video selecionado junta das opcoes para executar
print(f'Video selecionado: {titleVideos[choose]}')
print('')

# print das opcoes
print('[a] apenas o audio(mp4 - 128 kbps)\n[v] video e audio(30fps - 720p)') #\n\n[x] para pesquisar novamente
print('')

# escolhe oque fazer e entao executa a tarefa
watToDo = input('Oque deseja fazer: ')
print('')
if watToDo == "a":

    # define a url escolhida
    url = "https://www.youtube.com.br" + urls[choose]

    # faz o processo de download apenas do audio
    video = pytube.YouTube(url)    
    stream = video.streams.get_by_itag(140)
    print(f"Downloading... {stream.title}")
    stream.download(output_path="C:\\Users\\mekmi\\Desktop\\")
    print('')
    print("Done !")   
    print('') 

elif watToDo == "v":

    # define a url escolhida
    url = "https://www.youtube.com.br" + urls[choose]

    # faz o processo de download do video e audio
    video = pytube.YouTube(url)    
    stream = video.streams.get_by_itag(22)
    print(f"Downloading... {stream.title}")
    stream.download()
    print('')
    print("Done !")
    print('')
