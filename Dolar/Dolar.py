import reflex as rx

from Cabecera import navbar
#from C_en_proceso import 

def index() -> rx.Component:
   
    return rx.box(
        navbar(),
        #fotos_cabecera(),
    )

        
    


app = rx.App()
app.add_page(index)
