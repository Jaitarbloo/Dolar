import reflex as rx

def navbar() -> rx.Component:
    return rx.box(
        rx.center(
            rx.hstack(
                # Lado Izquierdo: Título con estilo
                rx.text(
                    "Dolar Coreses",
                    style={
                        "font_family": "Georgia, serif",
                        "font_weight": "bold",
                        "font_style": "italic",
                    },
                    size="7",
                    color="black",
                ),
                
                rx.spacer(),
                
                # Lado Derecho: Menú desplegable visible
                rx.menu.root(
                    rx.menu.trigger(
                        rx.button(
                            rx.icon("menu", color="black", size=24),
                            variant="soft",
                            color_scheme="gray",
                            cursor="pointer",
                        ),
                    ),
                    rx.menu.content(
                        rx.menu.item("Cabezera"),
                        rx.menu.item("Platos"),
                        rx.menu.item("Juan"),
                        rx.menu.item("Platos"),
                        rx.menu.separator(),
                        rx.menu.item("Ubicación"),
                        size="2",
                        width="180px",
                    ),
                ),
                width="100%",
                max_width="1200px",  # Mantiene el contenido centrado en pantallas grandes
                padding_x="2em",
                align="center",
            ),
            width="100%",
        ),
        # Propiedades del contenedor fijo
        position="fixed",
        width="100%",
        top="0",
        z_index="999",
        background_color="white",
        padding_y="1em",
        border_bottom="1px solid #F0F0F0",
    )
