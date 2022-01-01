import os
import pytube
from youtube_search import YoutubeSearch

from utils import cls, download_folder

ITAG_AUDIO = 140        # itag 140 = apenas o audio (mp4 - 128 kbps)
ITAG_VIDEO = 22         # itag 22 = video e audio (30fps - 720p)


def yt_search(term):
    """Efetua a busca no youtube pelo termo informado"""
    results = YoutubeSearch(term, max_results=10).to_dict()
    videos = [{
        'url': item['url_suffix'],
        'title':f"{item['title']} ({item['duration']})"
    } for item in results]
    for index, video in enumerate(videos):
        print(f'{index:02} - {video["title"]}')
    else:
        print()

    if not videos:
        print(f"* YOUTUBE NÃO RETORNOU DADOS PARA A PESQUISA '{term}'")

    return videos


def do_download(url, itag):
    """Efetua o download do stream"""
    # define a url escolhida
    url = "https://www.youtube.com.br" + url
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(itag)

    print(f"Downloading... {stream.title}")
    stream.download(output_path=download_folder())
    output_file = os.path.join(download_folder(), stream.default_filename)
    print(f"\nSaved file in {output_file} ({stream.filesize} B)\n")
    input("Tecle ENTER")


def download_audio(video):
    do_download(video['url'], ITAG_AUDIO)


def download_video_audio(video):
    do_download(video['url', ITAG_VIDEO])


def processVideo(video):
    title = video['title']
    # print do video selecionado junta das opcoes para executar
    print(f'Video selecionado: {title}')
    print('')
    # print das opcoes
    # \n\n[x] para pesquisar novamente
    opcoes = {
        "a": ("Apenas o áudio (mp4 - 128 kbps)", download_audio),
        "v": ("Vídeo e áudio (30fps - 720p)", download_video_audio),
        "x": ("Sair", lambda x: None)
    }
    for opcao in opcoes.keys():
        print(f"[{opcao}] {opcoes[opcao][0]}")

    print('')

    # escolhe oque fazer e entao executa a tarefa
    watToDo = input('O que deseja fazer: ')
    if watToDo in opcoes:
        metodo = opcoes[watToDo][1]
        metodo(video)


while True:
    cls()
    print('+-------------------------------+\n'
          '|    Youtube Downloader Tool    |\n'
          '+-------------------------------+\n')
    # inicia a pesquisa por termos no youtube
    term = input("Pesquisar por qual termo: ")

    if not term:
        break

    videos = yt_search(term)

    if not videos:
        # Se não encontrou nenhum vídeo começa novamente
        _ = input("Tecle ENTER")
        continue

    # define qual da lista vai ser usado
    choose = int(input('Escolha um numero para download: '))
    if 0 <= choose < len(videos):
        processVideo(videos[choose])
    else:
        print("ERRO: Informe um vídeo da lista!")
        input("Tecle ENTER")

print("\nFim")