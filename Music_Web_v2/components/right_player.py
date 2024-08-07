import reflex as rx
import os

class TextChangeState(rx.State):
    texts: list[str] = []
    current_index: int = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load_texts()

    def load_texts(self):
        file_path = os.path.join("assets", "informacion.txt")
        with open(file_path, "r") as file:
            self.texts = [line.strip() for line in file.readlines()]

    def next_text(self):
        self.current_index = (self.current_index + 2) % len(self.texts)

    def previous_text(self):
        self.current_index = (self.current_index - 2) % len(self.texts)

class PlayerState(rx.State):

    index_img: int = 0
    music_index: int = 0
    is_playing: bool = False
    loop: bool = False
    button_color: str = "#fff"

    mp3_files: list = [
        "song-1.mp3", "song-2.mp3", "song-3.mp3",
        "song-4.mp3", "song-5.mp3", "song-6.mp3",
        "song-7.mp3", "song-8.mp3", "song-9.mp3",
        "song-10.mp3", "song-11.mp3", "test.mp3"
    ]

    images_files = [
        "image-1.jpg", "image-2.jpg", "image-3.jpg",
        "image-4.jpg", "image-5.jpg", "image-6.jpg",
        "image-7.jpg", "image-8.jpg", "image-9.jpg",
        "image-10.jpg", "image-11.jpg", "test.jpg",
    ]

    def next_song(self):
        if self.index_img < len(self.images_files) - 1 and self.music_index < len(self.mp3_files) - 1:
            self.index_img += 1
            self.music_index += 1
        else:
            self.index_img = 0
            self.music_index = 0

    def prev_song(self):
        if self.index_img > 0 and self.music_index > 0:
            self.index_img -= 1
            self.music_index -= 1
        else:
            self.index_img = len(self.images_files) - 1
            self.music_index = len(self.mp3_files) - 1

    def toogle_play(self):
        self.is_playing = not self.is_playing

    def repeat(self):
        self.loop = not self.loop
        if self.button_color == "#fff":
            self.button_color = "black"
        else:
            self.button_color = "#fff"

class VolumeControlState(rx.State):
    
    show_slider: bool = False
    volume: float = 0.5

    def toggle_slider(self):
        self.show_slider = not self.show_slider

    def set_volume(self, value: list):
        self.volume = value[0] / 100  # Asume que `value` es una lista y toma el primer elemento


def right_player() -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                rx.text("Player"),
                rx.icon(tag="list-music", cursor= "pointer", font_size= "20px", color= "white"),
                display= "flex",
                align_items= "center",
                justify_content= "space-between",
                margin_bottom= "30px"
            ),
            rx.box(
                rx.image(
                    src=f"/images/{PlayerState.images_files[PlayerState.index_img]}",
                    width= "280px",
                    height= "220px",
                    border_radius= "12px"
                ),
                rx.box(
                    rx.text(
                        TextChangeState.texts[TextChangeState.current_index],
                        font_size = "26px",
                        font_weight = "500",
                        margin_bottom = "8px",
                    ),
                    rx.text(TextChangeState.texts[TextChangeState.current_index + 1],
                        font_size = "16px", margin_bottom = "16px"
                    ),
                ),
                display= "flex",
                flex_direction= "column",
                #align_items= "center",
                gap= "24px",
                text_align= "center",
                flex_wrap= "wrap",
                align_content= "center"
            ),
            padding= "20px",
            height= "62%"
        ),
        rx.box(   # right buttons         
            rx.audio(url=f"/audios/{PlayerState.mp3_files[PlayerState.music_index]}",
                controls=True, playing=PlayerState.is_playing, volume=VolumeControlState.volume,
                width="400px", height="116px", 
                on_ended=[PlayerState.next_song, TextChangeState.next_text], 
                loop=PlayerState.loop, class_name="audio"
            ),
            rx.hstack(
                rx.button(
                    rx.icon(tag="repeat"),
                    color= PlayerState.button_color,
                    on_click=PlayerState.repeat,
                    cursor= "pointer",
                    #size= "3",
                    _hover= {"color": "black"}
                ),
                rx.button(
                    rx.icon(tag="chevron-first"),
                    on_click=[PlayerState.prev_song, TextChangeState.previous_text],
                    cursor= "pointer",
                    #size= "3",
                    color= "#fff",
                    _hover= {"color": "black"}
                ),
                rx.button(
                    rx.icon(tag="play"),
                    on_click=PlayerState.toogle_play,
                    padding= "9px",
                    border_radius= "8px",
                    cursor= "pointer",    
                    #color= "#fff",
                    width= "3rem",
                    height= "3rem",
                    color = "#5773ff",
                    background_color="#fff",
                    _hover= {
                        "background_color": "gray",
                        "color": "black"
                    }
                ),
                rx.button(
                    rx.icon(tag="chevron-last"),
                    on_click=[PlayerState.next_song, TextChangeState.next_text],
                    cursor= "pointer",
                    #size= "3",
                    color= "#fff",
                    _hover= {"color": "black"}
                ),
                rx.button(
                    rx.icon(tag="volume-2"),
                    on_click=VolumeControlState.toggle_slider,
                    cursor= "pointer",
                    #size= "3",
                    color= "#fff",
                    _hover= {"color": "black"},
                    flex_direction= "column"
                ),
                rx.cond(
                    VolumeControlState.show_slider,
                    rx.slider(
                        default_value=VolumeControlState.volume * 100,
                        on_value_commit=VolumeControlState.set_volume,
                        min=0,
                        max=100,
                        step=1,
                        width="100px",
                        color_scheme="indigo",
                        #flex_direction="column"
                    )
                ),
                display= "flex",
                align_items= "center",
                gap= "30px",
                margin_top= "38px",  # 24px
                justify_content= "center",
                position = "relative",
                top = "54px"
            ),
            rx.box(
                rx.icon(tag="chevron-up", cursor="pointer", color="#fff"),
                rx.text("LYRICS"),
                display= "flex",
                flex_direction= "column",
                align_items= "center",
                position= "relative",
                bottom= "-124px"
            ),
            background_color= "#0e263d",
            height= "59%",  # 26%
            border_radius= "6px",
            display= "flex",
            flex_direction= "column",
            align_items= "center",
            #position= "relative",
        ),
    )