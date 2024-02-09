from supervision.assets import download_assets, VideoAssets
import supervision as sv
from ultralytics import YOLO
import numpy as np


download_assets(VideoAssets.PEOPLE_WALKING)


model = YOLO("yolov8n.pt")
tracker = sv.ByteTrack()
box_annotator = sv.BoundingBoxAnnotator()
label_annotator = sv.LabelAnnotator()
trace_annotator = sv.TraceAnnotator()


def callback(frame: np.ndarray, _: int) -> np.ndarray:
    results = model(frame)[0]
    detections = sv.Detections.from_ultralytics(results)
    # Each detected object is assigned a unique tracker ID, to continuous following object's motion path across different frames
    detections = tracker.update_with_detections(detections)
    labels = [
        f"#{tracker_id} {results.names[class_id]}"
        for class_id, tracker_id
        in zip(detections.class_id, detections.tracker_id)
    ]
    annotated_frame = box_annotator.annotate(frame.copy(), detections=detections)
    annotated_frame = label_annotator.annotate(annotated_frame, detections=detections, labels=labels)
    return trace_annotator.annotate(annotated_frame, detections=detections)


sv.process_video(
    source_path="people-walking.mp4",
    target_path="result.mp4",
    callback=callback
)

