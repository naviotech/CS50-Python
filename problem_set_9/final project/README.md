# Kcal Calculator
#### Video Demo:  <https://youtu.be/HIPgCjF13f4>
#### Description:

"I am glad to present you the calorie calculator,
Before I start, I will explain in detail what it consists of and how this program works.

This program uses a function called `main()` as the main function. Within this function, the built-in Python library tkinter is employed, providing facilities to create a user interface for data input. Once this library is called, the interface is created according to preferences, and a nested function within main() called `bmr_calculate()` is implemented to receive user inputs through the interface.

After passing the inputs to the nested function, I call another function named `first_handling_errors()` previously created with the functionality of handling errors from the user, such as an empty string or entering letters when only numerical input is requested. It captures the error and sends a personalized message to the user for correction.

Subsequently, all inputs are converted to integers, and another error-handling function `second_handling_errors()` is called again to make a final verification that the inputs are within the correct parameters. Valid ranges are used to ensure that the numbers fall within acceptable limits.

Once all possible user errors have been captured, the program proceeds to calculate the BMI (Basal Metabolic Rate) with the given parameters. (It is the first step in calculating a person's total calorie intake.)

To conclude the functionality of total calorie calculation, another external function called `tee_calculate() ` is called. This function calculates the total calories by passing the parameters resulting from the BMR calculation.

After completing this functionality and taking these data, I call another external function called `macronutrients()`. This function calculates the specific recommended macronutrients for a proper distribution.

Finally, I call the last external function called `bmi_calculate()`, which calculates the Body Mass Index of the user, taking as parameters the weight and height provided by the user.

Once all calculations for each functionality are done, I communicate the results to the user through the interface. If the parameters have not been entered correctly, they will also be communicated in the interface in `red`. In any other case, the information will be displayed in `green`.

To close the project, I perform testing on some of my functions, especially the error-handling functions, as they are crucial for the smooth flow of the program. Once testing is complete, all that is left is to note the requirements to initiate the program. These requirements would include:

-Having the `tkinter` library installed.
-Having `pytest` installed (in case testing is desired).

I hope you enjoyed my final project in CS50 Python, and I invite you to try it on your system.

