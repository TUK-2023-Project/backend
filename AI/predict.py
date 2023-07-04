import cv2
import numpy as np
from AI.constants import gesture, gesture_word
from AI.wordRecognition.ai_word import detect_word

CATEGORY_CONSONANT = 1
CATEGORY_VOWEL = 2
CATEGORY_WORD = 3

knn_vowel = cv2.ml.KNearest_load('./AI/model/knn_model_vowel_v2.yml')
knn_consonant = cv2.ml.KNearest_load('./AI/model/knn_model_consonant_v2.yml')



def get_key_from_value(word):
    for key, value in gesture_word.items():
        if value[0] == word:
            return key
    return None

def predict_most_probable_gesture(dataList, model):
    freq = {key: 0 for key in gesture}
    for list in dataList:
        freq[predict_one_gesture(list,model)] += 1

    return max(freq, key=freq.get)

def predict_one_gesture(data,model):
    landmarks = data['landmarks']
    joint = np.zeros((21, 3))
    for i in range(len(landmarks)):
        joint[i] = landmarks[i][:]


    # 각 랜드마크의 좌표 계산
    v1 = joint[[0,1,2,3,0,5,6,7,0,9,10,11,0,13,14,15,0,17,18,19],:] # Parent joint
    v2 = joint[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],:] # Child joint
    v = v2 - v1 # [20,3]
    # 정규화
    v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]

    # Get angle using arcos of dot product
    angle = np.arccos(np.einsum('nt,nt->n',
        v[[0,1,2,4,5,6,8,9,10,12,13,14,16,17,18],:], 
        v[[1,2,3,5,6,7,9,10,11,13,14,15,17,18,19],:])) # [15,]

    angle = np.degrees(angle) # Convert radian to degree

  
    data = np.array([angle], dtype=np.float32)
    _, results, _, _ = model.findNearest(data, 3)
    idx = int(results[0][0])
    return idx


def run(data, category_num, targetWord):
    # if data == []:
    #     return None
    if category_num == CATEGORY_CONSONANT:
        knn = knn_consonant
    elif category_num == CATEGORY_VOWEL:
        knn = knn_vowel
    elif category_num >= CATEGORY_WORD:
   
        return gesture_word[detect_word(data,get_key_from_value(targetWord))][0] == targetWord

    else:
        raise ValueError("Invalid categoryNum: {}".format(category_num))

    return gesture[predict_most_probable_gesture(data, knn)] == targetWord