import reflex as rx

config = rx.Config(
    app_name="Dolar",
   
    api_url="https://dolar-sed5.onrender.com",
    
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://dolar-peach.vercel.app",
        
        ],

    plugins=[

        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)