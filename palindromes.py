
def is_palindrome(word):
    length = len(word)
    front = 0
    back = length - 1
    is_palindrome_test = True
    while (front <= back):
        if (word[front] != word[back]):
            is_palindrome_test = False
        front += 1
        back -= 1
    return is_palindrome_test

def main():
    
    with open('sgb-words.txt', "r") as txtfile:
        for line in txtfile:
            word = str(line.rstrip())
            if is_palindrome(word):
                print(word + " is a palindrome")

if __name__ == "__main__":
    main()