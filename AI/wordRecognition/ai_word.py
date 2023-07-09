from AI.wordRecognition.utils.dataset_utils import load_dataset, load_reference_signs , create_dataset
from AI.wordRecognition.sign_recorder import SignRecorder
from AI.constants import gesture_word
import copy


# videos =  create_dataset() #비디오 기준으로 데이터셋 만들때 사용하는 함수 (주석을 풀어서 실행 후 다시 주석처리할것)  
# 데이터셋 정보를 가져옴

videos = load_dataset()
reference_signs = load_reference_signs(videos)

def detect_word(data , targetWord):

    copyReference = copy.copy(reference_signs[gesture_word[targetWord][1]])
    sign_recorder = SignRecorder(copyReference)

    sign_detected = sign_recorder.process_results(data)
    return sign_detected
