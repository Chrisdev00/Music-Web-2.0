import reflex as rx
from Music_Web_v2.data import Info
from Music_Web_v2.components.left_buttons import left_buttons
from Music_Web_v2.styles.styles import Size, EmSize



def left_list(informa: Info) ->rx.Component:
    return rx.vstack(        
        rx.hstack(
            rx.vstack(
                rx.text(
                    informa.name,
                    color = "#919191",
                    #margin_bottom = "12px",
                    text_transform = "uppercase"
                ),
                *[
                    left_buttons(info.icon, text=info.detail)
                    for info in informa.detalles
                ],
                rx.text(informa.name_two),
                *[
                    left_buttons(info.icon, text=info.detail)
                    for info in informa.library
                ],
                rx.text(informa.name_three),
                *[
                    left_buttons(info.icon, text=info.detail)
                    for info in informa.playlist
                ],
                gap = "0.8em"
            )
        )
    )