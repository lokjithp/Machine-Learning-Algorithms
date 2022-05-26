import pickle
from flask import Flask
from flask import request
from flask import jsonify
from json import JSONEncoder
import numpy as np

model_file='knn_iris.bin'

target_names=['setosa', 'versicolor', 'virginica']

with open(model_file,'rb') as f_in:
    my_model=pickle.load(f_in)


app=Flask('iris_model')

@app.route('/predict',methods=['POST'])
def predict():
    ival=request.get_json()
    #jsdata=setEncoder().encode(ival)

    target_value=np.array(['setosa', 'versicolor', 'virginica'])
    for key in ival:
        lst=ival[key]
    jsdata=np.array([lst])
    pred_val=my_model.predict(jsdata)

    result={
        'value':int(pred_val),
        'class':str(target_value[pred_val])
    }
    return jsonify(result)

if __name__=="__main__":    
    app.run(debug=True,host='0.0.0.0',port=9696)
