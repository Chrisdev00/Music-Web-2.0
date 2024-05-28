import reflex as rx
from Music_Web_v2.data import Music, Song
from Music_Web_v2.components.main_card_genres import main_card_genres

def main_menu(inf: Music) ->rx.Component:
    return rx.box(
        *[
            main_card_genres(det.tipo, det.genero, det.color)
            for det in inf.cards
        ],
        display= "grid",
        gap= "10px",
        grid_template_columns= "1fr 1fr"
    )