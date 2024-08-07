import reflex as rx
from Music_Web_v2.components.right_profile import right_profile
from Music_Web_v2.components.right_player import right_player


def right_section() ->rx.Component:
    return rx.box(
        rx.box(
            right_profile()            
        ),
        rx.box(
            right_player(),
            background_color= "#202026",
            border_radius= "6px",
            display= "flex",
            flex_direction= "column",
            color= "#fff",
            height= "88%" #  88%
        ),
        # rx.box(
        #     right_music_card(),
        #     right_buttons(),
        #     #button_v2(),
        #     background_color= "#202026",
        #     border_radius= "6px",
        #     display= "flex",
        #     flex_direction= "column",
        #     # color= "#fff",
        #     # height= "88%" #  88%
        # ),
        padding= "20px 36px 0px 0px",
        display = ["flex", "flex", "flex", "flex", "flex"],
        flex_direction = "column",
        width = "100%"
    )