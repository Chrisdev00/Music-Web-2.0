import reflex as rx
import Music_Web_v2.styles.styles as styles

def left_buttons(icon:str, text:str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(
                icon,
                font_size= "20px"
            ),
            text,
            margin_bottom = "5px",
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
        font_size= "14px",
        font_weight= "medium",
        transition = "all 0.3s ease"
    )