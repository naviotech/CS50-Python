def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)>=2 and len(s) <=6:
        if s[:2].isalpha():
            if s.isalnum():
                if len(s)== 3:
                    if s[-1] == "0":
                        return False
                    else:
                        return True
                elif len(s)== 4:
                    if  s[-2] == "0" :
                        return False
                    elif s[-2].isalpha() and s[-1] == "0":
                        return False
                    else:
                        return True
                elif len(s) == 5:
                    if s[2] == "0":
                        return False
                    elif s[2].isdigit() and ( s[3].isalpha() or s[4].isalpha()):
                        return False
                    elif s[2].isalpha() and s[3] == "0":
                        return False
                    elif s[-2].isalpha() and s[-1] == "0":
                        return False
                    else:
                        return True
                elif len(s) == 6:
                    if s[2].isdigit():
                        return False
                    if s[3] == "0":
                        return False
                    if s[3].isdigit() and ( s[4].isalpha() or s[5].isalpha()):
                        return False
                    if s[3].isalpha() and s[4] == "0":
                        return False
                    if s[-2].isalpha() and s[-1] == "0":
                        return False
                    else:
                        return True
                else: 
                    return False        
            else:
                return False
        else:
            return False 
    else:
        return False

if __name__ == "__main__":
    main()