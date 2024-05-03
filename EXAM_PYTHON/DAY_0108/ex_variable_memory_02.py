num1 = []
print(f"num1 => {num1} : {id(num1)}, {type(num1)}")

num2 = [11, 22.1]
print(f"num2 => {num2} : {id(num2)}, {type(num2)}")
print(f"num2[0] => {id(num2[0])}, {type(num2[0])}")
print(f"num2[1] => {id(num2[1])}, {type(num2[1])}")

print("=======값 변경=======")
# 리스트의 원소를 변경하는 경우 => 리스트 주소지는 변하지 않음
num2[0] = 100
print(f"num2 => {num2} : {id(num2)}, {type(num2)}")

# 리스트를 다른 리스트로 새로 변경하는 경우 => 리스트 주소지가 변함
num1 = num2
print(f"num1 => {num1} : {id(num1)}, {type(num1)}")