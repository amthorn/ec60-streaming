FROM python:3.10

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install imageai

COPY tiny-yolov3.pt tiny-yolov3.pt
COPY yolov3.pt yolov3.pt
COPY retinanet_resnet50_fpn_coco-eeacb38b.pth retinanet_resnet50_fpn_coco-eeacb38b.pth
COPY test.mp4 test.mp4
COPY test.png test.png

COPY image_detection.py image_detection.py
COPY test.py test.py

ENTRYPOINT ["python", "test.py"]