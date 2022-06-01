from flask import Flask, render_template, request, redirect, jsonify
import pickle
import pandas as pd
import numpy as np
# import requests

# Create an instance of Flask
app = Flask(__name__,template_folder='templates')

# Load the model
model = pickle.load(open('../model.pkl','rb'))

# Route to render index.html template using data 
@app.route("/index.html")
def index():
    return render_template("index.html")  
# Route to render index.html template using data 
@app.route("/model_build.html")
def model_build():
    return render_template("model_build.html")  

# Route to the form info
@app.route("/new_index.html")
def new_index():
    print("================")
    print("new_index")
    print("================")
    #profile_dict={'sex':['m','f']}
    return render_template("new_index.html")
# Route to the basic info
@app.route("/matchme", methods=["POST"])
def matchme():
    print("================")
    print("Match me")
    print("================")

    age=request.form["Age"]
    print(age)
    sex=request.form["Sex"]
    print(sex)
    income=request.form["Income"]
    print(income)
    status=request.form["Status"]
    print(status)
    diet=request.form["Diet"]
    print(diet)
    education=request.form["Education"]
    print(education)
    job=request.form["Job"]
    print(job)
    orientation=request.form["Orientation"]
    print(orientation)
    religion=request.form["Religion"]
    print(religion)
    height=request.form["Height"]
    print(height)
    ethnicity=request.form["Ethnicity"]
    print(ethnicity)
    drinks=request.form['Drinks']
    print(drinks)
    drugs=request.form['Drugs']
    print(drugs)
    smokes=request.form['Smokes']
    print(smokes)
    bodytype=request.form["Bodytype"]
    print(bodytype)

    #X_test=[age, body_type, diet, drinks, drugs, education, ethnicity, height, income, job, orientation, religion, sex, smokes,status]


    input_df = pd.DataFrame({'age':[age],'body_type': bodytype, 'diet':diet, 'drinks':drinks,
        'drugs':drugs,'education':education,'ethnicity':ethnicity,'height':[height], 'income': [income], 'job':job, 
        'orientation':orientation, 'religion':religion,'sex':sex,'smokes':smokes,'status':status})
    print(input_df)
   
    # Make prediction using model loaded from disk as per the data.
    prediction =model.predict(input_df)
    # Take the first value of prediction
    output = round(prediction[0], 2)
    print(output)
    #return jsonify(output)

    #Load Dataframe
    file_to_load = "../results_df.csv"

    # Read purchasing file and store into pandas data frame
    results_df= pd.read_csv(file_to_load)
    return_dict= results_df[results_df['class']== output].to_dict(orient="records")
    print(return_dict)
    return render_template("table.html", dict=return_dict) 

if __name__ == "__main__":
    app.run(debug=True)
