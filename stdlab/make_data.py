# stdlab\make_data.py
import random                              # 난수(무작위 수)를 만드는 모듈
from datetime import datetime, timedelta   # 날짜·시각 값과 시간 간격
from pathlib import Path                   # 폴더·파일 경로를 객체로 다룸

random.seed(42)                            # 시작값 고정: 누가 실행해도 같은 자료가 나옴
start = datetime(2026, 10, 14, 9, 0, 0)    # 첫 측정 시각 2026-10-14 09:00:00
lines = ["timestamp,sensor_id,value"]      # CSV 첫 줄(열 이름)
for i in range(60):                        # 측정 기록 60줄을 만듦
    t = start + timedelta(seconds=37 * i)  # i번째 측정 시각(37초 간격)
    sensor = random.choice(["T01", "T02", "T03"])  # 센서 셋 중 하나를 고름
    value = round(random.uniform(20, 30), 2)       # 20~30 사이 값, 소수 둘째 자리
    lines.append(f"{t.isoformat()},{sensor},{value}")  # "시각,센서,값" 한 줄

Path("data").mkdir(exist_ok=True)          # data 폴더가 없으면 만듦
Path("data/readings.csv").write_text("\n".join(lines) + "\n", encoding="utf-8")  # 파일로 저장
print("저장한 줄 수:", len(lines) - 1)     # 열 이름 줄을 뺀 기록 수 출력