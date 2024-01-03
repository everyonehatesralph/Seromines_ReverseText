while True:
    string = input("Enter a string: ").strip()

    if string.isalpha():
        reversed = string[::-1]
        print(f"Output: {reversed}\n")
    else:
        print(f"Error Reported! Enter text only.\n")
