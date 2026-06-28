# 4번 : 5명의 학생 점수가 담긴 리스트 score = [70, 60, 55, 90, 85]가 있습니다. score에서 최고 점수와 최저 점수, 평균 점수를 출력하세요.

score = [70, 60, 55, 90, 85]
print(f'최고점수: {max(score)}')
print(f'최저점수: {min(score)}')
print(f'평균점수: {sum(score) // 5}')