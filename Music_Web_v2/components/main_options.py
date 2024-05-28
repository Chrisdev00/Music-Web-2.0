import reflex as rx

def main_options()->rx.Component:
    return rx.hstack(
        rx.box(
            rx.link(
                "Music",
                href="#",
                text_transform="uppercase",
                color= "#919191",
                transition= "all 0.3s ease",
                _hover= {"color":"#5773ff"},
                text_decoration= "none"
            ),
            rx.link(
                "Live",
                href="#",
                text_transform="uppercase",
                color= "#919191",
                transition= "all 0.3s ease",
                _hover= {"color":"#5773ff"},
                text_decoration= "none"
            ),
            rx.link(
                "Podcast",
                href="#",
                text_transform="uppercase",
                color= "#919191",
                transition= "all 0.3s ease",
                _hover= {"color":"#5773ff"},
                text_decoration= "none"
            ),
            display= "flex",
            align_items= "center",
            gap= "20px"
        ),
        rx.hstack(
            rx.input(
                rx.input.slot(
                    rx.icon(tag="search", color= "#fff", cursor= "pointer")
                ),
                placeholder="Type here to search",
                width= "80%",
                size="3",
                background_color= "transparent",
                #border = "none",
                outline = "none",
                color = "#fff",
                border= "2px solid #464748",
                border_radius= "8px"
            ),
            width = "100%",
            display= "flex",
            align_items= "center",
            gap= "6px",
            #background_color= "#1d1d1d",
            #border= "1px solid #464748",
            padding= "10px 0",
            justify_content= "flex-end"
            #border_radius= "8px"
        ),
        display= "flex",
        align_items= "center",        
        #justify_content= "space-between"
    )