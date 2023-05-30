from utils.dataset_utils import load_dataset, load_reference_signs , create_dataset
from sign_recorder import SignRecorder



def detect_word(data):


    # videos =  create_dataset() #비디오 기준으로 데이터셋 만들때 사용하는 함수 (주석을 풀어서 실행 후 다시 주석처리할것)
     

    # 데이터셋 정보를 가져옴 
    videos = load_dataset()

    # Create a DataFrame of reference signs (name: str, model: SignModel, distance: int)
    reference_signs = load_reference_signs(videos)

    # Object that stores mediapipe results and computes sign similarities
    sign_recorder = SignRecorder(reference_signs)


    parsed_front_data = {
        "left" : [[0.7237339615821838, 0.8497132658958435, 4.4172091406835534e-07, 0.6824007630348206, 0.8145554065704346, -0.016210610046982765, 0.6565616130828857, 0.7370223999023438, -0.02620561607182026, 0.6585904359817505, 0.664800226688385, -0.03863553702831268, 0.6705167889595032, 0.6071651577949524, -0.050209060311317444, 0.6455270648002625, 0.6018590927124023, -0.010662962682545185, 0.6153036952018738, 0.5174403786659241, -0.027540871873497963, 0.5987749099731445, 0.4621528685092926, -0.0380958691239357, 0.5860664248466492, 0.41467925906181335, -0.045292966067790985, 0.6801928877830505, 0.5890337228775024, -0.019383899867534637, 0.6730836033821106, 0.46362048387527466, -0.03987377882003784, 0.6655659079551697, 0.3883482813835144, -0.054251667112112045, 0.6612192988395691, 0.32908234000205994, -0.06169426813721657, 0.7138404250144958, 0.6112839579582214, -0.03046857938170433, 0.7061606645584106, 0.5283010005950928, -0.06278789043426514, 0.6956537961959839, 0.6015628576278687, -0.06768371164798737, 0.6921303868293762, 0.6590455770492554, -0.062263231724500656, 0.7452576756477356, 0.6537164449691772, -0.04227346554398537, 0.729937732219696, 0.6167311072349548, -0.06940988451242447, 0.7182468175888062, 0.6752480864524841, -0.06883666664361954, 0.714868426322937, 0.7233352661132812, -0.06213619187474251], [0.7236599326133728, 0.847048282623291, 4.593084383941459e-07, 0.682803213596344, 0.812738835811615, -0.017189720645546913, 0.6567263007164001, 0.7397803068161011, -0.02803914062678814, 0.657784104347229, 0.6695371866226196, -0.041125185787677765, 0.6678146123886108, 0.610668420791626, -0.053058549761772156, 0.6443284153938293, 0.6004756689071655, -0.011604645289480686, 0.6149349808692932, 0.5163729190826416, -0.0285848006606102, 0.5989574193954468, 0.461309552192688, -0.039080094546079636, 0.5866203904151917, 0.41414597630500793, -0.04602057859301567, 0.679247260093689, 0.5871784090995789, -0.019839487969875336, 0.6726073026657104, 0.4626499116420746, -0.040048182010650635, 0.6654469966888428, 0.38809365034103394, -0.05392558500170708, 0.661018431186676, 0.3292613625526428, -0.06094861403107643, 0.7130022644996643, 0.6090773940086365, -0.03057408332824707, 0.7058142423629761, 0.5312923789024353, -0.06213798001408577, 0.695660412311554, 0.6043347120285034, -0.06641680002212524, 0.6920374035835266, 0.6609237194061279, -0.060604486614465714, 0.7440446615219116, 0.6514291167259216, -0.042188309133052826, 0.7301341891288757, 0.6138159036636353, -0.06760678440332413, 0.7189984321594238, 0.6702952980995178, -0.06605306267738342, 0.715760350227356, 0.7167580127716064, -0.058872926980257034], [0.723004162311554, 0.8469727039337158, 4.5383549718280847e-07, 0.6823686957359314, 0.8128291368484497, -0.01691843755543232, 0.6569032669067383, 0.739646852016449, -0.027818066999316216, 0.6584276556968689, 0.6695270538330078, -0.0409860834479332, 0.6676225662231445, 0.6115372776985168, -0.05314629152417183, 0.6446422338485718, 0.6021558046340942, -0.012453695759177208, 0.6149516105651855, 0.5179146528244019, -0.029698388651013374, 0.5986732244491577, 0.4630547761917114, -0.04028636962175369, 0.5861800909042358, 0.4157763421535492, -0.04732868820428848, 0.6792464256286621, 0.5888803005218506, -0.02077343873679638, 0.6724126935005188, 0.4633972644805908, -0.04116469621658325, 0.6651234030723572, 0.3883812427520752, -0.055000174790620804, 0.6608063578605652, 0.32915201783180237, -0.06204375997185707, 0.7129302024841309, 0.6105323433876038, -0.03147866949439049, 0.7047638893127441, 0.5311749577522278, -0.06325779110193253, 0.6944117546081543, 0.6047140955924988, -0.06763556599617004, 0.6910640597343445, 0.661859393119812, -0.06192830950021744, 0.7443737983703613, 0.6523323059082031, -0.04301372542977333, 0.7289563417434692, 0.6168420910835266, -0.06915143877267838, 0.7172250747680664, 0.6740070581436157, -0.06810645014047623, 0.7137615084648132, 0.7206435203552246, -0.061206310987472534], [0.7232080101966858, 0.8471037149429321, 4.570647149648721e-07, 0.6821331977844238, 0.8125115633010864, -0.016952484846115112, 0.6562807559967041, 0.738866925239563, -0.02780112251639366, 0.6577473282814026, 0.6685487031936646, -0.04085814207792282, 0.667175829410553, 0.6093937754631042, -0.0527489148080349, 0.6441320776939392, 0.6005398631095886, -0.01192699559032917, 0.6140629649162292, 0.5164145827293396, -0.028843563050031662, 0.597350001335144, 0.4618262052536011, -0.039353784173727036, 0.5845091938972473, 0.41475996375083923, -0.04650069400668144, 0.6787043213844299, 0.587813675403595, -0.020182069391012192, 0.6719730496406555, 0.4636320173740387, -0.040477994829416275, 0.6649244427680969, 0.3891032934188843, -0.054519835859537125, 0.6609782576560974, 0.3299159109592438, -0.061840880662202835, 0.7123211026191711, 0.6102954745292664, -0.03084244392812252, 0.7046603560447693, 0.5304760336875916, -0.06244692578911781, 0.6940523982048035, 0.6041232943534851, -0.06681118160486221, 0.6905077695846558, 0.6615068316459656, -0.06124558672308922, 0.7437323331832886, 0.6525421738624573, -0.04234977066516876, 0.7284671664237976, 0.6172051429748535, -0.06861397624015808, 0.7163008451461792, 0.6741721630096436, -0.06778419017791748, 0.7125025987625122, 0.7208893895149231, -0.06106666475534439], [0.7225584387779236, 0.8471834659576416, 4.5806319803887163e-07, 0.6815620064735413, 0.8128465414047241, -0.017082074657082558, 0.6562831401824951, 0.7404870986938477, -0.028425423428416252, 0.657294511795044, 0.6710403561592102, -0.042066942900419235, 0.666638970375061, 0.6124078631401062, -0.05468754842877388, 0.6448003649711609, 0.6026839017868042, -0.012883830815553665, 0.6151084303855896, 0.517815113067627, -0.030402962118387222, 0.5985437035560608, 0.4629612863063812, -0.0411616750061512, 0.5857115387916565, 0.4153285622596741, -0.048347875475883484, 0.6792432069778442, 0.5895501375198364, -0.021477853879332542, 0.6722103357315063, 0.46388089656829834, -0.0422053337097168, 0.6648858785629272, 0.38898104429244995, -0.05615061894059181, 0.6606441736221313, 0.3291892409324646, -0.06327779591083527, 0.7127612829208374, 0.6118534803390503, -0.032466333359479904, 0.7047377228736877, 0.5310670733451843, -0.0647364929318428, 0.6948288679122925, 0.6057051420211792, -0.0687849149107933, 0.691926896572113, 0.6632322669029236, -0.06273974478244781, 0.7441092729568481, 0.6545228958129883, -0.044303201138973236, 0.7292343378067017, 0.6171474456787109, -0.07098641991615295, 0.7176762223243713, 0.6747602820396423, -0.06977120786905289, 0.7143669128417969, 0.7220607399940491, -0.06262373924255371]],
        "right" : [[0.7237339615821838, 0.8497132658958435, 4.4172091406835534e-07, 0.6824007630348206, 0.8145554065704346, -0.016210610046982765, 0.6565616130828857, 0.7370223999023438, -0.02620561607182026, 0.6585904359817505, 0.664800226688385, -0.03863553702831268, 0.6705167889595032, 0.6071651577949524, -0.050209060311317444, 0.6455270648002625, 0.6018590927124023, -0.010662962682545185, 0.6153036952018738, 0.5174403786659241, -0.027540871873497963, 0.5987749099731445, 0.4621528685092926, -0.0380958691239357, 0.5860664248466492, 0.41467925906181335, -0.045292966067790985, 0.6801928877830505, 0.5890337228775024, -0.019383899867534637, 0.6730836033821106, 0.46362048387527466, -0.03987377882003784, 0.6655659079551697, 0.3883482813835144, -0.054251667112112045, 0.6612192988395691, 0.32908234000205994, -0.06169426813721657, 0.7138404250144958, 0.6112839579582214, -0.03046857938170433, 0.7061606645584106, 0.5283010005950928, -0.06278789043426514, 0.6956537961959839, 0.6015628576278687, -0.06768371164798737, 0.6921303868293762, 0.6590455770492554, -0.062263231724500656, 0.7452576756477356, 0.6537164449691772, -0.04227346554398537, 0.729937732219696, 0.6167311072349548, -0.06940988451242447, 0.7182468175888062, 0.6752480864524841, -0.06883666664361954, 0.714868426322937, 0.7233352661132812, -0.06213619187474251], [0.7236599326133728, 0.847048282623291, 4.593084383941459e-07, 0.682803213596344, 0.812738835811615, -0.017189720645546913, 0.6567263007164001, 0.7397803068161011, -0.02803914062678814, 0.657784104347229, 0.6695371866226196, -0.041125185787677765, 0.6678146123886108, 0.610668420791626, -0.053058549761772156, 0.6443284153938293, 0.6004756689071655, -0.011604645289480686, 0.6149349808692932, 0.5163729190826416, -0.0285848006606102, 0.5989574193954468, 0.461309552192688, -0.039080094546079636, 0.5866203904151917, 0.41414597630500793, -0.04602057859301567, 0.679247260093689, 0.5871784090995789, -0.019839487969875336, 0.6726073026657104, 0.4626499116420746, -0.040048182010650635, 0.6654469966888428, 0.38809365034103394, -0.05392558500170708, 0.661018431186676, 0.3292613625526428, -0.06094861403107643, 0.7130022644996643, 0.6090773940086365, -0.03057408332824707, 0.7058142423629761, 0.5312923789024353, -0.06213798001408577, 0.695660412311554, 0.6043347120285034, -0.06641680002212524, 0.6920374035835266, 0.6609237194061279, -0.060604486614465714, 0.7440446615219116, 0.6514291167259216, -0.042188309133052826, 0.7301341891288757, 0.6138159036636353, -0.06760678440332413, 0.7189984321594238, 0.6702952980995178, -0.06605306267738342, 0.715760350227356, 0.7167580127716064, -0.058872926980257034], [0.723004162311554, 0.8469727039337158, 4.5383549718280847e-07, 0.6823686957359314, 0.8128291368484497, -0.01691843755543232, 0.6569032669067383, 0.739646852016449, -0.027818066999316216, 0.6584276556968689, 0.6695270538330078, -0.0409860834479332, 0.6676225662231445, 0.6115372776985168, -0.05314629152417183, 0.6446422338485718, 0.6021558046340942, -0.012453695759177208, 0.6149516105651855, 0.5179146528244019, -0.029698388651013374, 0.5986732244491577, 0.4630547761917114, -0.04028636962175369, 0.5861800909042358, 0.4157763421535492, -0.04732868820428848, 0.6792464256286621, 0.5888803005218506, -0.02077343873679638, 0.6724126935005188, 0.4633972644805908, -0.04116469621658325, 0.6651234030723572, 0.3883812427520752, -0.055000174790620804, 0.6608063578605652, 0.32915201783180237, -0.06204375997185707, 0.7129302024841309, 0.6105323433876038, -0.03147866949439049, 0.7047638893127441, 0.5311749577522278, -0.06325779110193253, 0.6944117546081543, 0.6047140955924988, -0.06763556599617004, 0.6910640597343445, 0.661859393119812, -0.06192830950021744, 0.7443737983703613, 0.6523323059082031, -0.04301372542977333, 0.7289563417434692, 0.6168420910835266, -0.06915143877267838, 0.7172250747680664, 0.6740070581436157, -0.06810645014047623, 0.7137615084648132, 0.7206435203552246, -0.061206310987472534], [0.7232080101966858, 0.8471037149429321, 4.570647149648721e-07, 0.6821331977844238, 0.8125115633010864, -0.016952484846115112, 0.6562807559967041, 0.738866925239563, -0.02780112251639366, 0.6577473282814026, 0.6685487031936646, -0.04085814207792282, 0.667175829410553, 0.6093937754631042, -0.0527489148080349, 0.6441320776939392, 0.6005398631095886, -0.01192699559032917, 0.6140629649162292, 0.5164145827293396, -0.028843563050031662, 0.597350001335144, 0.4618262052536011, -0.039353784173727036, 0.5845091938972473, 0.41475996375083923, -0.04650069400668144, 0.6787043213844299, 0.587813675403595, -0.020182069391012192, 0.6719730496406555, 0.4636320173740387, -0.040477994829416275, 0.6649244427680969, 0.3891032934188843, -0.054519835859537125, 0.6609782576560974, 0.3299159109592438, -0.061840880662202835, 0.7123211026191711, 0.6102954745292664, -0.03084244392812252, 0.7046603560447693, 0.5304760336875916, -0.06244692578911781, 0.6940523982048035, 0.6041232943534851, -0.06681118160486221, 0.6905077695846558, 0.6615068316459656, -0.06124558672308922, 0.7437323331832886, 0.6525421738624573, -0.04234977066516876, 0.7284671664237976, 0.6172051429748535, -0.06861397624015808, 0.7163008451461792, 0.6741721630096436, -0.06778419017791748, 0.7125025987625122, 0.7208893895149231, -0.06106666475534439], [0.7225584387779236, 0.8471834659576416, 4.5806319803887163e-07, 0.6815620064735413, 0.8128465414047241, -0.017082074657082558, 0.6562831401824951, 0.7404870986938477, -0.028425423428416252, 0.657294511795044, 0.6710403561592102, -0.042066942900419235, 0.666638970375061, 0.6124078631401062, -0.05468754842877388, 0.6448003649711609, 0.6026839017868042, -0.012883830815553665, 0.6151084303855896, 0.517815113067627, -0.030402962118387222, 0.5985437035560608, 0.4629612863063812, -0.0411616750061512, 0.5857115387916565, 0.4153285622596741, -0.048347875475883484, 0.6792432069778442, 0.5895501375198364, -0.021477853879332542, 0.6722103357315063, 0.46388089656829834, -0.0422053337097168, 0.6648858785629272, 0.38898104429244995, -0.05615061894059181, 0.6606441736221313, 0.3291892409324646, -0.06327779591083527, 0.7127612829208374, 0.6118534803390503, -0.032466333359479904, 0.7047377228736877, 0.5310670733451843, -0.0647364929318428, 0.6948288679122925, 0.6057051420211792, -0.0687849149107933, 0.691926896572113, 0.6632322669029236, -0.06273974478244781, 0.7441092729568481, 0.6545228958129883, -0.044303201138973236, 0.7292343378067017, 0.6171474456787109, -0.07098641991615295, 0.7176762223243713, 0.6747602820396423, -0.06977120786905289, 0.7143669128417969, 0.7220607399940491, -0.06262373924255371]]
    }

    sign_detected = sign_recorder.process_results(parsed_front_data)

    print("예측값 : ")
    print(sign_detected)

    return sign_detected


    # 0. 결과 값을 return할 수 있는 String으로 추출해보기 (O)

    # 1. 일단 더미데이터를 넣어서 결과값이 추출가능한지 수정해보기 (O)
    
    # 2. record모드와 상관없이 항상 데이터를 뽑아서 보내지는지 확인해보기 (O)
    
    # 3. 프론트에서 보내고 있는 배열값을 해당 함수에서 사용하고있는 방식으로 파싱할 것 (진행중)

    # 4. 동시에 카메라가 아니라 한번의 api호출에 대한 결과 값 return으로 함수처리 수정하기 (O)

    # 5. 웹소켓 연결 및 실제 api연동해보기

    # 6. 영상을 기준으로 모델을 만드는 것 같은데 파일 기준으로 만들 수 있는지 찾아보기 (O)