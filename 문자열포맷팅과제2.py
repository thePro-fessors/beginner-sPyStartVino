# - 이름의 공백을 제거하고, 성과 이름 사이에 공백을 한 칸 넣어 출력하세요.
#     - 데이터 : raw_name = “    P ark  gu n  woo”
# - 출력 결과
# - 성 : PARK   /    이름 : GUNWOO

raw_name = "    P ark  gu n  woo"
first = raw_name.replace(" ","").upper()

print(f"성 : {first[:4]} / 이름 : {first[4:]}")