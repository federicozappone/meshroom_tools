import cv2
import numpy as np
import sys
import os
import concurrent.futures

from tqdm import tqdm
from datetime import datetime


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_frames.py video_file_name.mp4 [decimation]")
        exit(0)

    if len(sys.argv) == 3:
        decimation = int(sys.argv[2])
    else:
        decimation = 1

    print(f"Decimation: {decimation}")

    executor = concurrent.futures.ThreadPoolExecutor(max_workers=8)

    file_name = os.path.basename(sys.argv[1])

    print(f"File name: {file_name}")
    cap = cv2.VideoCapture(file_name)

    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if num_frames == 0:
        print("Invalid video file")
        exit(0)

    print(f"Numer of frames: {num_frames}")

    output_dir = f"extracted/frames_{datetime.now().strftime('%d-%m-%Y-%H.%M.%S')}"
    print(f"Output dir: {output_dir}")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in tqdm(range(num_frames)):
        ret, frame = cap.read()

        if i % decimation != 0:
            continue

        filename = f"{output_dir}/{i // decimation:06d}.png"
        executor.submit(cv2.imwrite, filename, frame)

    print("Done.")
