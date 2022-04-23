# LEDModule
LCDApp에서 이용 가능한 LED 모듈 연동기능에 대한 설명

# 개요
LCDApp에서는 지하철 및 고속열차의 LCD 디스플레이 시뮬레이션을 제공합니다.

이 LCDApp과 연동할 수 있는 LED 모듈인 MAX7219를 설치하여 서울교통공사 신형 전동차에 설치된 소형 LED 전광판도 시뮬레이션 할 수 있습니다. 단 여러 MAX7219를 연결하여 32x8 크기 이상의 LED를 사용하게 하는 Daisy-Chain (데이지체인)은 지원하지 않음을 알려드립니다.


동영상으로 시뮬레이션 예시 보기:
<a href="https://youtu.be/B3ViA21AWCQ">▶ YouTube 링크</a>

# 준비물
Raspberry Pi, 16GB 이상의 Micro SD 카드, <a href="http://m.intopion.com/goods/view?no=3831560">암-암 점퍼케이블</a>, Max7219, 8x8 LED 모듈 4개

# Raspberry Pi OS 플래시하기
데스크톱이나 Mac에 Micro SD 카드를 연결한 뒤 <a href="https://www.raspberrypi.com/software/">Raspberry Pi Imager</a>를 실행합니다.

**Raspbery Pi OS (32-bit)**을 운영체제로 선택하고 저장소 선택에서 자신의 Micro SD카드를 선택한 뒤 플래싱을 진행해주세요.

플래싱이 완료되면, 해당 Micro SD 카드를 Raspberry Pi에 연결하고, Raspberry Pi에 마우스, 키보드, HDMI 케이블을 연결하여 데스크톱 컴퓨터처럼 설정을 진행해줍니다.

이때, Wi-Fi 국가를 대한민국으로 설정해서는 안 되며, 미국으로 설정해주시기 바랍니다.
이외 자세한 설명은 Raspberry Pi 설정법을 검색해주시기 바랍니다.

# Git 리포지토리 복제하기
그 다음 터미널 에뮬레이터에서
```
git clone https://github.com/injeonmetro/LEDModule.git
```
을 입력하여 Git 리포지토리를 복제해줍니다.
완료되었다면
```
cd LEDModule/max7219
```
를 입력하여 MAX7219의 폴더로 이동합니다.
그 다음 필요한 모듈을 설치합니다.
```
python3 install -U -r requirements.txt
```
만약 실행에 성공하지 못했다면, Raspberry Pi의 파이썬 구동 모듈의 버전이 낮은 것이므로
```
sudo apt-get update&&sudo apt-get upgrade
```
를 입력하여 모듈들을 업그레이드 한 뒤 위 명령어를 다시 실행해줍니다.

# 전 단계에서 설치한 모듈 실행하기
전 단계에서는 LED를 실행시키는 LumaLED 모듈, 같은 네트워크의 다른 기기에서도 LED를 이용할 수 있게 하는 FastAPI와 FastAPI의 서버를 운영시키는 Uvicorn을 설치했습니다.
이제 해당 코드를 실행합니다.
```
python3 -m uvicorn main:app --reload --host:0.0.0.0
```

# LCDApp에서 실행하기
LCDApp에서는 Raspberry Pi의 내부 IP주소를 복사, 붙여넣기 해주시기 바랍니다. `http://`, `:8000`, `docs`와 같은 불필요한 접두사를 제외한 오로지 주소만을 입력하지 않으면 정상적인 연동이 불가능해집니다.
