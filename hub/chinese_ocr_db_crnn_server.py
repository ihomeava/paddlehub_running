import paddlehub as hub
import cv2

ocr = hub.Module(name="chinese_ocr_db_crnn_server")
result = ocr.recognize_text(images=[cv2.imread('data/images/a7e0bd92393ba155da10c5b19e9924f3.jpeg')],
                            use_gpu=True,
                            output_dir='output',
                            visualization=True,
                            box_thresh=0.5,
                            text_thresh=0.5)

# or
# result = ocr.recognize_text(paths=['/PATH/TO/IMAGE'])