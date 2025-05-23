# Installation Environment
1. Python3.9.18  사용 
2. spinqit 0.2.2 사용   
3. numpy  1.23.4 사용     
2. pyenv 가상환경 사용                      

# What is this
1. 퀀텀 otp 서비스                          <br>
2. 퀀텀 부분은 SpinQ 사의 퀀텀 시뮬레이터 사용          <br>


# How to excute
- python app.py
- 외부IP 로 접근하려면, ngrok 터널링 서비스 사용. run_ngrok.sh   확인

# Test Vidoe
- [Video Demo link](https://youtu.be/aEk2rYbvbzY)


# Main Issues
1. otp 생성시 교착상태 빠질수 있음              <br>
- export OMP_NUM_THREADS=1                      <br>
- 위 환경설정을 통해서 해결, 단일 스레드 실행: 대형 서버 CPU에서 OpenMP 스케줄러가 교착상태에 빠지는 사례 
2. 버전 맞추기 numpy==1.23.5" "spinqit==0.2.2" "python 3.9.x"                   
3. 


# pyenv 사용법
pyenv versions         # 설치된 버전/가상환경 목록          
pyenv virtualenvs      # 가상환경 목록                      
pyenv activate <name>  # 가상환경 활성화                    
pyenv deactivate       # 비활성화                           



# git 
- 강제 병합 : git pull origin main --allow-unrelated-histories   


