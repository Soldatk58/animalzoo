from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pickle

# Загружаем модель
model = pickle.load(open('model/animal_predictor_model.pkl', 'rb'))

# Создаем экземпляр FastAPI
app = FastAPI()

class Input(BaseModel):
    hair:int
    feathers:int
    eggs:int
    milk:int
    airborne:int
    aquatic:int
    predator:int
    toothed:int
    backbone:int
    breathes:int
    venomous:int
    fins:int
    legs:int
    tail:int
    domestic:int
    catsize:int

@app.get('/')
def read_root():
    return {'msg':'Animal Predictor'}

@app.post('/predict')
def predict_type(input:Input):
    data = input.dict()
    data_in = [[data['hair'], data['feathers'], data['eggs'], data['milk'], data['airborne'],
    data['aquatic'], data['predator'], data['toothed'], data['backbone'], data['breathes'],
    data['venomous'], data['fins'], data['legs'], data['tail'], data['domestic'], data['catsize']]]

    prediction = model.predict(data_in)

    return {
        'prediction': prediction[0]
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)