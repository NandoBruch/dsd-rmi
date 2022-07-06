import Pyro4
uri = input("Digite a uri\n").strip()
youtube = Pyro4.Proxy(uri)


while True:
    opcao = int(input('Selecione uma das opções a seguir:\n [0] - Buscar um vídeo\n [1] - Buscar do histórico\n [2] - Sair\n'))
    if opcao == 0:
        video = input(f'Bem vindo, qual vídeo voce deseja pesquisar?\n')
        print(youtube.search(video))
    elif opcao == 1:
        print(youtube.list_queue())
        video_index = int(input('Qual vídeo voce deseja recuperar?\n'))
        print(youtube.get_video_by_index(video_index))
    else: break