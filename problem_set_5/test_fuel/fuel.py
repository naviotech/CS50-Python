def main():
    print(gauge(convert(input("Fraction: "))))


def convert(fraction):
    while True:
        try:
            x,y = fraction.split("/")
            x= int(x)
            y= int(y)
            result = ((x/y)*100)
            percentage = round(result)
            if percentage > 100:
                raise ValueError
            return percentage
        except (ValueError,ZeroDivisionError):
            continue

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif  percentage >= 99 :
        return "F"
    else:
        return(f"{percentage}%")
    

if __name__ == "__main__":
    main()