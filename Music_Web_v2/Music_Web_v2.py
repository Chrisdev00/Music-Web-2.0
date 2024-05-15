import reflex as rx
from Music_Web_v2.views.left_section import left_section
from Music_Web_v2 import data


# class State(rx.State):
#     """The app state."""

Data = data.data


def index() -> rx.Component:
    return rx.vstack(
        left_section(Data.media_list),
        grid_template_columns= "1fr 4fr 2fr",
    )


app = rx.App()
app.add_page(index)
