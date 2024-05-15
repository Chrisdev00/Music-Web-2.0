import json

class Detail:
    def __init__(self, icon, detail):
        self.icon = icon
        self.detail = detail
        

class Info:
    def __init__(self, name, name_two, name_three, detalles=[], library=[], playlist=[]):        
        self.name = name
        self.name_two = name_two
        self.name_three = name_three
        self.detalles = [Detail(**info) for info in detalles]
        self.library = [Detail(**info) for info in library]
        self.playlist = [Detail(**info) for info in playlist]
        


class Data:
    def __init__(self, media_list):

        self.media_list = [Info(**info) for info in media_list]


with open ("assets/data/data.json") as file:
    json_data = json.load(file)

data = Data(**json_data)