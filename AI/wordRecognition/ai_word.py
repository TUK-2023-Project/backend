from AI.wordRecognition.utils.dataset_utils import load_dataset, load_reference_signs , create_dataset
from AI.wordRecognition.sign_recorder import SignRecorder


# videos =  create_dataset() #비디오 기준으로 데이터셋 만들때 사용하는 함수 (주석을 풀어서 실행 후 다시 주석처리할것)  
# 데이터셋 정보를 가져옴



def detect_word(data):


    videos = load_dataset()
    reference_signs = load_reference_signs(videos)
    sign_recorder = SignRecorder(reference_signs)

    sign_detected = sign_recorder.process_results(data)
    return sign_detected
