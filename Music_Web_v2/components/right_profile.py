import reflex as rx


def right_profile() ->rx.Component:
    return rx.hstack(
        rx.icon(tag="bell", color= "#fff", cursor= "pointer", font_size="20px"),
        rx.icon(tag="settings", color= "#fff", cursor= "pointer", font_size="20px"),
        rx.box(
            rx.box(
                rx.image(src="/profile.png", width="30px", height="30px"),
                display= "flex",
                align_items= "center",
                background= "#32323d",
                padding= "6px",
                border_radius= "6px 0 0 6px"
            ),
            rx.box(
                rx.text("Jhon Doe"),
                background_color= "#25252d",
                border_radius= "0 6px 6px 0",
                padding= "13px",
                color= "#fff"
            ),
            display= "flex"
        ),
        display= "flex",
        align_items= "center",
        gap= "18px",
        justify_content= "flex-end",
        margin_bottom= "40px"
    )