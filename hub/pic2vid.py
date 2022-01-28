import os


def convert_jpg_to_mp4(jpg_path, output_name):
    os.system(r"ffmpeg -y -framerate 25 -i {}\%06d.jpg  "
              r"data/videos/{}.avi".format(jpg_path, output_name))
    return True


if __name__ == '__main__':
    jpg_path = r"data/videos/MOT17/test/MOT17-01-SDP/img1"
    output_name = r"MOT17-01-SDP"
    convert_jpg_to_mp4(jpg_path, output_name)