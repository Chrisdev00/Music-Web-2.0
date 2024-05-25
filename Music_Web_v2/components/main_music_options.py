import reflex as rx
from Music_Web_v2.data import Song
from Music_Web_v2.components.main_button_music import main_button_music

def main_music_options(deta: Song) ->rx.Component:
    return rx.box(
            *[
                main_button_music(ix.num, ix.img, ix.title, ix.singer, ix.dur)
                for ix in deta.info_songs
            ]
        )
    