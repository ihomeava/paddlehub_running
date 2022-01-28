import paddlehub as hub
import cv2

face_landmark = hub.Module(name="face_landmark_localization")

# Replace face detection module to speed up predictions but reduce performance
# face_landmark.set_face_detector_module(hub.Module(name="ultra_light_fast_generic_face_detector_1mb_320"))

result = face_landmark.keypoint_detection(images=[cv2.imread('data/images/20220128161252.jpg')],
                                            batch_size=1,
                                            use_gpu=True,
                                            output_dir='output',
                                            visualization=True)
# or
# result = face_landmark.keypoint_detection(paths=['/PATH/TO/IMAGE'])