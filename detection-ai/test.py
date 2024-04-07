from imageai.Detection import VideoObjectDetection
import os
import cv2

execution_path = os.getcwd()

def isCat(second_number, output_arrays, count_arrays, average_output_count):
    print("SECOND : ", second_number)
    print("Array for the outputs of each frame ", output_arrays)
    print("Array for output count for unique objects in each frame : ", count_arrays)
    print("Output average count for unique objects in the last second: ", average_output_count)
    print("------------END OF A SECOND --------------")

detector = VideoObjectDetection()
# detector.setModelTypeAsTinyYOLOv3()
# detector.setModelPath( os.path.join(execution_path , "tiny-yolov3.pt"))
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "yolov3.pt"))
# detector.setModelTypeAsRetinaNet()
# detector.setModelPath( os.path.join(execution_path , "retinanet_resnet50_fpn_coco-eeacb38b.pth"))
detector.loadModel()

video_path = detector.detectObjectsFromVideo(
    camera_input=cv2.VideoCapture('http://localhost:8088/hls/Basement_Cam.m3u8'),
    # input_file_path=os.path.join(execution_path, "test.mp4"),
    # output_file_path=os.path.join(execution_path, "stuff_detected"),
    custom_objects=detector.CustomObjects(person=True, cat=True),
    per_second_function=isCat,
    frames_per_second=1,
    save_detected_video=False,
    frame_detection_interval=2,
)

print(video_path)