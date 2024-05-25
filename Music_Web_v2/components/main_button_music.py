import reflex as rx


def main_button_music(num:str, img:str, title: str, singer:str, dur:str) ->rx.Component:
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.text(
                    num,
                    color= "#919191",
                    font_size= "12px",
                    font_weight= "bold",
                    margin_top= "6px"
                ),
                rx.image(src=img, width="50px", height="50px"),
                rx.box(
                    rx.text(title),
                    rx.text(
                        singer,
                        color= "#919191",
                        font_size= "12px",
                        margin_top= "6px"
                    ),
                ),
                display= "flex",
                align_items= "center",
                gap= "20px"
            ),
            rx.hstack(
                rx.text(dur, font_size="13px", font_weight="bold"),
                rx.box(
                    rx.icon(
                        tag="play",
                        cursor= "pointer",
                        font_size= "20px",
                        width="12px",
                        height="12px",
                        color="#5773ff"
                    ),
                    display= "flex",
                    align_items= "center",
                    justify_content= "center",
                    background_color= "#32323d",
                    padding= "6px",
                    border= "2px solid #464748",
                    border_radius= "6px"
                ),
                rx.icon(
                    tag="square_plus",
                    cursor= "pointer",
                    font_size= "20px",
                    color= "#919191"
                ),
                display= "flex",
                align_items= "center",
                gap= "20px"
            ),
            display= "flex",
            align_items= "center",
            justify_content= "space-between",
            margin_bottom= "20px"
        )
    )