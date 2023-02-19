import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd
import json

app = Flask(__name__)
## Load the model
voting_clf = pickle.load(open('voting_clf.pkl',"rb"))

@app.route('/')
def home():
    return render_template("Inventory_login.html")

@app.route('/LOGIN', methods = ['POST'])
def login():
    name1 = request.form['username']
    email = request.form['email']
    return render_template("attribute.html", name2 = name1)



# @app.route('/predict', methods = ['POST'])
# def predict():
#     data = request.json['data']  
    
#     # """
#     # request.json['data'] :
#     #  It indicates that  whenever we hit predict api then whatever input we will
#     #  put it into the json format which is capture inside the data key
#     # """
#     print(data)
#     print(list(data.values())) # data is in dictionary format and we have to provide it into list
#     print(np.array(list(data.values())).reshape(1,-1))
#     new_data = np.array(list(data.values())).reshape(1,-1)

#     predicted_value  = voting_clf.predict(new_data)[0]

#     if predicted_value == 0:
#         return jsonify({'Result':f"Your Product will not sell in next 6 months"})
    
#     else:
#         return jsonify({"Result":f'Your Product will sell in next 6 months'})

@app.route('/predict', methods = ['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    new_data = np.array(data).reshape(1,-1)

    
    predicted_value  = voting_clf.predict(new_data)[0]
    
    if predicted_value == 0:
        return render_template('thanku.html', prediction_text = "Your Product will not sell in next 6 months")
    
    else:
        return render_template('thanku.html', prediction_text = 'Your Product will sell in next 6 months')
    


if __name__ == "__main__":
    app.run(debug=True)

