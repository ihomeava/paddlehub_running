import cv2
import paddlehub as hub

# 模型加载
# use_gpu：是否使用GPU进行预测
model = hub.Module(name='animegan_v2_hayao_99', use_gpu=True)

# 模型预测
result = model.style_transfer(images=[cv2.imread('data/human/WechatIMG170.jpeg')],
                                output_dir='output',
                                visualization=True)

# or
# result = model.style_transfer(paths=['/PATH/TO/IMAGE'])s