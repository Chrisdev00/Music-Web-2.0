import reflex as rx

def main_options()->rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.link(
                "Music",
                href="#",
                text_transform="uppercase",
                color= "#919191",
                transition= "all 0.3s ease",
                _hover= {"color":"#5773ff"}
            ),
            rx.link(
                "Live",
                href="#",
                text_transform="uppercase",
                color= "#919191",
                transition= "all 0.3s ease",
                _hover= {"color":"#5773ff"}
            ),
            rx.link(
                "Podcast",
                href="#",
                text_transform="uppercase",
                color= "#919191",
                transition= "all 0.3s ease",
                _hover= {"color":"#5773ff"}
            ),
            display= "flex",
            align_items= "center",
            gap= "20px"
        ),
        rx.hstack(
            rx.input(
                rx.input.slot(
                    rx.icon(tag="search")
                ),
                placeholder="Type here to search",
                display= "flex",
                align_items= "center",
                gap= "6px",
                #"width": "70%",
                background_color= "#1d1d1d",
                border= "1px solid #464748",
                padding= "10px",
                border_radius= "8px"
            ),
        ),
        display = "flex",
        align_items= "center",
        gap = "20px"
    )