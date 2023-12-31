from dao import ModelDAO
from model.categoriesM import categories

class categoriesDAO(ModelDAO.modeleDAO):
    def __init__(self):
        """
        Initilize categoriesDAO object by establising connexion to the data base
        """
        params =ModelDAO.modeleDAO.connect_object
        self.cur=params.cursor()

    def findAll(self) -> list[categories]:
        """
            Goal : list all recording inside categories table
            -----------------------------------------------------------
            params :
                keyfound --> Key used for search
            Return :
                List of categories object
        """
        try:
            query='''SELECT * FROM categories;'''
            self.cur.execute(query)
            res=self.cur.fetchall()
            list_categories=[]

            if len(res)>0:
                for r in res :
                    cat=categories()
                    cat.SetCategoriesId(r[0]) # Utilisez l'indice r[0] pour accéder au premier élément de la ligne
                    cat.SetCategoryName(r[1]) # Utilisez l'indice r[1] pour accéder au deuxième élément de la ligne
                    list_categories.append(cat)
                return list_categories
            else:
                return None

        except Exception as e:
            print(f"Erreur_categoriesDAO.findAll ::: {e}")
        finally :
            self.cur.close()

