import pixellib
from pixellib.torchbackend.instance import instanceSegmentation
import cv2

capture = cv2.VideoCapture(0)

segment_video = instanceSegmentation()
segment_video.load_model("pointrend_resnet50.pkl", detection_speed = "rapid")
target_classes = segment_video.select_target_classes(person = True)
segment_video.process_camera(capture,  show_bboxes = True, frames_per_second= 5, segment_target_classes = target_classes, check_fps=True, show_frames= True,
frame_name= "frame", output_video_name="output_video.mp4")