#!/bin/bash
export OMP_NUM_THREADS=1

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
FLASK_LOG="flask_server_$TIMESTAMP.log"
NGROK_LOG="ngrok_$TIMESTAMP.log"

# 1. Flask 서버 실행 (날짜 로그 기록)
echo "[*] Starting Flask server..."
(
  while IFS= read -r line; do
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $line" | tee -a "$FLASK_LOG"
  done
) < <(python3 app.py 2>&1) &
FLASK_PID=$!
sleep 2

# 2. ngrok 실행 (표준출력으로 동시에 로그 + 화면 출력)
echo "[*] Starting ngrok tunnel (see below for forwarding URL)..."
ngrok http 5000 2>&1 | tee "$NGROK_LOG"

# 3. 종료 처리
echo "[*] Shutting down Flask server (PID $FLASK_PID)..."
kill $FLASK_PID
