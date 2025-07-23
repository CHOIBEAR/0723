# 0723
📌 문자열(str)
- 인덱싱과 슬라이싱 가능: a[1:3], a[-1], a[:3]
- 반복문 사용 가능: for char in a:
- 길이 확인: len(a)
- 불변(immutable) 자료형

📌 리스트(list)
- 인덱싱, 슬라이싱 가능: b[1:3], b[-3:]
- 값 수정 및 확장 가능
- 2차원 리스트 처리 가능: a[-1:] = [b]
- 길이 확인: len(b)

📌 튜플(tuple)
- 리스트와 거의 동일하게 슬라이싱, 인덱싱 가능
- 불변(immutable)이지만 내부 가변 객체는 수정 가능
- 리스트를 튜플로 변환 가능: tuple(a)
- 예: b[1]['title'] = b[1]['title'][:4]

📌 딕셔너리(dict)
- key를 통해 value 접근: d["one"]
- for문으로 key와 value 순회 가능: for k in d: print(k, d[k])
- 길이 확인: len(d)
- 슬라이싱 불가 (예: d["one":] → 에러 발생)

📌 2차원 리스트 응용
- 리스트 안의 리스트 구조 가능
- 특정 행 교체: E[-1:] = [e]
- 행의 내용만 교체: a[1][:] = b

📌 리스트 안의 딕셔너리 다루기
- 특정 키 값 변경: arr1[0]['k1'] = arr2[0]['k1']
- 조건 필터링 (bool 값 찾기):
  for row in arr:
      for key in row:
          if type(row[key]) == bool:
              print(f'{key} : {row[key]}')

📌 튜플 내부 딕셔너리 값 수정
- 튜플로 바꿔도 내부 딕셔너리는 변경 가능:
  b[1]['title'] = b[1]['title'][:4]
  또는
  for i in b:
      if i['no'] == 2:
          i['title'] = i['title'][:4]
