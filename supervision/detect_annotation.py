import cv2 as cv
import supervision as sv
from ultralytics import YOLO


'''
    Obtain Prediction
'''
model = YOLO("yolov8n.pt")
image = cv.imread('./sample1.jpg')
# cv.imshow('Colour Image Thumbnail', image)
results = model(image)[0]
'''
    Load Prediction into Supervision
'''
detections = sv.Detections.from_ultralytics(results)
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
