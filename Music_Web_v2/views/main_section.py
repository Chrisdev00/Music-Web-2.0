import reflex as rx
from Music_Web_v2.components.main_options import main_options
from Music_Web_v2.components.main_info import main_info
from Music_Web_v2.components.main_menu import main_menu
from Music_Web_v2.components.main_music_options import main_music_options
from Music_Web_v2.data import Music, Song


def main_section(data: list[Music], det: list[Song]) -> rx.Component:
    return rx.grid(
        main_options(),
        main_info(),
        rx.box(
            rx.box(
                rx.hstack(
                    rx.text("Genres"),
                    rx.link(
                        "See all",
                        color= "#919191",
                        font_size= "12px"
                    ),
                    display= "flex",
                    align_items= "center",
                    justify_content= "space-between",
                    margin_bottom= "30px",
                ),
                rx.box(
                    *[
                        main_menu(dat)
                        for dat in data
                    ]                   
                ),
                width= "40%",
                color = "#fff",
                background_color= "#202026",
                padding= "20px",
                border_radius= "6px",
                display = ["none", "none", "none", "none", "grid"]
            ),
            rx.box(
                rx.box(
                    rx.hstack(
                        rx.text("Top Songs"),
                        rx.link("See All", color= "#919191", font_size= "12px"),
                        display= "flex",
                        justify_content= "space-between",
                        align_items= "center",
                        margin_bottom= "30px"
                    )
                ),
                rx.box(
                    *[
                        main_music_options(i)
                        for i in det
                    ]
                ),
                width= ["0%", "0%", "100%", "100%", "65%"],
                background_color= "#202026",
                padding= "20px",
                color= "#fff",
                border_radius= "6px"
            ),
            margin_top= "14px",
            display= "flex",
            gap = "20px"
        ),
        padding= "20px 36px",
        display = ["none", "none", "grid", "grid", "grid"]    
    )