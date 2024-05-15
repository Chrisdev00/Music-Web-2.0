import reflex as rx
from Music_Web_v2.components.menu_list import menu_list
from Music_Web_v2.data import Info




def left_section(data: list[Info]) ->rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.icon(tag="activity", stroke_width=2.5),
            rx.link(
                "AsmrProg"
            )
        ),
        rx.box(
            *[                
                menu_list(dat)
                for dat in data
            ]            
        )
    )