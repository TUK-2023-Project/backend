import os

import pandas as pd
from tqdm import tqdm

from AI.wordRecognition.models.sign_model import SignModel
from AI.wordRecognition.utils.landmark_utils import save_landmarks_from_video, load_array


def create_dataset():

    # 비디오 파일을 기준으로 데이터셋 생성
    videos = [
        file_name.replace(".mp4", "")
        for root, dirs, files in os.walk(os.path.join("data", "videos"))
        for file_name in files
        if file_name.endswith(".mp4")
    ]

    n = len(videos)
    if n > 0:
        print(f"\nExtracting landmarks from new videos: {n} videos detected\n")

        for idx in tqdm(range(n)):
            save_landmarks_from_video(videos[idx])

    return videos
    

def load_dataset():
    dataset = {}
    base_dir = os.path.join("AI/wordRecognition/data", "dataset")
    categories = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    
    for category in categories:
        cat_path = os.path.join(base_dir, category)
        dataset[category] = [
            file_name.replace(".pickle", "").replace("pose_", "")
            for root, dirs, files in os.walk(cat_path)
            for file_name in files
            if file_name.endswith(".pickle") and file_name.startswith("pose_")
        ]

    return dataset


def load_reference_signs(videos):
    reference_signs = {}
    for category, video_names in videos.items():
        signs = {"name": [], "sign_model": [], "distance": []}
        for video_name in video_names:
            sign_name = video_name.split("-")[0]
            path = os.path.join("AI/wordRecognition/data", "dataset", category, sign_name, video_name)

            left_hand_list = load_array(os.path.join(path, f"lh_{video_name}.pickle"))
            right_hand_list = load_array(os.path.join(path, f"rh_{video_name}.pickle"))

            signs["name"].append(sign_name)
            signs["sign_model"].append(SignModel(left_hand_list, right_hand_list))
            signs["distance"].append(0)

        reference_signs[category] = pd.DataFrame(signs, dtype=object)

    return reference_signs