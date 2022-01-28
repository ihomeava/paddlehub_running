import paddlehub as hub
import cv2

human_seg = hub.Module(name="deeplabv3p_xception65_humanseg")
result = human_seg.segmentation(images=[cv2.imread('data/images/20220128161252.jpg')],
                                batch_size=1,
                                use_gpu=True,
                                visualization=True,
                                output_dir='output')
# or
# result = human_seg.segmentation(paths=['/PATH/TO/IMAGE'])