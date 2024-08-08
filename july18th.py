# def generate_testcases(n, min_length = 10, max_length = 100):
#     res = []
    
#     for l in range(min_length, max_length + 1):
#         for _ in range(n):
#             res.append(generate_text(l))

#     if not os.path.exists(testcase_dir):
#         os.makedirs(testcase_dir)
    
#     for idx, elem in enumerate(res):
#         f = open(f'./{testcase_dir}/testcase{idx}.para', 'w+')
#         f.write(elem)
#         f.close()

#     return res 



# def fib(n):
#     if n == 0:
#         return 1 
#     elif n == 1:
#         return 1 
    

text = ['a=1', 'b=2','a+b+3']

def eval_simple_python(text):
    result = text[-1]
    
    if not '=' in result : 
        return result   
    elif '=' in result: 
        return None
    else:
        raise ValueError

text = ['a=1', 'b=2','a+b+3']
eval_simple_python(text)
    

def eval_simple_python(text):

    last_text = text[-1].strip()  
    # Get the last text and remove leading/trailing whitespace
    
    if '=' in last_text:
        return None
    elif:
        return eval(last_text)
    else: 
        raise NameError
    

