import reflex as rx


def main_card_genres(tip:str, gen:str) ->rx.Component:
    return rx.box(        
        rx.text(tip, font_size="14px"),
        rx.text(gen, font_size="14px"),
        background_color= "#476a8a",
        padding= "22px 10px",
        display= "flex",
        justify_content= "center",
        border_radius= "6px",
        cursor= "pointer",
        flex_direction= "column",
        font_size= "14px",
        font_weight= "bold", 
        flex_wrap= "wrap",
        align_content= "center",
    )