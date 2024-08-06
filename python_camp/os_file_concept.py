import os 
import pickle 

# --------------------------------------------
# 1. os 기초 예제 
# 
# 1) os.path 이해하기 (os.path.exists, os.path.join, os.path)
# 2) os.listdir / os.makedir 해보기 
# 3) os.getcwd / os.changedir 해보기 
# --------------------------------------------
print(os.getcwd())

for elem in os.listdir():
    if os.path.isdir(elem):
        print(f'<DIR>\t\t{elem}')
    elif '.' in elem:
        extension = elem.split('.')[-1]
        print(f'{extension} file\t\t{elem}')

def create_dir(directory_name):
    if not os.path.exists(directory_name):
        print(f"{directory_name} does not exitst;")
        os.makedirs(directory_name)
    else:
        print(f'{directory_name} does exists;')

create_dir('hello world')
# --------------------------------------------
# 2. file 기초 예제 
# 
# 1) open 이해하기 
# 2) 파일 읽기, 써보기 
# --------------------------------------------

# f = open('example.txt','w+', encoding = 'utf-8')
# f = open('example.txt','a+', encoding = 'utf-8')
# f = open('example.txt','r', encoding = 'utf-8')


# for i in range(100):
#     print(i, file = f)
#     # f.write(str(i) + '\n')
#     # print(1, file = f)

# print(f.readline())
# print(f.readline())
# for line in f.readlines():
#     print(line)

# f.close()


# --------------------------------------------
# 3. pickle 기초 예제 
# 
# 1) pickle.load() 해보기 
# 2) pickle.dump() 해보기 
# --------------------------------------------

d = {1:1}

pickle.dump(d,open('empty_dict.pickle', 'wb+'))

e = pickle.load(open('empty_dict.pickle', 'rb'))

print(e)