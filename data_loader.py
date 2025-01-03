import tensorflow as tf
import dill as pk
import os

curr_path = os.path.dirname(__file__)

class ModelLoader:
    _instance = None
    
    @staticmethod
    def get_instance():
        if ModelLoader._instance is None:
            ModelLoader._instance = ModelLoader()
        return ModelLoader._instance
    
    def __init__(self) -> None:
        if ModelLoader._instance is not None:
            raise Exception('This is a singleton')
        
        
        self.model = tf.keras.models.load_model(os.path.join(curr_path, 'model', 'lstm_model_new_.keras'))
        
    def get_data(self):
        return self.model
    
    
class TokenizerLoader:
    _instance = None
    
    @staticmethod
    def get_instance():
        if TokenizerLoader._instance is None:
            TokenizerLoader._instance = TokenizerLoader()
        return TokenizerLoader._instance
    
    def __init__(self) -> None:
        if TokenizerLoader._instance is not None:
            raise Exception('This is a singleton')
        with open(os.path.join(curr_path, 'data', 'tokenizer.pkl'), 'rb') as f:
            self.tokenizer = pk.load(f)
        
    def get_data(self):
        return self.tokenizer