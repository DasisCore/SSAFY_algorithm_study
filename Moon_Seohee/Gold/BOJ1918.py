# BOJ1918 후위표기식

lst = input()
new_lst = []
stack = []
for i in lst:
    if 65 <= ord(i) <= 90:
        new_lst.append(i)
    elif i == "(":
        stack.append(i)
    elif i == ")":
        while True:
            tem = stack.pop()
            if tem != "(":
                new_lst.append(tem)
            else :
                break
    elif i == "+" or i == "-":
        while True:
            if stack == [] or stack[-1] == "(":
                stack.append(i)
                break
            else :
                new_lst.append(stack.pop())                     
    elif i == "*" or i == "/":
        while True:
            if stack == [] or stack[-1] == "(" or stack[-1] == "+" or stack[-1] == "-":
                stack.append(i)
                break
            else :
                new_lst.append(stack.pop())        

for j in range(len(stack)):
    new_lst.append(stack.pop())

result = "".join(new_lst)
print(result)