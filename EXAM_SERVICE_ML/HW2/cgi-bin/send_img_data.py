### 모듈 로딩
import cgi, sys, codecs
import datetime
### CNN을 예측을 위한 모듈 로딩
from PIL import Image
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, WeightedRandomSampler

import torch
import torch.nn as nn

# 사전 학습된 모델 로딩
import torchvision.models as models # 다양한모델패키지
model_vgg = models.vgg16(pretrained=True)

# 사전 훈련된 모델의 파라미터 학습 유무 설정 함수
def set_parameter_requires_grad(model, feature_extract = True):
    if feature_extract:
        for param in model.parameters():
            param.requires_grad = False # 학습하는 것을 방지

set_parameter_requires_grad(model_vgg) # 함수 호출

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        # VGG16의 특성 추출기 부분만 가져오기
        self.features = model_vgg.features
        # VGG16의 특성 추출기의 출력 크기 계산
        self.num_features = 512 * 1 * 1  # VGG16은 입력 이미지를 224x224 크기로 처리하므로, 여기서는 1x1로 출력됩니다.
        # 이진 분류를 위한 새로운 fully connected layer 정의
        self.fc = nn.Sequential(
            nn.Linear(self.num_features, 4096),  # 특성 추출기의 출력 크기를 입력으로 받음
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(4096, 1),  # 이진 분류를 위한 출력 뉴런 수
            nn.Sigmoid()  # 이진 분류를 위한 시그모이드 활성화 함수
        )

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)  # flatten
        x = self.fc(x)
        return x


def predict(img_path):
    img_path = img_path[1:]
    # 모델 클래스 생성
    model = CNN()
    model.load_state_dict(torch.load('./model/model_VGG16.pth'))
    model.eval()  # 모델 추론으로 제발 좀

    # 이미지 가져오기
    image_path = img_path#######################
    image = Image.open(image_path)

    mean = [0.485, 0.456, 0.406]
    std = [0.229, 0.224, 0.225]

    preprocessing = transforms.Compose([
        transforms.Resize((50, 50), interpolation=transforms.InterpolationMode.BILINEAR),  # 1. resize
        # transforms.CenterCrop(224), # 2. 중앙크롭
        transforms.ToTensor(),  # 3. 값의 크기를 0~1로
        transforms.Normalize(mean=mean, std=std)  # 4. normalized
    ])

    # 이미지 전처리
    processed_image = preprocessing(image)

    # DataLoader에 넣기 위해 차원 추가
    processed_image = processed_image.unsqueeze(0)

    original_loader = DataLoader(processed_image)

    # GPU 연결 -> 물론 없음
    if torch.cuda.is_available():
        DEVICE = torch.device('cuda')
    else:
        DEVICE = torch.device('cpu')
    model.eval()
    correct = 0
    cnt = 0
    with torch.no_grad():
        for image in original_loader:
            image = image.to(DEVICE)

            output = model(image)
            # print(output.max(1, keepdim = True))
            prediction = output.round()  # 이진 분류에서는 반올림하여 0 또는 1로 변환
            if prediction.item() == 0:
                return "피자가 아닙니다"
            else:
                return "피자입니다"

##########################################

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# 웹 페이지의 form 태그 내의 input 태그 입력값 가져와
# 저장하고 있는 인스턴스
form = cgi.FieldStorage() # output이 우리가 생각하는  terminal이 아니라 Web임!!

# 클라이언트의 요청 데이터 추출 
if "img_file" in form :
	fileitem = form["img_file"]
 
	# 서버에 이미지 파일 저장
	img_file = fileitem.filename
	
	suffix=datetime.datetime.now().strftime("%y%m%d_%H%M%S")
	
	save_path = f"./image/{suffix}_{img_file}"
	with open(save_path, "wb") as f:
		f.write(fileitem.file.read())
  
	img_path = f"../image/{suffix}_{img_file}"
	pred_val = predict(img_path)
 
else:
  img_path = "None"
  pred_val = "입력된 사진이 없습니다"

 
 
# 요청에 대한 응답 HTML 
print("Content-Type: text/html; charset=utf-8")    # HTML is following
print()                             # blank line, end of headers
print("<TITLE>CGI script output</TITLE>")
print("<H1>This is my first CGI script</H1>")
print(f"Hello, world! ")

print(f"<img src={img_path}>")
print(f"<h3>{pred_val}</h3>") # 예측값으로 수정하기 
