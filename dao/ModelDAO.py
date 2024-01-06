from abc import ABC, abstractmethod
from dao.connexionDAO import ConnexionBD

class modeleDAO(ABC):

    connect_object = ConnexionBD().getConnexion()

    ### CRUD

    # INSERT

    # SELECT

    @abstractmethod
    def findAll(self) -> list:
        pass

    # UPDATE

    # DELETE
