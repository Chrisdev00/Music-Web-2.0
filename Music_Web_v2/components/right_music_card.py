import reflex as rx
from Music_Web_v2.components.right_buttons import right_buttons

class MediaPlayerState(rx.State):
    is_playing: bool = False

    def play(self):
        self.is_playing = True

    def pause(self):
        self.is_playing = False

    def toogle_play(self):
        self.is_playing = not self.is_playing

def right_music_card() ->rx.Component:
    return rx.box(
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
                src="/player.png", 
                width= "280px",
                height= "220px",
                border_radius= "12px"
            ),
            rx.box(
                rx.text(
                    "Ripple Echoes",
                    font_size= "26px",
                    font_weight= "500",
                    margin_bottom= "8px"
                ), 
                rx.text("Kael Fisher", font_size= "16px", margin_bottom= "4px"), 
                rx.text("Best of 2024", color = "#919191", font_size = "12px", font_weight= "bold")
            ),
            rx.hstack(
                rx.text("02:45", font_size="11px"),
                rx.box(
                    rx.slider(default_value=75, min=10, max=340, size="2"),
                    width="100%"
                ),
                rx.text("01:02", font_size="11px"),
                
                # rx.audio(
                #     url="/audios/test.mp3",
                #     controls=True,
                #     playing=MediaPlayerState.is_playing,
                # ),
                # rx.button("Reproducir", on_click=MediaPlayerState.play, style={"backgroundColor": "green", "color": "white"}),
                # rx.button("Pausar", on_click=MediaPlayerState.pause),
                # rx.button("Reproducir/Pausar", on_click=MediaPlayerState.toogle_play),
                #spacing = "2",
                display= "flex",
                #flex_direction= "column",
                align_items= "center",
                margin= "10px 0"
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
        height= "86%"   # 86%     
    )