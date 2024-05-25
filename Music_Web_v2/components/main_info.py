import reflex as rx

def main_info() ->rx.Component:
    return rx.hstack(
        rx.box(
            rx.heading("Trending New Song", size="3"),
            rx.box(
                rx.text("Lost Emotions", font_size="56px", margin_bottom="8px"),
                rx.hstack(
                    rx.text("Rion Clarke", display= "inline"),
                    rx.text("63 Million Plays", display="inline", margin_left="12px", color="#919191")
                ),
                rx.hstack(
                    rx.button(
                        "Listen Now",
                        border= "none",
                        border_radius= "14px",
                        font_weight= "regular",
                        padding="12px 16px",
                        width= "112px",
                        height= "40px",
                        cursor= "pointer",  
                        background_color= "indigo",
                        color= "#fff",
                        _hover= {"background_color": "#5773ff"}
                    ),
                    rx.icon(
                        tag="heart",
                        size= 36,
                        stroke_width="6px",
                        color= "#5773ff",
                        border= "1px solid #fff",
                        padding= "5px",
                        border_radius= "50%"
                    ),
                    margin_top="30px",
                    display= "flex",
                    align_items= "center",
                    gap= "16px",
                    cursor= "pointer"
                ),
                margin_top= "12px",
                padding= "26px"
            )
        ),
        rx.image(
            src="/trend.png",
            width = "300px",
            height = "200px",
            border_radius= "12px"
        ),
        display= "flex",
        margin_top= "40px",
        align_items= "center",
        justify_content= "space-between",
        color= "#fff"
    )