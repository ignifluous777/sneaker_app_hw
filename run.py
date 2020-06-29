from flask_routes.routes import app
from models.sneaker_listing import SneakList

SneakList.dbpath = "data/sneaker_list.db"

app.run()
