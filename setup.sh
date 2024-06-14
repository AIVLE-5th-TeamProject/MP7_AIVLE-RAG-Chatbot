#!/bin/bash


# 프로젝트 루트 디렉토리에 database 및 documents 폴더 생성
mkdir -p database documents

# conda 가상환경 생성 및 활성화
if conda info --envs | grep -q "mini7"; then
  echo "Conda environment 'mini7' already exists."
else
  conda create --name mini7 python=3.11.9 -y
  echo "Created conda environment 'mini7'."
fi

source $(conda info --base)/etc/profile.d/conda.sh
conda activate mini7

# 가상환경에 필요한 모듈 설치
pip install -r requirements.txt

# 데이터베이스 마이그레이션 파일 생성
python manage.py makemigrations

# 생성된 마이그레이션 파일을 데이터베이스에 적용
python manage.py migrate

# 관리자 페이지 접근용 슈퍼유저 생성 (Username, Email, Password를 입력해야 함)
echo "슈퍼유저 계정을 생성하려면 아래의 프롬프트에 따라 Username, Email, Password를 입력하세요:"
python manage.py createsuperuser

# 가상환경 비활성화
conda deactivate

echo "설치 및 설정이 완료되었습니다."
