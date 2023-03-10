import falcon
import json
from sqlalchemy.orm import Session

from model import DogModel

class Resource():
    def __init__(self, session: Session):
        self.session = session

    def on_get(self, req, resp):
        dogs = self.session.query(DogModel).all()
        results = [
            {
                "id": dog.id,
                "breed": dog.breed,
                "color": dog.color
            } for dog in dogs]

        # Create a JSON representation of the resource
        resp.text = json.dumps({"results": results}, ensure_ascii=False)
