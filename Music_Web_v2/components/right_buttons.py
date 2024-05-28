import reflex as rx

# class PlayerState(rx.State):
#     current_index: int = 0
#     # Asume que tienes una lista de los nombres de los archivos en tu carpeta assets
#     mp3_files = ["song1.mp3", "song2.mp3", "song3.mp3"]

#     def next_song(self):
#         if self.current_index < len(self.mp3_files) - 1:
#             self.current_index += 1
#         else:
#             self.current_index = 0

#     def prev_song(self):
#         if self.current_index > 0:
#             self.current_index -= 1
#         else:
#             self.current_index = len(self.mp3_files) - 1

# class MediaPlayerState(rx.State):
#     is_playing: bool = False

#     def play(self):
#         self.is_playing = True

#     def pause(self):
#         self.is_playing = False

#     def toogle_play(self):
#         self.is_playing = not self.is_playing

# def MediaPlayer():
#     return rx.vstack(
#         rx.audio(url=f"/assets/{PlayerState.mp3_files[PlayerState.current_index]}", autoplay=True, controls=True),
#         rx.button("Anterior", on_click=PlayerState.prev_song),
#         rx.button("Siguiente", on_click=PlayerState.next_song),
#    )

def right_buttons() ->rx.Component:
    return rx.box(
        rx.hstack(
            rx.button(
                rx.icon(tag="repeat"),
                cursor= "pointer",
                #size= "3",
                color= "#fff",
                _hover= {"color": "black"}
            ),
            rx.button(
                rx.icon(tag="chevron-first"),
                cursor= "pointer",
                #size= "3",
                color= "#fff",
                _hover= {"color": "black"}
            ),
            rx.button(
                rx.icon(tag="play"),
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
                cursor= "pointer",
                #size= "3",
                color= "#fff",
                _hover= {"color": "black"}
            ),
            rx.button(
                rx.icon(tag="arrow-right-left"),
                cursor= "pointer",
                #size= "3",
                color= "#fff",
                _hover= {"color": "black"}
            ),
            display= "flex",
            align_items= "center",
            gap= "30px",
            margin_top= "24px",
            justify_content= "center"
        ),
        rx.box(
            rx.icon(tag="chevron-up", cursor="pointer", color="#fff"),
            rx.text("LYRICS"),
            display= "flex",
            flex_direction= "column",
            align_items= "center",
            position= "absolute",
            bottom= "8px"
        ),
        background_color= "#5773ff",
        height= "26%",  # 26%
        border_radius= "6px",
        display= "flex",
        flex_direction= "column",
        align_items= "center",
        position= "relative"  
    )