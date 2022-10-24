from django.apps import AppConfig
from django.conf import settings
from tensorflow.keras.models import load_model
import pickle, os
    
class Predictor(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'disease_prediction'
    path = os.path.join(settings.BASE_DIR, 'disease_prediction')
    model = load_model(settings.MODEL)
    encoder = pickle.load(open(settings.ENCODER, 'rb'))
    
    def prediction(self, data):
        encoded = self.model.predict(data)
        output = self.encoder.inverse_transform(encoded)
        return (output,encoded)
    
