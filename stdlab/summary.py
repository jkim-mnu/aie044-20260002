# stdlab\summary.py
import statistics                          # 평균 등 통계 함수
from collections import defaultdict        # 처음 보는 키에 기본값을 만드는 사전
from pathlib import Path                   # 파일 경로

values = defaultdict(list)                 # 센서 이름 -> 측정값 목록
with Path("data/readings.csv").open(encoding="utf-8") as f:  # 블록이 끝나면 파일이 닫힘
    next(f)                                # 첫 줄(열 이름)은 건너뜀
    for line in f:                         # 한 줄씩 읽음
        t, sensor, v = line.strip().split(",")   # "시각,센서,값"을 셋으로 나눔
        values[sensor].append(float(v))    # 그 센서의 목록에 값(실수)을 추가

# 표 머리글: :<8은 8자리 폭 왼쪽 정렬, :>8은 8자리 폭 오른쪽 정렬
print(f"{'sensor':<8}{'count':>6}{'min':>8}{'max':>8}{'mean':>8}")
print("-" * 38)                            # 구분선(빼기 기호 38개)
for sensor in sorted(values):              # 센서 이름순(규칙 4항)
    vs = values[sensor]                    # 그 센서의 측정값 목록
    # 개수·최솟값·최댓값·평균. :>8.2f는 소수 둘째 자리(규칙 3항)
    print(f"{sensor:<8}{len(vs):>6}{min(vs):>8.2f}{max(vs):>8.2f}{statistics.mean(vs):>8.1f}")