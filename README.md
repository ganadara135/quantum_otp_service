# 설치환경
1. Python3.9.18  사용, spinqit 패키지는 3.9 에서 설치 가능
2. pyenv 가상환경 사용

# 서비스 작동 가정
1. 퀀텀 otp 서비스 
2. 퀀텀 부분은 SpinQ 사의 퀀텀 시뮬레이터 사용



# 실행시 이슈
1. otp 생성시 교착상태 빠질수 있음
- export OMP_NUM_THREADS=1    
- 위 환경설정을 통해서 해결, 단일 스레드 실행: 대형 서버 CPU에서 OpenMP 스케줄러가 교착상태에 빠지는 사례
2. 버전 맞추기 numpy==1.23.5" "spinqit==0.2.2" "python 3.9.x"
3. 


# pyenv 사용법
pyenv versions         # 설치된 버전/가상환경 목록
pyenv virtualenvs      # 가상환경 목록
pyenv activate <name>  # 가상환경 활성화
pyenv deactivate       # 비활성화

