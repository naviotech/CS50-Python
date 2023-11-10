def main():
    print("Output:", shorten(input("Input: ")))

def shorten(word):
    my_list = ["A","a","E","e","i","I","O","o","U","u"]
    my_other_list = []
    for letter in word:
        if letter not in my_list:
            my_other_list.append(letter)

    conc= "".join(my_other_list)
    return conc

if __name__ == "__main__":
    main()
