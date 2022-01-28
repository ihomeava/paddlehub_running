import paddlehub as hub

tracker = hub.Module(name="jde_darknet53")
# Read from a video file
tracker.tracking('data/videos/MOT17-01-SDP.avi',
                    output_dir='output',
                    visualization=True,
                    draw_threshold=0.5,
                    use_gpu=True)
# or read from a image stream
# with tracker.stream_mode(output_dir='image_stream_output', visualization=True, draw_threshold=0.5, use_gpu=True):
#    tracker.predict([images])