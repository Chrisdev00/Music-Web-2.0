import reflex as rx
import Music_Web_v2.styles.styles as styles

def left_buttons(icon:str, text:str) -> rx.Component:
    return rx.box(
        rx.link(
            rx.hstack(
                rx.icon(
                    icon
                ),
                rx.text(text),
                display = "flex",
                align_items = "center",
                gap = "18px",         
                _hover = {"color": "#5773ff"},
            ),
            href="#",
            display = "flex",
            direction = "row",
            gap = "20px",
            text_decoration = "none",
            color = "#fff",
            font_size= "15px",
            transition = "all 0.3s ease"
        ),
        display= "flex"
    )