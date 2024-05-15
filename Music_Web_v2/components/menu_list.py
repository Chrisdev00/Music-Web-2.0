import reflex as rx
from Music_Web_v2.data import Info



def menu_list(informa: Info) ->rx.Component:
    return rx.vstack(
        
        rx.hstack( 
            rx.box(
                informa.detalles,
                rx.box(
                    rx.text(informa.name),
                    *[
                        rx.link(
                            rx.hstack(
                                rx.icon(info.icon),
                                info.detail
                            ),
                            cursor = "pointer",                            
                        )
                        for info in informa.detalles
                    ],
                    rx.text(informa.name_two),
                    *[
                        rx.hstack(
                            rx.icon(info.icon),
                            info.detail
                            
                        )
                        for info in informa.library
                    ],
                    rx.text(informa.name_three),
                    *[
                        rx.hstack(
                            rx.icon(info.icon),
                            info.detail
                            
                        )
                        for info in informa.playlist
                    ]
                )
            )       
        )
    )