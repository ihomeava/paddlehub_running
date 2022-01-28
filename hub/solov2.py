import cv2
import paddlehub as hub

img = cv2.imread('data/human/WechatIMG170.jpeg')
model = hub.Module(name='solov2', use_gpu=True)
output = model.predict(image=img,
                        threshold=0.5,
                        visualization=True,
                        save_dir='output')