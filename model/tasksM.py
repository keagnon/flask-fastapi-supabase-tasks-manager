from model.categoriesM import categories
from model.usersM import users

class tasks:
    def __init__(self):
        self.__task_id:int =None
        self.__title:str=""
        self.__description:str=""
        self.__completed:str=""
        self.__due_date:str=""
        self.__user_id:users=None
        self.__category_id:categories=None

    def SetTaskId(self,task_id:int)-> None:
        """
        This function helps to set id of task
        -----------------------------------------------------
        Params :
            task_id: id of the task
        Return :
            Nothing
        """
        self.__task_id=task_id

    def GetTaskId(self)-> None:
        """
        Get user id from task table
        -----------------------------------------------------
        Params :
            Nothing
        Return :
            Id of the tak from task table
        """
        return self.__task_id

    def SetTitleofTask(self,title:str)-> str:
        """
        Helps to set task title
        -----------------------------------------------------
        Params :
            title : title of the task
        Return :
            Nothing
        """
        self.__title=title

    def GetTitleofTask(self)-> str:
        """
        Used to get the title of the task from task table
        -----------------------------------------------------
        Params :
            Nothing
        Return :
            Title of the task
        """
        return self.__title

    def SetDescriptionofTask(self,description:str)-> str:
        """
        Used to set description of the task
        -----------------------------------------------------
        Params :
            description : description (detail) about task
        Return :
            Nothing
        """
        self.__description=description

    def GetDescriptionofTask(self)-> str:
        """
        Used to get task description from task table
        -----------------------------------------------------
        Params :
            Nothing
        Return :
            description : description of this task
        """
        return self.__description

    def SetDueDate(self,duedate:str)-> str:
        """
        Used to set due date link to this task
        -----------------------------------------------------
        Params :
            duedate: due date
        Return:
            nothing
        """
        self.__due_date=duedate

    def GetDueDate(self)-> str:
        """
        Used to get due date from table
        -----------------------------------------------------
        Params :
            Nothing
        Return :
            duedate : due date
        """
        return self.__due_date

    def SetTaskCompleted(self, completed)-> str:
        """
        Used to set the status of the task whether it is completed or not
        -----------------------------------------------------------------
        Params :
            completed : task status that we will set in task table
        Return :
            Nothing
        """
        self.__completed=completed

    def GetTaskCompleted(self)-> str:
        """
        Used to get the status of the task
        ------------------------------------------------------
        Params :
            Nothing
        Return :
            completed : status of the task
        """
        return self.__completed

    def SetUserId(self,userid:users)-> None:
        """
        Used to insert value in user table for attribut user_id
        ------------------------------------------------------------
        Params :
            userid : id of the user
        Return :
            Nothing
        """
        self.__user_id=userid

    def GetUserId(self) -> users:
        """
        Return object users associated to the user id
        -----------------------------------------------------------
        Params :
            Nothing
        Return :
            Object users link to that user id
        """
        return self.__user_id

    def SetCategoryId(self, categoryid: categories)-> None:
        """
        Used to insert value in category table for attribut category_id
        ---------------------------------------------------------------
        Params :
            categoryid : id of category
        Return :
            Nothing
        """
        self.__category_id=categoryid

    def GetCategoryId(self)-> categories:
        """
        Return Object category associated to tha category id
        -------------------------------------------------------------
        Params :
            Nothing
        Return :
            Object categories link to that category id
        """
        return self.__category_id