import cv2
import numpy as np
import sys
import os
import concurrent.futures

from tqdm import tqdm
from datetime import datetime


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_frames.py video_file_name.mp4")
        exit(0)

    executor = concurrent.futures.ThreadPoolExecutor(max_workers=8)

    print(f"File name: {sys.argv[1]}")
    cap = cv2.VideoCapture(sys.argv[1])

    file_name = os.path.basename(sys.argv[1])

    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if num_frames == 0:
        print("Invalid video file")
        exit(0)

    print(f"Numer of frames: {num_frames}")

    output_dir = f"extracted/frames_{datetime.now().strftime('%d-%m-%Y-%H.%M.%S')}"
    print(f"Output dir: {output_dir}")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    skips = 0
    index = 0

    for i in tqdm(range(num_frames)):
        ret, frame = cap.read()

        skips += 1

        if skips == 5:
            skips = 0

        if skips != 1:
            continue

        filename = f"{output_dir}/{index:06d}.png"
        executor.submit(cv2.imwrite, filename, frame)

        index += 1

    print("Done.")
