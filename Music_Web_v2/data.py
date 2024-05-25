import json

# ////////////////////////

class Detail:
    def __init__(self, icon, detail):
        self.icon = icon
        self.detail = detail

class DetailMusic:
    def __init__(self, tipo, genero):
        self.tipo = tipo
        self.genero = genero

class InfoMusic:
    def __init__(self, num, img, title, singer, dur):
        self.num = num
        self.img = img
        self.title = title
        self.singer = singer
        self.dur = dur
        
# //////////////////

class Info:
    def __init__(self, name, name_two, name_three, detalles=[], library=[], playlist=[]):        
        self.name = name
        self.name_two = name_two
        self.name_three = name_three
        self.detalles = [Detail(**info) for info in detalles]
        self.library = [Detail(**info) for info in library]
        self.playlist = [Detail(**info) for info in playlist]

class Music:
    def __init__(self, cards=[]):
        self.cards = [DetailMusic(**info) for info in cards]
        
class Song:
    def __init__(self, info_songs=[]):
        self.info_songs = [InfoMusic(**info) for info in info_songs]

# /////////////////

class Data:
    def __init__(self, media_list, genres, music):

        self.media_list = [Info(**info) for info in media_list]
        self.genres = [Music(**info) for info in genres]
        self.music = [Song(**info) for info in music]


with open ("assets/data/data.json") as file:
    json_data = json.load(file)

data = Data(**json_data)