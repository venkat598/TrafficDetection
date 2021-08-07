from imageai.Detection import ObjectDetection
import os
import red
import green

def main():
    
    count=0
    execution_source = os.getcwd()

    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_source , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_source , "F:\CS\TrafficDetection\saved_img.jpg"), output_image_path=os.path.join(execution_source , "imagenew.jpg"))

    for eachObject in detections:
        if(eachObject["name"]=="car" or eachObject["name"]=="bus" or eachObject["name"]=="truck" ):
            count+=1
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
    
    print(count)
    if(count>20):
        green.main()
    else:
        red.main()



















#Car detection code reference taken from github @OlafenwaMoses
#https://gist.github.com/OlafenwaMoses/5cf354473586415e3623442b8454532c
