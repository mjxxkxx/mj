class MyDate:

    def __init__(self, year = 0, month = 0, day = 0, hour = 0, minute = 0, sec = 0):
        
        assert year >= 0
        self.year = year
        
        assert 0 <= month <= 12
        self.month = month
        
        def check_valid_day(year, month, day):
            if month == 2:
                if year % 100 == 0 and year % 400 != 0 or year % 4 != 0:
                    return 0 <= day <= 28
                elif year % 4 == 0:
                    return 0 <= day <=29 
            elif month in [1, 3, 5, 7, 8, 10, 12]:
                return 0 <= day <= 31
            else:
                return 0 <= day <= 30

        check_valid_day(2022, 2, 15)
        check_valid_day(2022, 4, 60)
        
        assert check_valid_day(year, month, day)
        self.day = day

        assert 0 <= hour <= 24
        self.hour = hour

        assert 0 <= minute <= 60
        self.minute = minute

        assert 0 <= sec <= 60
        self.sec = sec

    def __add__(self, other):
    
        remainder_sec = (self.sec + other.sec) % 60
        quotient_sec = (self.sec + other.sec) // 60

        remainder_minute = (self.minute + other.minute + quotient_sec) % 60
        quotient_minute = (self.minute + other.minute + quotient_sec) // 60

        remainder_hour = (self.hour + other.hour + quotient_minute) % 24
        quotient_hour = (self.hour + other.hour + quotient_minute) // 60
        
        remainder_month = (self.month + other.month) % 12
        quotient_month = (self.month + other.month) // 12

        year = self.year + other.year
        year += quotient_month

        if remainder_month == 2:
            if year % 100 == 0 and year % 400 != 0 or year % 4 != 0:
                remainder_day = (self.day + other.day + quotient_hour) % 28
                quotient_day = (self.day + other.day + quotient_hour) // 28

            elif year % 4 == 0:
                remainder_day = (self.day + other.day + quotient_hour) % 29
                quotient_day = (self.day + other.day + quotient_hour) // 29
            
        elif remainder_month in [1, 3, 5, 7, 8, 10, 12]:
            remainder_day = (self.day + other.day + quotient_hour) % 31 
            quotient_day = (self.day + other.day + quotient_hour) // 31

        else:
            remainder_day = (self.day + other.day + quotient_hour) % 30
            quotient_day = (self.day + other.day + quotient_hour) // 30
            
        month = remainder_month + quotient_day

        if month > 12:
            remainder_month = month % 12
            quotient_month = month // 12
            month = remainder_month
            year += quotient_month

        return MyDate(year = year, month = month, day = remainder_day, hour = remainder_hour, minute = remainder_minute, sec = remainder_sec)          


    def __sub__(self, other):
        '''
        2022.03.13.01.01.01
        2022.03.12.13.10.10
        0,0,1,-12,-9,-9
        '''
        def list_sub(l, r, table = {0:12, 1:31, 2:24, 3:60, 4:60}):
            res = []
            for a, b in zip(l, r):
                res.append(a-b)
            
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

        res = list_sub(self, other, table = {0:12, 1:31, 2:24, 3:60, 4:60})
        # return MyDate(res[0], res[1], res[2], res[3], res[4], res[5])
        return MyDate(*res)

        '''
        if self.year > other.year :
            if self.month > other.month:
                if self.day > other.day:
                    if self.hour > other.hour:
                        if self.minute > other.minute:
                            if self.sec > other.sec:
                                return MyDate(year = self.year - other.year, 
                                                month = self.month - other.month, 
                                                day = self.day - other.day, 
                                                hour = self.hour - other.hour, 
                                                minute = self.minute - other.minute, 
                                                sec = self.sec - other.sec) 

                            elif self.sec < other.sec:
                                return MyDate(year = self.year - other.year, 
                                                month = self.month - other.month, 
                                                day = self.day - other.day, 
                                                hour = self.hour - other.hour, 
                                                minute = self.minute - other.minute - 1,  
                                                sec = 60 + self.sec - other.sec)
                        elif self.minute < other.minute:
                            return MyDate(year = self.year - other.year, 
                                            month = self.month - other.month, 
                                            day = self.day - other.day, 
                                            hour = self.hour - other.hour - 1, 
                                            minute = 60 + self.minute - other.minute, 
                                            sec = self.sec - other.sec) 
                    elif self.hour < other.hour:
                        return MyDate(year = self.year - other.year, 
                                        month = self.month - other.month, 
                                        day = self.day - other.day - 1, 
                                        hour = other.hour - self.hour, 
                                        minute = self.minute - other.minute, 
                                        sec = self.sec - other.sec) 
                elif self.day < other.day:
                    return MyDate(year = self.year - other.year, 
                                    month = self.month - other.month - 1, 
                                    day = self.day - other.day , 
                                    hour = self.hour - other.hour, 
                                    minute = self.minute - other.minute, 
                                    sec = self.sec - other.sec)
            elif self.month < other.month:
                return MyDate(year = self.year - other.year - 1 , 
                                month = 12 - self.month + other.month, 
                                day = sdfasdfasself.day - other.day , 
                                hour = self.hour - other.hour, 
                                minute = self.minute - other.minute, 
                                sec = self.sec - other.sec)
        '''
    def __eq__(self, other):
        if self.year == other.year \
                and self.month == other.month \
                and self.day == other.day \
                and self.hour == other.hour \
                and self.minute == other.minute \
                and self.sec == other.sec: 
            return True
        else: return False

    def __lt__(self, other):
        if self.year < other.year :
            if self.month < other.month:
                if self.day < other.day:
                    if self.hour < other.hour:
                        if self.minute < other.minute:
                            if self.sec < other.sec:
                                return True 
                            else: return False
                        else: return False
                    else: return False
                else: return False
            else: return False
        else: return False
    
    def __le__(self, other):
        if self.year <= other.year :
            if self.month <= other.month:
                if self.day <= other.day:
                    if self.hour <= other.hour:
                        if self.minute <= other.minute:
                            if self.sec <= other.sec:
                                return True 
                            else: return False
                        else: return False
                    else: return False
                else: return False
            else: return False
        else: return False

    def __gt__(self, other):
        if self.year >= other.year :
            if self.month >= other.month:
                if self.day >= other.day:
                    if self.hour >= other.hour:
                        if self.minute >= other.minute:
                            if self.sec > other.sec:
                                return True 
                            else: return False
                        else: return False
                    else: return False
                else: return False
            else: return False
        else: return False

    def __ge__(self, other):
        if self.year >= other.year :
            if self.month >= other.month:
                if self.day >= other.day:
                    if self.hour >= other.hour:
                        if self.minute >= other.minute:
                            if self.sec >= other.sec:
                                return True 
                            else: return False
                        else: return False
                    else: return False
                else: return False
            else: return False
        else: return False

if __name__ == '__main__':
    d0 = MyDate()
    d1 = MyDate(2022, 4, 1, 14, 30)
    # d2 = MyDate(2024, 8, 100, 23, 10) # should raise an error 
    # d3 = MyDate(2024, 2, 30)

    d3 = MyDate(day = 1) 
    assert d1 + d3 == MyDate(2022, 4, 2, 14, 30)
    print(d1-d3)
    assert d1 - d3 == MyDate(2022, 3, 31, 14, 30) 
    d4 = MyDate(2022, 3, 31, 14, 30)

    assert d3 + d4 == MyDate(2022, 4, 1, 14, 30)

    # assert d1 < d2 

    # d1 + d2 
    # MyDate.__add__(d1, d2)

    
    
