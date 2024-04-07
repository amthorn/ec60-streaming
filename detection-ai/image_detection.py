from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path , "yolov3.pt"))
# detector.setModelTypeAsRetinaNet()
# detector.setModelPath( os.path.join(execution_path , "retinanet_resnet50_fpn_coco-eeacb38b.pth"))
detector.loadModel()

detections = detector.detectObjectsFromImage(
    input_image=os.path.join(execution_path , "test.png"),
    output_image_path=os.path.join(execution_path , "output.png"),
    minimum_percentage_probability=50
)

for eachObject in detections:
    print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
    print("--------------------------------")

