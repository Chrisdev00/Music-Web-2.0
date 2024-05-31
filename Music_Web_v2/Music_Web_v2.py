import reflex as rx
from Music_Web_v2.views.left_section import left_section
from Music_Web_v2.views.main_section import main_section
from Music_Web_v2.views.right_section import right_section
from Music_Web_v2 import data
from Music_Web_v2.styles.styles import BASE_STYLE


# class State(rx.State):
#     """The app state."""

Data = data.data


def index() -> rx.Component:
    return rx.grid(
        rx.theme_panel(default_open=False),
        left_section(Data.media_list),
        main_section(Data.genres, Data.music),
        right_section(),
        grid_template_columns= "1fr 4fr 2fr",
    )


app = rx.App(
    style=BASE_STYLE,
    stylesheets= [
        "https://fonts.googleapis.com/css2?family=Roboto:wght@300;500&display=swap",
        "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
    ],
    theme=rx.theme(
        appearance="dark"
    )
)
app.add_page(index)
