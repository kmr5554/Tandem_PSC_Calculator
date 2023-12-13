
# Importing the run module
import refined_run

# Prompt user for input
Tcell = float(input("Enter cell temperature (in Kelvin): "))
Egap = float(input("Enter energy gap (in electron volts): "))

# Execute the run module with user inputs
refined_run.main(Tcell, Egap)
