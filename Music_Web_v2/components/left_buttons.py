import reflex as rx
import Music_Web_v2.styles.styles as styles

def left_buttons(icon:str, text:str) -> rx.Component:
    return rx.box(
        rx.link(
            rx.hstack(
                rx.icon(
                    icon,
                    #size= 20
                ),
                rx.text(text),
                #margin_bottom = "5px",
                #margin_top = "5px",
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
            #font_weight= "medium",
            transition = "all 0.3s ease"
        ),
        display= "flex"
    )