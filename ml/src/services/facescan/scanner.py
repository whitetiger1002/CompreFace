from src.services.facescan.backend.facenet.facenet import Facenet2018
from src.services.facescan.backend.insightface.insightface import InsightFace

ALL_BACKENDS = [Facenet2018, InsightFace]


class Scanner:
    """ Increases package usability """
    Facenet2018 = Facenet2018
    InsightFace = InsightFace


Scanners = {backend.ID: backend for backend in ALL_BACKENDS}
