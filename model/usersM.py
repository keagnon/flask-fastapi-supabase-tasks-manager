class users:
    def __init__(self):
      self.__user_id:int =None
      self.__username:str=""
      self.__email:str=""
      self.__password:str=""

    def SetUserId(self,user_id:int) -> None:
       """
        This method helps to set the value of the user id in attribut user_id
        ---------------------------------------------------------------------
        Params:
            user_id: User id from table
        Returns:
            Nothing
       """
       self.__user_id=user_id

    def GetUserId(self)-> None:
       """
        Get the value of user id inside the table
        ---------------------------------------------------------------------
        Return:
            id of the user
       """
       return self.__user_id

    def SetUsername(self,username:str) -> str:
       """
        It is used to set the value of the username link to the attribut username
        -------------------------------------------------------------------------
        Params:
            username: User name that we will set in the table
        Returns:
            Nothing
       """
       self.__username=username

    def GetUsername(self) -> str:
       """
        Get the username from table
        -------------------------------------------------------------------------
        Params:
            Nothing
        Reurn:
            name of the user
       """
       return self.__username

    def SetUserEmail(self,email:str)-> str:
       """
        Goal : Set email of the user
        -------------------------------------------------------------------------
        Params:
            email: User email that we will ste in the table
        Return:
            Nothing
       """
       self.__email=email

    def GetUserEmail(self)-> str:
       """
       Goal: Get email of the user from user table
       --------------------------------------------------------------------------
       Params :
            Nothing
       Return :
            Email of the user
       """
       return self.__email

    def SetUserPassword(self,password:str)-> str:
       """
        This function permit to set the password of the user
        -------------------------------------------------------------------------
        Params :
            password : password of the user
        Return :
            Nothing
       """
       self.__password=password

    def GetUserPassword(self)-> str:
       """
       This function permit to get the user password from user table
       --------------------------------------------------------------------------
        Params :
            Nothing
        Return :
            Password of the user from user table
       """
       return self.__password