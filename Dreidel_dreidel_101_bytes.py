class test:
    @staticmethod
    def assert_equals(test_value, expected):
        print(f"Test Passed: {expected} == {test_value}") if test_value == expected else print(f"Test Failed, expected {expected}. Got {test_value}")
        return test_value == expected

def gamble(r,c,p):
    a = {'G':lambda c,p:(c+p,0),'H': lambda c,p:(c+p//2,p-p//2),'S':lambda c,p:(c-1,p+1),'N':lambda c,p:(c,p)}
    for x in r:
        c,p=a[x[0]](c,p)
    return c

a={'G':lambda c,p:(c+p,0),'H': lambda c,p:(c+p//2,p-p//2),'S':lambda c,p:(c-1,p+1),'N':lambda c,p:(c,p)}

test.assert_equals(gamble(['Nun'], 10, 20), 10)
test.assert_equals(gamble(['Gimel'], 10, 20), 30)
test.assert_equals(gamble(['Hei', 'Shin'], 10, 20), 19)
test.assert_equals(gamble(['Hei', 'Hei'], 10, 20), 25)
test.assert_equals(gamble(['Hei', 'Hei', 'Hei'], 10, 20), 27)
test.assert_equals(gamble(['Nun', 'Nun', 'Shin', 'Gimel'], 10, 20), 30)
test.assert_equals(gamble(['Shin', 'Shin', 'Hei'], 10, 20), 19)
test.assert_equals(gamble(['Shin', 'Shin'], 1, 20), -1)
test.assert_equals(gamble(['Shin', 'Shin', 'Hei'], 1, 20), 10)
    
