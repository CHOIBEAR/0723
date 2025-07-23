# a = "문자열"
# b = [1,2,3,4,5,6,7,8,9,10]
# c=(1,2,3,4,5,6,7,8,9,10)
# d={"one": 1, "two": 2, "three": 3,"four": 4, "five": 5}

# for txt in a:
#     print(txt)
# print(a[0])
# print(a)
# print(type(a))
# print(a[0:])
# print(a[1:3])
# print(a[1:])  # from index 1 to the end
# print(a[:3])  # from the start to index 3
# print(a[-1])  # last character
# print(a[-2])  # second last character
# print(a[-3:])  # last three characters
# print(len(a))  # length of the string

# for i in b:
#     print(i)
# print(b[0])
# print(b)
# print(type(b))
# print(b[0:])
# print(b[1:3])  # from index 1 to index 3 (exclusive)
# print(b[1:])  # from index 1 to the end
# print(b[:3])  # from the start to index 3 (exclusive)
# print(b[-1])  # last element
# print(b[-2])  # second last element
# print(b[-3:])  # last three elements
# print(len(b))  # length of the list

# for i in c:
#     print(i)
# print(c[0])
# print(c)
# print(type(c))
# print(c[0:])
# print(c[1:3])  # from index 1 to index 3 (exclusive
# print(c[1:])  # from index 1 to the end
# print(c[:3])  # from the start to index 3 (exclusive)
# print(c[-1])  # last element
# print(c[-2])  # second last element
# print(c[-3:])  # last three elements
# print(len(c))  # length of the tuple

# for i in d:
#     print(i, d[i])
# print(d["one"])
# print(d)
# print(type(d))
# print(d["one":])  # This will raise an error since dicts do not support slicing
# print(d["one":"three"])  # This will also raise an error
# print(d["one":"five"])  # This will also raise an error
# print(d["one":"four"])  # This will also raise an error
# print(d["one":"five"])  # This will also raise an error
# print(len(d))  # length of the dictionary   

# E=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# e= [10, 11, 12]

# E[-1:] =[e]
# print(E)

# a = [
#     [1,2,3],
#     [4,5,6,7],
# ]
# b = [8,9]
# a[-1:] = [b] # << 문제 a[:] 이용하여 b의 리스트로 변경하기!!

# # 1. 삭제 후 추가 방법
# # del a[1:]
# # a.append(b)

# # 2. 2차원 배열 그대로 변경 하는 방법
# # a[-1:] = [b]

# # 3. 1차원 배열를 기준으로 변경하는 방법
# # a[1][:] = b

# print(a)

# a= {"k1":10, "k2":20, "k3":30}

# b={"k1":30}

# # a["k1"]= b["k1"]
# # a=b

# arr1=[a]
# arr2=[b]

# arr1[0]["k1"]= arr2[0]["k1"]
# print(arr1)

# a = {"k1":10, "k2":20, "k3":30}
# b = {"k1":'케이1', "k2":'케이2', "k3":'케이3'}
# c = {"k1":True,"k2":False}

# arr= [a, b, c]
# #문제. 리스트 행 중에 값이 논리형인 행을 찾아서 출력하기.
# print(arr[2])
# print(arr[-1:])
# print(arr[2]['k1'])  # True
# print(arr[2]['k2'])  # False

# for i in arr:
#     for key in i:
#         if type(i[key]) == bool:
#             print(f"Key: {key}, Value: {i[key]}")

# 1. 슬라이싱 방법으로 선택적으로 출력
# print(arr[-1:])

# 2. 각 행에 있는 값을 매번 조건문으로 비교 후 출력
# if type(arr[0]['k1']) == bool:
#   print(arr[0])
# if type(arr[1]['k1']) == bool:
#   print(arr[1])
# if type(arr[2]['k1']) == bool:
#   print(arr[2])

# 3. 2번 방식을 중복을 해결 하기 위해서 반복문으로 출력
# for row in arr:
#   for key in row:
#     if type(row[key]) == bool:
#       print(f'{key} : {row[key]}')

# a = [
#   {'no': 1, 'title': 'Python'},
#   {'no': 2, 'title': 'JavaScript'},
#   {'no': 3, 'title': 'CSS'}
#   ]

# # print(type(a), a)
# b = tuple(a)
#  # print(type(b), b)


# a = [
#   {'no': 1, 'title': 'Python'},
#   {'no': 2, 'title': 'JavaScript'},
#   {'no': 3, 'title': 'CSS'}
#   ]
# b = tuple(a)
# #b[1]['title'] = 'Java'
# # 문제) 위의 코드 방식이 아닌 슬라이싱 방법으로 title의 값이 'Java'가 될 수 있도록 코드를 작성하세요.

# b[1]['title'] = b[1]['title'][:4]
# print(b)

# for i in b:
#     if i['no'] == 2:
#         i['title'] =i ['title'][0:4]
# print(b)

# 1. 슬라이싱을 이용하여 선택적 값 변경
# b[1]['title'] = b[1]['title'][:4]

# 2. 해당 key인 `no`의 값을 확인 후 슬라이싱 방법으로 값 변경
# for row in b:
#   if row['no'] == 2:
#     row['title'] = row['title'][:4]