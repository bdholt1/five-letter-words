
def is_palindrome(word):
    return word == word[::-1]

def main():
    
    with open('sgb-words.txt', "r") as txtfile:
        for line in txtfile:
            word = str(line.rstrip())
            if is_palindrome(word):
                print(word + " is a palindrome")

if __name__ == "__main__":
    main()