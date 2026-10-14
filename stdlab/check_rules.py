# stdlab\check_rules.py
import subprocess                          # 다른 프로그램을 실행하는 모듈
import sys

# summary.py를 실행하고 화면 출력 대신 문자열(result.stdout)로 받음
result = subprocess.run([sys.executable, "stdlab/summary.py"],
                        capture_output=True, text=True, encoding="utf-8")
# 머리글·구분선 두 줄을 뺀 나머지 줄을 공백 기준으로 나눔 -> [센서, 개수, 최솟값, 최댓값, 평균]
rows = [line.split() for line in result.stdout.splitlines()[2:] if line.strip()]
problems = []                              # 찾은 위반을 모아 둘 목록
sensors = [row[0] for row in rows]         # 출력된 센서 이름 순서
if sensors != sorted(sensors):             # 규칙 4항: 이름순인가
    problems.append(f"규칙 4항 위반: 센서가 이름순이 아님 {sensors}")
for row in rows:
    if len(row[4].split(".")[1]) != 2:     # 규칙 3항: 평균의 소수점 아래가 두 자리인가
        problems.append(f"규칙 3항 위반: 평균 {row[4]}이 소수 둘째 자리가 아님")
for p in problems:
    print(p)
print("검사 통과" if not problems else f"검사 실패 {len(problems)}건")
sys.exit(1 if problems else 0)             # 종료 코드: 0 통과, 1 실패(자동 검사가 이 값을 봄)
