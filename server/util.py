import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_location_names():
    return __locations
def get_estimated_price(location, sqft, bath, bhk):
    print("Get Estimated Prices Called")
    try:
        loc_index =  __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if (loc_index >= 0):
        x[loc_index] = 1
    return round(__model.predict([x])[0], 2) # 2 here will give rhe price for 2 decimal places

def load_saved_artefacts():
    print("loading the saved artefacts... start")
    global __data_columns
    global __model
    global __locations

    with open("./artefacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open("./artefacts/Bengaluru_houses_price_prediction_model.pickle", 'rb') as f:
        __model = pickle.load(f)
    print("loading saved artefacts...done")


# if __name__ == '__main__':
#     load_saved_artefacts()
#     print(get_location_names())
#     print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
#     print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
#     print(get_estimated_price('Kalhali', 1000, 2, 2)) # other location
#     print(get_estimated_price('Ejipura', 1000, 3, 3)) # other location
#
