# 문제 1. 문자열 a = "Python"이 있을 때, 인덱스를 사용해 't'를 출력하는 코드를 작성하시오.

# 문제 2. 문자열 "Python"에서 'yth'만 슬라이싱으로 출력하는 코드를 작성하시오.

# 문제 3. 리스트 b = [10, 20, 30, 40, 50]의 길이를 출력하는 코드를 작성하시오.

# 문제 4. 위 리스트 b에서 마지막 3개 요소만 출력하는 코드를 작성하시오.

# 문제 5. 튜플 c = (1, 2, 3)의 두 번째 값을 10으로 바꾸는 코드를 작성하면 어떤 오류가 발생하는지 설명하시오.

# 문제 6. 딕셔너리 d = {"one": 1, "two": 2}에서 키 "two"에 해당하는 값을 출력하는 코드를 작성하시오.

# 문제 7. 딕셔너리 d = {"one": 1, "two": 2, "three": 3}에서 "one":"three"처럼 슬라이싱을 하면 어떤 오류가 발생하는지 설명하시오.

# 문제 8. 2차원 리스트 e = [[1, 2], [3, 4], [5, 6]]의 마지막 행을 [7, 8]로 바꾸는 코드를 작성하시오.

# 문제 9. 리스트 arr = [{"a": 10}, {"a": True}, {"a": "hello"}]에서 값이 논리형인 딕셔너리만 출력하는 코드를 작성하시오.

# 문제 10. 다음 리스트를 튜플로 변환한 후, 두 번째 요소의 'title' 값이 'JavaScript'에서 'Java'가 되도록 슬라이싱을 이용하여 수정하는 코드를 작성하시오.  
# 단, 튜플 전체를 재정의하거나 직접 문자열을 대입하지 말고 슬라이싱만 사용할 것.

# a = [
#   {'no': 1, 'title': 'Python'},
#   {'no': 2, 'title': 'JavaScript'},
#   {'no': 3, 'title': 'CSS'}
# ]
# b = tuple(a)

# 문제 1. 문자열 a = "Python"이 있을 때, 인덱스를 사용해 't'를 출력하는 코드를 작성하시오.
a = "Python"
print(a[3])  # 't' 출력

# 문제 2. 문자열 "Python"에서 'yth'만 슬라이싱으로 출력하는 코드를 작성하시오.
print(a[1:4])  # 'yth' 슬라이싱 출력

# 문제 3. 리스트 b = [10, 20, 30, 40, 50]의 길이를 출력하는 코드를 작성하시오.
b = [10, 20, 30, 40, 50]
print(len(b))  # 리스트 b의 길이 출력

# 문제 4. 위 리스트 b에서 마지막 3개 요소만 출력하는 코드를 작성하시오.
print(b[-3:])  # 마지막 3개 요소 출력

# 문제 5. 튜플 c = (1, 2, 3)의 두 번째 값을 10으로 바꾸는 코드를 작성하면 어떤 오류가 발생하는지 설명하시오.
c = (1, 2, 3)
# 튜플의 요소는 변경할 수 없으므로 변경하는 코드를 작성하면 오류를 발생시킴.

# 문제 6. 딕셔너리 d = {"one": 1, "two": 2}에서 키 "two"에 해당하는 값을 출력하는 코드를 작성하시오.
d = {"one": 1, "two": 2}
print(d["two"])  # 키 "two"에 해당하는 값 출력

# 문제 7. 딕셔너리 d = {"one": 1, "two": 2, "three": 3}에서 
# "one":"three"처럼 슬라이싱을 하면 어떤 오류가 발생하는지 설명하시오.

# 딕셔너리는 슬라이싱을 지원하지 않으므로,
# d["one":"three"]와 같은 코드를 작성하면 오류가 발생함.

# 문제 8. 2차원 리스트 e = [[1, 2], [3, 4], [5, 6]]의 마지막 행을 [7, 8]로 바꾸는 코드를 작성하시오.
e = [[1, 2], [3, 4], [5, 6]]
e[-1] = [7, 8]  # 마지막 행을 [7, 8]로 변경
print(e)  # 변경된 2차원 리스트 출력

# 문제 9. 리스트 arr = [{"a": 10}, {"a": True}, {"a": "hello"}]에서
# 값이 논리형인 딕셔너리만 출력하는 코드를 작성하시오.
arr = [{"a": 10}, {"a": True}, {"a": "hello"}]
for i in arr:
    if type(i["a"]) == bool:
        print(i)
# 문제 10. 다음 리스트를 튜플로 변환한 후, 두 번째 요소의 'title' 값이 'JavaScript'에서 'Java'가 되도록 슬라이싱을 이용하여 수정하는 코드를 작성하시오.  
# 단, 튜플 전체를 재정의하거나 직접 문자열을 대입하지 말고 슬라이싱만 사용할 것.

a = [
  {'no': 1, 'title': 'Python'},
  {'no': 2, 'title': 'JavaScript'},
  {'no': 3, 'title': 'CSS'}
]
b = tuple(a)

for i in b:
    if i['no'] == 2:
        i['title'] = i['title'][:4]  # 'Java'까지만 남김
print(b)  # 수정된 딕셔너리 출력
#튜플은 불변임으로 직접 수정할 수 없지만 튜플 내부의 요소가 딕셔너리나 리스트라면 그 내부의 요소는 
#수정할 수 있음.   
