import cv2 as cv
import supervision as sv
from ultralytics import YOLO
import numpy as np
'''
    Obtain Prediction
'''
model = YOLO("yolov8n.pt")
image = cv.imread('./sample1.jpg')
results = model(image)[0]
'''
    Load Prediction into Supervision
'''
selected_classes = [66, 0]
height, width, channels = image.shape
image_area = height * width
# zone = sv.PolygonZone(...)


detections = sv.Detections.from_ultralytics(results)
detections = detections[np.isin(detections.class_id, selected_classes)] # By selected classes
detections = detections[detections.confidence > 0.5] # By confidence
detections = detections[detections.area > 1000] # By area of objects
detections = detections[(detections.area / image_area) < 0.8] # By relative of area
w = detections.xyxy[:, 2] - detections.xyxy[:, 0]
h = detections.xyxy[:, 3] - detections.xyxy[:, 1]
detections =  detections[(w > 200) & (h > 200)] # By box of dimensions
# mask = zone.trigger(detections=detections)
# detections = detections[mask]# By Polygon Zone
detections = detections[(detections.confidence > 0.7) & detections.area > 300] # By mixed conditions


'''
    Annotation
'''
bounding_box_annotator = sv.BoundingBoxAnnotator()
label_annotator = sv.LabelAnnotator()
labels = [
    model.model.names[class_id]
    for class_id
    in detections.class_id
]


annotated_image = bounding_box_annotator.annotate(
    scene=image, detections=detections)
annotated_image = label_annotator.annotate(
    scene=annotated_image, detections=detections, labels=labels)


sv.plot_image(annotated_image)


cv.waitKey(0)          
cv.destroyAllWindows()
