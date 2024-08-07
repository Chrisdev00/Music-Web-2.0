# Componente que ya no se usa cambiado en la version 2

# import reflex as rx

# class PlayerState(rx.State):
    
#     current_index: int = 0
#     is_playing: bool = False
#     loop: bool = False
#     button_color: str = "#fff"

#     # Asume que tienes una lista de los nombres de los archivos en tu carpeta assets
#     mp3_files: list = [
#         "song-1.mp3", "song-2.mp3", "song-3.mp3",
#         "song-4.mp3", "song-5.mp3", "song-6.mp3",
#         "song-7.mp3", "song-8.mp3", "song-9.mp3",
#         "song-10.mp3", "song-11.mp3", "test.mp3"
#     ]

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

#     # def play(self):
#     #     self.is_playing = True

#     # def pause(self):
#     #     self.is_playing = False

#     def toogle_play(self):
#         self.is_playing = not self.is_playing

#     def repeat(self):
#         self.loop = not self.loop
#         if self.button_color == "#fff":
#             self.button_color = "black"
#         else:
#             self.button_color = "#fff"
    
    
# class VolumeControlState(rx.State):
    
#     show_slider: bool = False
#     volume: float = 0.5

#     def toggle_slider(self):
#         self.show_slider = not self.show_slider

#     def set_volume(self, value: list):
#         self.volume = value[0] / 100  # Asume que `value` es una lista y toma el primer elemento 



# def right_buttons() ->rx.Component:
#     return rx.box(
#         rx.audio(url=f"/audios/{PlayerState.mp3_files[PlayerState.current_index]}", 
#             controls=True, playing=PlayerState.is_playing,
#             volume=VolumeControlState.volume, width="350px", on_ended=PlayerState.next_song, class_name="audio" #loop=PlayerState.loop
#         ),
#         rx.hstack(
#             rx.button(
#                 rx.icon(tag="repeat"),
#                 color= PlayerState.button_color,
#                 on_click=PlayerState.repeat,
#                 cursor= "pointer",
#                 #size= "3",
#                 _hover= {"color": "black"}
#             ),
#             rx.button(
#                 rx.icon(tag="chevron-first"),
#                 on_click=PlayerState.prev_song,
#                 cursor= "pointer",
#                 #size= "3",
#                 color= "#fff",
#                 _hover= {"color": "black"}
#             ),
#             rx.button(
#                 rx.icon(tag="play"),
#                 on_click=PlayerState.toogle_play,
#                 padding= "9px",
#                 border_radius= "8px",
#                 cursor= "pointer",    
#                 #color= "#fff",
#                 width= "3rem",
#                 height= "3rem",
#                 color = "#5773ff",
#                 background_color="#fff",
#                 _hover= {
#                     "background_color": "gray",
#                     "color": "black"
#                 }
#             ),
#             rx.button(
#                 rx.icon(tag="chevron-last"),
#                 on_click=PlayerState.next_song,
#                 cursor= "pointer",
#                 #size= "3",
#                 color= "#fff",
#                 _hover= {"color": "black"}
#             ),
#             rx.button(
#                 #rx.icon(tag="arrow-right-left"),
#                 rx.icon(tag="volume-2"),
#                 on_click=VolumeControlState.toggle_slider,
#                 cursor= "pointer",
#                 #size= "3",
#                 color= "#fff",
#                 _hover= {"color": "black"},
#                 flex_direction= "column"
#             ),
#             rx.cond(
#                 VolumeControlState.show_slider,
#                 rx.slider(
#                     default_value=VolumeControlState.volume * 100,
#                     on_value_commit=VolumeControlState.set_volume,
#                     min=0,
#                     max=100,
#                     step=1,
#                     width="100px",
#                     color_scheme="indigo",
#                     #flex_direction="column"
#                 ),
#             ),
#             display= "flex",
#             align_items= "center",
#             gap= "30px",
#             margin_top= "24px",  # 24px
#             justify_content= "center"
#         ),
#         # rx.box(
#         #     rx.icon(tag="chevron-up", cursor="pointer", color="#fff"),
#         #     rx.text("LYRICS"),
#         #     display= "flex",
#         #     flex_direction= "column",
#         #     align_items= "center",
#         #     position= "absolute",
#         #     bottom= "8px"
#         # ),
#         background_color= "#0e263d",
#         height= "26%",  # 26%
#         border_radius= "6px",
#         display= "flex",
#         flex_direction= "column",
#         align_items= "center",
#         position= "relative",
        
#     )




# import asyncio
# import reflex as rx

# class VolumeControlState(rx.State):
#     volume: float = 0.5  # Establece el volumen inicial al 50%

#     def increase_volume(self):
#         if self.volume < 1.0:
#             self.volume += 0.1  # Aumenta el volumen en un 10%

#     def decrease_volume(self):
#         if self.volume > 0.0:
#             self.volume -= 0.1  # Disminuye el volumen en un 10%

# def audio_with_volume_control():
#     return rx.vstack(
#         rx.audio(
#             url="https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba.mp3",
#             volume=VolumeControlState.volume,
#             controls=True,
#         ),
#         rx.button("Aumentar Volumen", on_click=VolumeControlState.increase_volume),
#         rx.button("Disminuir Volumen", on_click=VolumeControlState.decrease_volume),
#     )



