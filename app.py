from flask import Flask,render_template,request 
import math
import pickle 

#load files
with open ("poilynomia_features_model",'rb') as f:
    pfm = pickle.load(f)
with open ("model_picle",'rb') as f:
    model = pickle.load(f)



app = Flask(__name__) 

@app.route('/')
def home():
    return render_template("index.html") 



@app.route('/results', methods=['GET','POST'])
def predicting_value():
    if request.method == "POST":
        val1 = request.form["val"]
        val1 = int(val1)  
        trasformed_data = pfm.fit_transform([[val1]])
        res = model.predict(trasformed_data)
        res = math.ceil(float(res)) 
    #month and year calculation
    number_of_days = val1
    years = number_of_days // 365
    months = (number_of_days - years *365) // 30
    days = (number_of_days - years * 365 - months*30)
    ans = "In "+str(years)+"Years "+str(months)+"Months "+str(days)+"Days you will get "+str(res)+" subscribers"
    return render_template('index.html',result=ans) 

    
if __name__ == "__main__":
    app.run(debug=True)