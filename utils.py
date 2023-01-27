import numpy as np
import pickle
import json
import config1

class MedicalInsurance():
    def __init__(self, age, gender, bmi, children, smoker, region):
        
        self.age = age
        self.gender = gender
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = region
        return

    def __load_model(self):
        with open(config1.Linear_Reg_Model, 'rb') as f:
            self.model = pickle.load(f)
            print(self.model)

        with open(config1.JSON_File_Path, 'r') as f:
            self.project_data = json.load(f) 
            print(self.project_data)

    def get_predicted_price(self):
        self.__load_model()

        test_array = np.zeros(self.model.n_features_in_)
        test_array[0] = self.age
        test_array[1] = self.project_data['Gender'][self.gender]
        test_array[2] = self.bmi
        test_array[0] = self.children
        test_array[0] = self.project_data['Smoker'][self.smoker]
        region = 'region_' + self.region
        index = self.project_data['Column Name'].index(region)

        test_array[index] = 1

        predicted_charges = np.around(self.model.predict([test_array])[0],3)
        return predicted_charges
