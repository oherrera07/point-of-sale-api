from config.db.postgres.config import app
from models.user import *


@app.route("/")
def index():
    return "<p>Index route!</p>"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

