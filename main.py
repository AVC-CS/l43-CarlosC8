def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    total = 0
    i = 0

    while i < 5:
        userValue = int(input("Enter a number: "))
        total = userValue + total
        i = i + 1
    print(total)

    ########################################
    # Do not delete the return statement
    ########################################
    return total


if __name__ == '__main__':
    main()
