from joblib import load
import numpy as np

class Modelo():
    def __init__(self):
        self.model = load('backend/modelo_entrenado.joblib')

    def consultar(self, data):
        data = np.array(data)
        data = data.astype(int)
        model_response = self.model.predict_proba([data])[:,1]

        return model_response