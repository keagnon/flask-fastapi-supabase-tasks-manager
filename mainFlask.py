import os
from flask import Flask, render_template, request
from flask_cors import CORS #gestion des accès au w.s.
from datetime import datetime
from functools import wraps
#from controller.categoriesC import categories
from controller import categoriesC
from model.categoriesM import categories

app = Flask(__name__)

CORS(app, ressources={fr"api/tasksmanager/*":{"origins":"*"}})

#categories routes
@app.route('/api/tasksmanager/categories',methods=['GET'])
def getCategories():
    catC=categoriesC.categories.displayCategories()
    print(list)

    List_categories=[]

    if type(catC)==list:
        for c in catC:
            category={
                "category_id":c.GetCategoryId(),
                "category_name":c.GetCategoryName()
            }

            List_categories.append(category)
        return {'response': List_categories}

    return {'response':"categories not found"}

if __name__=='__main__':
    #Run flask with the following defaults value
    app.run(debug=True,port=3000, host='0.0.0.0', )