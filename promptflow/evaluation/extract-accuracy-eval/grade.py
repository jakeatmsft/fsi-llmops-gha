from promptflow import tool
import json


@tool
def grade(groundtruth: str, prediction: str):
    # groundtruth and prediction are both json objects in string format, try to convert them to json objects and compare the number of items in the complaint array
    try:
        groundtruth = json.loads(groundtruth)
        prediction = json.loads(prediction)
        if len(groundtruth['complaints']) == len(prediction['complaints']):
            return "Correct"
        else:
            return "Incorrect"
    except:
        return "Incorrect"
    


