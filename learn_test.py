# def greet(name):
#     """
#     这个函数用于问候某人
#     参数:
#     name: str - 需要问候的人的名字
#     """
#     name = name + "hsduhfvdu"
#     # return f"Hello, {name}!"
#     return name
#     # return f"hshfh{name}"

# print(greet("Alice"))
# help(greet)  查看函数的文档字符串

'''
此函数是问好
'''
# def intro(name):
#     #name = name +"你好"
#     return f"大家好，我是{name}"

# print(intro("lily"))
'''
def cuclulation(a , b ):
    return f" 加、减、乘、除、取余、幂计算的结果分别是：{ a + b }, { a - b }, { a * b } , { a / b } , { a % b } , { a ** b } "
'''
'''
age = 45
if age <= 18:
    print("你是未成年人")
    if 18< age<= 30 :
      print("你是中年人")
    else : 
      30< age <=50 
      print("你是中老年人")
else :
   print("你是老年人")
'''
count = 1
while count < 10:
    #print("计数:", count)
    count += 2

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits():
#      print(fruit)
# fruits = (1,2,3,4,5)
# for i in fruits:
#     print(i)
# fruits={1,2,3,4,5,6}
# for j in fruits:
#     print(j)
# fruits = {"name":"john","age" : 12,"city":"beijing"}
# for key,value in fruits.items():
#     print(f"{key}:{value}")
    
#for i in range(5):
 #   print(i)
    
# for m in range(1,5):
#     for n in range(1,5):
#         print(f"m={m},n={n}")
# 给定字符串
'''
test = "naioAbfisB\nl[56]474hello worlddnif gfj\nfhf(mfign"

# 查找 "hello world" 在字符串中的起始位置
index = test.find("hello world")

# 如果找到 "hello world"
if index != -1:
    # "hello" 前面的所有字符
    before_hello = test[:index]
    # "world" 后面的所有字符
    after_world = test[index + len("hello world"):]
    
    print("hello 前面的字符:")
    print(before_hello)
    
    print("\nworld 后面的字符:")
    print(after_world)
else:
    print("字符串中没有找到 'hello world'")
'''
'''
# 给定字符串
test = "naioAbfisB\nl[56]474hello worlddnif gfj\nfhf(mfign"

# 查找 "hello world" 在字符串中的起始位置
index = test.find("hello world")

# 判断是否存在 "hello world"
if index != -1:
    # 获取 "hello world" 前面的字符
    before_hello_world = test[:index]
    
    # 获取 "hello world" 后面的字符
    after_hello_world = test[index + len("hello world"):]
    
    # 打印结果
    print("hello world 前面的字符:")
    print(before_hello_world)
    
    print("\nhello world 后面的字符:")
    print(after_hello_world)
else:
    # 如果 "hello world" 不存在
    print("无")
'''
s = "abcdefgh"
print(s[::2])  # 输出 "aceg" - 每隔一个字符提取一次
