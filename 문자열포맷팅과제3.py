# - 파일 제목을 다음과 같이 가공하여 출력하세요.
# - 데이터 : file_info = “20260316_test_report.pdf”
# - 출력 결과

file_info = "20260316_test_report.pdf"

print(f'작성일 : {file_info[:4]}년 {file_info[4:6]}월 {file_info[6:8]}일')
print(f'확장자 : {file_info[-3:].upper()} 문서')