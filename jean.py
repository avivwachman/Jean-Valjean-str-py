__author__ = "aviv"

if __name__ == '__main__':
    message = input("Please enter a 5 digit number\n")
    # 24601
    while len(message) != 5:
        message = input("Error not a 5 digit number, enter again\n")
    summ = 0
    print(f"You entered the number: {message}")
    mess_len = len(message)
    print("The digits of the number are: ", end='')
    for i in range(mess_len):
        summ += int(message[i])
        if i + 1 == mess_len:
            print(f"{message[i]}")
        else:
            print(f"{message[i]},", end='')
    print("The sum of the digits is: " + str(summ), end='')
