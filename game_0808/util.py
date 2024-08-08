def list_sub(l, r, table = {0:12, 1:31, 2:24, 3:60, 4:60}):
    res = []
    for a, b in zip(l, r):
        res.append(a-b)
    
    # 처음으로 0이 아닌 양수인 res의 element 찾기 

    first_nonzero_idx = 0

    for idx, elem in enumerate(res):
        if elem > 0:
            first_nonzero_idx = idx 
            break 
    else:
        assert False, f'{r} is larger than {l}'
    
    for idx, elem in enumerate(res[first_nonzero_idx:-1], start = first_nonzero_idx):
        if res[idx+1] < 0: # idx에서 idx + 1로 받아내림을 실행 
            res[idx] = res[idx] - 1 
            res[idx+1] = table[idx] + res[idx+1]
    return res 

if __name__ == '__main__':
    print(list_sub([2022, 1, 1, 0, 0, 0], [2021, 12, 31, 23, 59, 59]))