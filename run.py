from app import create_app
from app.api.v1.views.party_views import Parties


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
