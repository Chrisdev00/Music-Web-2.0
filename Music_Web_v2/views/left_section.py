import reflex as rx
from Music_Web_v2.components.left_list import left_list
import Music_Web_v2.styles.style_web as styles
from Music_Web_v2.data import Info


def left_section(data: list[Info]) ->rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.icon(
                tag="activity", 
                stroke_width=2.5,
                style=styles.links_styles
            ),
            rx.link(
                rx.text(
                    "Chrisdev00",
                    style=styles.links_styles
                )
            ),
            display = "flex",
            align_items ="center",
            gap = "6px"
        ),
        rx.vstack(
            *[                
                left_list(dat)
                for dat in data
            ]          
        ),
        rx.box(
            rx.box(
                rx.image(
                    src="/current.png",
                    width="36px",
                    height="36px"
                ),
                rx.text("Apple Homepod"),
                bg= "#32323d",
                border_radius= "6px 6px 0 0",
                padding ="10px",
                display = "flex",
                align_items = "center",
                gap = "10px",
                color = "#fff",
                font_size = "13px"
            ),
            rx.box(
                rx.icon(
                    tag="podcast",
                    cursor = "pointer",
                    font_size = "20px",
                    color = "white"
                ),
                rx.text(
                    "Playing on Device",
                    color = "#919191"
                ),
                bg= "#25252d",
                border_raidus = "0 0 6px 6px",
                padding = "8px",
                display = "flex",
                align_items = "center",
                justify_content = "center",
                gap = "6px",
                font_size = "13px"
            ),
            margin_right= "40px",
            width = "100%"
        ),
        #            mob//mob-tab//tablet//tab-des//desktop        
        display = ["none", "none", "none", "flex", "flex"],
        style=styles.section_style

    )