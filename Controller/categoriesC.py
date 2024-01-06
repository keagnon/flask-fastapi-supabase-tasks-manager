from Dao.categoriesDAO import *
from model import categoriesM

class categories:

    @staticmethod
    def displayCategories():
        """
            Goal : Visualize all categories avalaible
            Params : Nothing
            Return: All categories
        """
        try:
            CatDAO=categoriesDAO()
            c=CatDAO.findAll()
            return c

        except Exception as e :
            print(f"Erreur_categories.displayCategories() ::: {e}")