# FizzBuzz Solution

class FizzBuzzConfig(object):
    def __init__(self, first_num, first_num_name, second_num, second_num_name):
        self.num_1 = first_num
        self.num_2 = second_num
        self.name_1 = first_num_name
        self.name_2 = second_num_name

class FizzBuzzer(object):
    def __init__(self, config):
        self.config = config
    
    def getFizOutput(self, num):
        product = self.config.num_1 * self.config.num_2
        if num % product == 0:
            return f"{self.config.name_1}{self.config.name_2}"
        elif num % self.config.num_1 == 0:
            return self.config.name_1
        elif num % self.config.num_2 == 0:
            return self.config.name_2
        else:
            return str(num)

def main():
    config = FizzBuzzConfig(3, "Fizz", 5, "Buzz")
    buzzer = FizzBuzzer(config)
    for i in range(1, 31):
        print(f"{buzzer.getFizOutput(i)}")


main()