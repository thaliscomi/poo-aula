class Playlist:
    def __init__(self, id, nome, desc):
        self.id = id
        self.nome = nome
        self.desc = desc
    def toString(self):
        return f"Playlist {self.id}: {self.nome} - {self.desc}"

class Musica:
    def __init__(self, id, titulo, artista, album):
            self.id = id
            self.titulo = titulo
            self.artista = artista
            self.album = album
    def toString(self):
        return f"{self.titulo} - {self.artista} ({self.album})"

class PlaylistItem:
    def __init__(self, id, id_playlist, id_musica, seq):
        self.id = id
        self.id_playlist = id_playlist
        self.id_musica = id_musica
        self.seq = seq
    def toString(self):
        return f"Item {self.id}: Playlist {self.id_playlist}, Música {self.id_musica}, Seq {self.seq}"
class UI:
    def __init__(self):
        self.playlists = []
        self.musicas = []
        self.itens = []
    def inserir_playlist(self):
        id = int(input("ID: "))
        nome = input("Nome: ")
        desc = input("Descrição: ")

        self.playlists.append(Playlist(id, nome, desc))
    def listar_playlists(self):
        for p in self.playlists:
            print(p.toString())
    def inserir_musica(self):
        id = int(input("ID: "))
        titulo = input("Título: ")
        artista = input("Artista: ")
        album = input("Album: ")
        self.musicas.append(Musica(id, titulo, artista, album))
    def listar_musicas(self):
        for m in self.musicas:
            print(m.toString())
    def inserir_item(self):
        id = int(input("ID: "))
        idp = int(input("ID da Playlist: "))
        idm = int(input("ID da Música: "))
        seq = int(input("Sequência: "))
        self.itens.append(PlaylistItem(id, idp, idm, seq))
    def listar_itens(self):
        for i in self.itens:
            print(i.toString())

    def menu(self):
        while True:
            print("\n1 Inserir Playlist")
            print("2 Listar Playlists")
            print("3 Inserir Música")
            print("4 Listar Músicas")
            print("5 Inserir Item")
            print("6 Listar Itens")
            print("0 Sair")
            op = input("Escolha: ")
            if op == "1":
                self.inserir_playlist()
            elif op == "2":
                self.listar_playlists()
            elif op == "3":
                self.inserir_musica()
            elif op == "4":
                self.listar_musicas()
            elif op == "5":
                self.inserir_item()
            elif op == "6":
                self.listar_itens()
            elif op == "0":
                break

ui = UI()
ui.menu()