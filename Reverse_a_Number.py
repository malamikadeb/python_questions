# Given a number num = 789, write a Python program using a while loop to reverse the number and print the result.

# dummy change

def main():
    num = 789
    reversed_num = 0
    while num > 0:
        digit = num % 10 
        num = num // 10 
        reversed_num = reversed_num * 10 + digit  
    print(reversed_num)
if __name__ == "__main__":
    main()
    
