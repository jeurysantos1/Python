#Authot:Jeury Santos
#Title: FizzBuxx game
#Description: This game look in a range of number all number devide by 3 replace by Fizz , the same for / by 5 = Buxx and  / 3 and /5 = FizzBuzz

for number in range(1, 101):
    if (number % 3 or number % 5) == 0:
         number ="FizzBuzz"
    elif number % 3 == 0 :
        number = "Fizz"

    elif number % 5 == 0 :
        number = "Buzz"              

    print(number)
