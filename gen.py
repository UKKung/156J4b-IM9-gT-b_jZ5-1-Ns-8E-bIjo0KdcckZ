import random

lower = "qwertyuiopasdfghjkklzxcvbnmqwertyuiopasdfghjkklzxcvbnmqwertyuiopasdfghjkklzxcvbnmqwertyuiopasdfghjkklzxcvbnm"
upper = "QWERTYUIOPASDFGHJKLZXCVBNMQWERTYUIOPASDFGHJKLZXCVBNMQWERTYUIOPASDFGHJKLZXCVBNMQWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"
symbols = "[]{}().,/;:_-[]{}().,/;:_-[]{}().,/;:_-[]{}().,/;:_-[]{}().,/;:_-"

all = lower + upper + numbers + symbols
length = 40
password = "".join(random.sample(all,length))

print(password)
