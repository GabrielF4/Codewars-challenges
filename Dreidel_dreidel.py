class test:
    @staticmethod
    def assert_equals(test_value, expected):
        print(f"Test Passed: {expected} == {test_value}") if test_value == expected else print(f"Test Failed, expected {expected}. Got {test_value}")
        return test_value == expected

def gamble(rolls, my_coins, pot):
    
    for roll in rolls:
        if roll == 'Gimel':
            my_coins += pot
            pot = 0
        elif roll == 'Hei':
            my_coins += pot//2
            pot -= pot//2
        elif roll == 'Shin':
            pot += 1
            my_coins -= 1
        
    return my_coins

test.assert_equals(gamble(['Nun'], 10, 20), 10)
test.assert_equals(gamble(['Gimel'], 10, 20), 30)
test.assert_equals(gamble(['Hei', 'Shin'], 10, 20), 19)
test.assert_equals(gamble(['Hei', 'Hei'], 10, 20), 25)
test.assert_equals(gamble(['Hei', 'Hei', 'Hei'], 10, 20), 27)
test.assert_equals(gamble(['Nun', 'Nun', 'Shin', 'Gimel'], 10, 20), 30)
test.assert_equals(gamble(['Shin', 'Shin', 'Hei'], 10, 20), 19)
test.assert_equals(gamble(['Shin', 'Shin'], 1, 20), -1)
test.assert_equals(gamble(['Shin', 'Shin', 'Hei'], 1, 20), 10)
    
