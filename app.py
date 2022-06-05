
# URL = localhost:5000



from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

#from sklearn.metrics import ConfusionMatrixDisplay
# from imblearn.over_sampling import RandomOverSampler
# from sklearn.preprocessing import OrdinalEncoder 
# from sklearn.preprocessing import minmax_scale

import pandas as pd 
import numpy as np

from sklearn.preprocessing import OneHotEncoder, LabelEncoder

import  pickle

#with open('model_adaboost.pkl','rb') as fin:
 #   model = pickle.load(fin)

model = pickle.load(open('model_adabo.pkl','rb'))
#model = pickle.load(open('model_neural.pkl','rb'))

print(type(model))


featuresL=['BMI','Smoking','AlcoholDrinking','Stroke','PhysicalHealth','MentalHealth','DiffWalking','Sex','AgeCategory','Race','Diabetic','PhysicalActivity','GenHealth','SleepTime','Asthma','KidneyDisease','SkinCancer']

#tell app where database is located
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' 
#database initalized with app settings
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)   
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    predictionn =  db.Column(db.Integer, default=0)  

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content, predictionn=model.predict(pd.DataFrame([(task_content.split(","))],columns=featuresL )))
        #new_task = Todo(content=task_content, predictionn= model.predict(np.array(task_content.split(",")).reshape(1, -1))) 

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
            
    else:
        tasks = Todo.query.order_by(Todo.date_created).all() 
        return render_template('index.html', tasks=tasks)   

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'Failed to delete that task'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'task failed to update line 67'
    else:
        return render_template('update.html', task=task)

if __name__ == "__main__":
    app.run(debug=True)

