from quart import (
    Quart
)

from routes.API import api

app = Quart(
    __name__,
    template_folder='templates',
    static_folder='static'
    )

app.register_blueprint(api)