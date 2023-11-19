#Kcal Calculator
try:
    import tkinter as tk
except ImportError:
    print("Tkinter is not installed.")

def first_handling_errors(weight, age,height):
    if weight == "":
        raise ValueError("Enter a value for weight.")
    if age == "":
        raise ValueError("Enter a value for age")
    if height == "":
        raise ValueError("Enter a value for height")
    if not weight.isdigit():
        raise TypeError("Weight must be a number.")
    if not height.isdigit():
        raise TypeError("Height must be a number.")
    if not age.isdigit():
        raise TypeError("Age must be a number.")
    
def second_handling_errors(weight,age,height,sexe,activity):
    if weight>300 or weight<15:
        raise ValueError("¡Enter valid values for weight! ")
    if age<1 or age>160:
        raise ValueError("¡Enter valid values for age!")
    if height<50 or height>300:
        raise ValueError("¡Enter valid values for height!")
    if not sexe in [1,2]:
        raise ValueError("Please introduce a value for gender.")
    if activity not in [1,2,3,4,5]:
        raise ValueError("Please introduce a value for activity level.")
def tee_calculate(info=list):
        
        geb, activity = info
        if activity == 1:
            tee = geb * 1.2
        elif activity == 2:
            tee = geb * 1.375
        elif activity == 3:
            tee = geb * 1.55
        elif activity == 4:
            tee = geb * 1.725
        else:
            tee = geb * 1.9
         
        result = tee
        return result

def macronutrients(tee):
    protein = (tee * 0.2)/4
    fat = (tee * 0.3)/9
    carbohydrate = (tee * 0.5)/4
    values = [protein, fat, carbohydrate]
    return values

def bmi_calculate(weight,height):
    bmi = weight/((height/100)**2)
    if bmi < 18.5:
        indication = "Underweight"
    elif 18.5<= bmi < 25:
        indication = "Normal Weight"
    elif 25<= bmi < 30:
        indication = "Overweight"
    else:
        indication = "Obese"

    dates_bmi=[bmi,indication]
    return dates_bmi
    
def main():
    def bmr_calculate():
        try:
            first_handling_errors(weight_dates.get(), age_dates.get(),height_dates.get())
            name = name_dates.get()
            weight = int(weight_dates.get())
            height = int(height_dates.get())
            age = int(age_dates.get())
            sexe = int(div_gender.get())
            activity = int(div_activity.get())
            #Handling errors
            second_handling_errors(weight,age,height,sexe,activity)
            if sexe == 1:
                bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
            else:
                bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

            my_list_values=[bmr,activity]
            
            tee= tee_calculate(my_list_values)
            parameters = macronutrients(tee)
            bmi, indication = bmi_calculate(weight,height)

            protein, fat , carbohydrates = parameters

            result_label.config(text=f"Hey {name}, the calories you need per day are {tee:.1f}kcal\n"
                            "and the standard nutritional parameters for macronutrients would be\n"
                            f"{carbohydrates:.1f} gr of carbohydrates, {protein:.1f} gr of protein and "
                            f"{fat:.1f} gr of fat.\n"
                            f"The resulting BMI was {bmi:.2f} points, and due to this\n score, your weight is in {indication}", bg="green")
        
        except ValueError as error:
            result_label.config(text=f"{error}", bg="red")
        except TypeError as e:
            result_label.config(text=f"{e}", bg="red")
       
        
    window = tk.Tk()
    window.title("Kcal Calculator")
    window.config(bg="#535353")

    #finallyvariables
    name_dates = tk.Entry(window, fg="white", background="#353535")
    weight_dates = tk.Entry(window, fg="white", background="#353535")
    height_dates = tk.Entry(window, fg="white", background="#353535")
    age_dates = tk.Entry(window, fg="white", background="#353535")
    div_gender = tk.IntVar()
    div_activity = tk.IntVar()

    #name
    name_etiquette = tk.Label(window, text="Name:", fg="white", background="#535353")
    name_etiquette.grid(row=0, column=0, padx=10, pady=10)
    name_dates.grid(row=0, column=1, padx=10, pady=10)

    #etiquette kg
    weight_etiquette = tk.Label(window, text="Weight (kg):", fg="white", background="#535353")
    weight_etiquette.grid(row=1, column=0, padx=10, pady=10)
    weight_dates.grid(row=1, column=1, padx=10, pady=10)

    #etiquette cm
    height_etiquette = tk.Label(window, text="Height (cm):", fg="white", background="#535353")
    height_etiquette.grid(row=2, column=0, padx=10, pady=10)
    height_dates.grid(row=2, column=1, padx=10, pady=10)

    #etiquette Age
    age_etiquette = tk.Label(window, text="Age (years):", fg="white", background="#535353")
    age_etiquette.grid(row=3, column=0, padx=10, pady=10)
    age_dates.grid(row=3, column=1, padx=10, pady=10)

    #button male/female
    gender_etiquette = tk.Label(window, text="Gender:", fg="white", background="#535353")
    gender_etiquette.grid(row=4, column=0, padx=2, pady=10)
    if_male = tk.Radiobutton(window, text="Male", variable=div_gender, value=1, background="#535353")
    if_male.grid(row=4, column=1, padx=10, pady=10, sticky="w")
    if_female = tk.Radiobutton(window, text="Female", variable=div_gender, value=2, background="#535353")
    if_female.grid(row=4, column=2, padx=10, pady=10, sticky="w")

    #button level activity
    activity_etiquette = tk.Label(window, text="Activity Level:", fg="white", background="#535353")
    activity_etiquette.grid(row=5, column=0, padx=2, pady=10)
    if_sedentary = tk.Radiobutton(window, text="Sedentary", variable=div_activity, value=1, background="#535353")
    if_sedentary.grid(row=5, column=1, padx=2, pady=10, sticky="w")
    if_light = tk.Radiobutton(window, text="Light", variable=div_activity, value=2, background="#535353")
    if_light.grid(row=5, column=2, padx=10, pady=10, sticky="w")
    if_moderate = tk.Radiobutton(window, text="Moderate", variable=div_activity, value=3, background="#535353")
    if_moderate.grid(row=6, column=1, padx=1, pady=10, sticky="w")
    if_active = tk.Radiobutton(window, text="Active", variable=div_activity, value=4, background="#535353")
    if_active.grid(row=6, column=2, padx=10, pady=10, sticky="w")
    if_very_active = tk.Radiobutton(window, text="Very Active", variable=div_activity, value=5, background="#535353")
    if_very_active.grid(row=6, column=3, padx=10, pady=10, sticky="w")

    #button
    button_calc = tk.Button(window, text="Calculate", command=bmr_calculate, fg="white", background="#696969")
    button_calc.grid(row=7, column=0, columnspan=2, pady=10)

    #result
    result_label = tk.Label(window, text="", fg="white", background="#535353")
    result_label.grid(row=8, column=1, columnspan=2, pady=10)

    window.mainloop()
   


if __name__ == "__main__":
    main()
