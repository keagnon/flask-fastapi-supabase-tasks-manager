class categories:
    def __init__(self) :
        self.__category_id:int =None
        self.__category_name:str=""

    def SetCategoriesId(self,category_id:int) -> None:
        """
        This method is used to insert value in attribut category_id
        -------------------------------------------------------------
        Params:
            category_id: Id of category table
        Return:
            Nothing
        """
        self.__category_id=category_id

    def GetCategoryId(self)-> None:
        """
        This method is used to return the category id
        -------------------------------------------------------------
        Return:
            Category id
        """
        return self.__category_id

    def SetCategoryName(self,category_name:str) -> str:
        """
        This method is used to insert category name in attribut name
        -------------------------------------------------------------
        Params:
            category_name : Reference of the category
        Return:
            Nothing
        """
        self.__category_name=category_name

    def GetCategoryName(self) -> str:
        """
        This method is used to return the category name
        -------------------------------------------------------------
        Return:
            category_name
        """
        return self.__category_name


