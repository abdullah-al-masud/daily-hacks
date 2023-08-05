import cv2
import numpy as np
import os
import yt_dlp
import pandas as pd


def video_download(file_path):
    """
    must be a csv or txt file
    Column names will be {url, height}
    
    txt or csv format
    
    url,height
    svjnsdvljsndvlsdnvlsd,1080
    """

    data = pd.read_csv(file_path)
    for i in range(data.shape[0]):
        if not pd.isnull(data['height'].iloc[i]):
            opts = {'format': 'bv*[height=%d]+ba'%data['height'].iloc[i]}
        else:
            opts = {}
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download(data['url'].iloc[i])


def video_cutter(path, outdir, segments, segment_type):
    """
    segment_type can be {'segment', 'frame', 'time'}. Time will be in seconds
    segments must be {int, list, list} respectively for these above segment_types
    if segments is int, it will indicate how many pieces will be made out of the whole video 
    if segments is list and indicating frame numbers, they will be used as starting frame number of each video slice
    """

    videoname = '.'.join(os.path.split(path)[-1].split('.')[:-1])
    capture = cv2.VideoCapture(path)
    total_frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(capture.get(cv2.CAP_PROP_FPS))
    if segment_type == 'segment' and isinstance(segments, int):
        segments = np.linspace(0, total_frames, segments).tolist()
    elif segment_type == 'frame' and isinstance(segments, list):
        pass
    elif segment_type == 'time' and isinstance(segments, list):
        segments = [int(fps * x) for x in segments]
    segments = [int(i) for i in segments]

    i = 0
    frame_count = 0
    store = None
    total_segs = len(segments)
    while True:
        print('\r%08d/%08d...   '%(frame_count+1, total_frames), end='', flush=True)
        ret, frame = capture.read()
        if not ret:
            break
        if i < total_segs:
            if frame_count == segments[i]:
                if frame_count == 0:
                    os.makedirs(outdir, exist_ok=True)
                    size = (frame.shape[1], frame.shape[0])
                end_frame = segments[i+1] if i+1 < total_segs else total_frames
                end_frame -= 1
                if store is not None:
                    store.release()
                store = cv2.VideoWriter(os.path.join(outdir, '%s_%08d_to_%08d.mp4'%(videoname, segments[i], end_frame)),
                                        cv2.VideoWriter_fourcc(*'mp4v'),
                                        fps,
                                        size
                                    )
                i += 1
        store.write(frame)
        frame_count += 1
    print('complete!!')
    capture.release()
    store.release()


