import paddlehub as hub
import cv2

face_detector = hub.Module(name="ultra_light_fast_generic_face_detector_1mb_640")
result = face_detector.face_detection(images=[cv2.imread('data/images/20220128161252.jpg')],
                                        batch_size=1,
                                        use_gpu=True,
                                        visualization=True,
                                        output_dir='output',
                                        confs_threshold=0.5)
# or
# result = face_detector.face_detection((paths=['/PATH/TO/IMAGE'])