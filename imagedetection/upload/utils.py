#Import 
from imageai.Detection import ObjectDetection
import os
from .models import Upload


def detectImg(img):

	execution_path = os.getcwd()

	detector = ObjectDetection()
	detector.setModelTypeAsYOLOv3()
	detector.setModelPath(os.path.join(execution_path , "yolo.h5"))
	detector.loadModel()
	detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path,"media/"+img),
		output_image_path = os.path.join(execution_path,"media/detected_"+img))


	return detections