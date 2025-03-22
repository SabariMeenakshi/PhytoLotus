# Parameters from the regression model
m = -1.4747  # Slope
c = 207.93461   # Intercept

# Learning rate for coefficient updates
learning_rate = 0.00005

original_m = m
original_c = c

def linear_func(temp, m, c):
    return m * temp + c

def predict_duration(temp, concentration):
    # Calculate duration in hours based on temperature
    duration_hours = linear_func(temp, m, c)
    # Adjust duration based on concentration of contaminants
    adjusted_duration_hours = duration_hours * (concentration * (1/98))
    # Convert hours to days
    duration_days = adjusted_duration_hours / 24
    return adjusted_duration_hours, duration_days

def determine_lotuses(flow_rate):
    if 50 <= flow_rate <= 100:
        return "Use 4 lotuses as treatment"
    elif 100 < flow_rate <= 200:
        return "Use 5 lotuses as treatment"
    elif 200 < flow_rate <= 400:
        return "Use 6 lotuses as treatment"
    elif 400 < flow_rate <= 500:
        return "Use 7 lotuses as treatment"
    elif flow_rate > 500:
        return ("This project will require a significant amount of lotuses, so please "
                "talk to your local government officials, obtain necessary legal documents or "
                "licenses, and consult a professional ecologist or environmental scientist.")
    else:
        return "Use 3 lotuses as treatment."

def update_coefficients(temp, actual_duration):
    global m, c
    predicted_duration = linear_func(temp, m, c)
    error = actual_duration - predicted_duration
    m += learning_rate * error * temp
    c += learning_rate * error
    return m, c

def guide_for_updating_coefficients():
    guide = (
        "### Guide for Updating Coefficients ###\n"
        "1. When the predicted duration is incorrect, provide the correct duration when prompted.\n"
        "2. The program calculates the error between the predicted and actual duration.\n"
        "3. Using the error, the coefficients (m and c) are updated as follows:\n"
        "   - m_new = m + learning_rate * error * temperature\n"
        "   - c_new = c + learning_rate * error\n"
        "4. A learning rate is applied to ensure minimal updates for gradual improvement.\n"
        "5. After updating, the new coefficients are displayed.\n"
        "6. Use the updated coefficients for improved predictions in subsequent runs.\n"
    )
    print(guide)

# Input date
user_date = input("Enter the current date (YYYY-MM-DD): ")

# Input temperature
temperature = float(input("Enter the temperature in Fahrenheit: "))

# Input flow rate
flow_rate = float(input("Enter the river flow rate in gallons per second: "))

# Input total concentration of contaminants
contaminants_concentration = float(input("Enter the total concentration of contaminants in ppm: "))

# Predict duration incorporating the concentration of contaminants
adjusted_duration_hours, adjusted_duration_days = predict_duration(temperature, contaminants_concentration)

# Determine number of lotuses
lotus_advice = determine_lotuses(flow_rate)

# Display results
print(f"Adjusted treatment duration at {temperature}°F with {contaminants_concentration} ppm of contaminants:")
print(f"- {adjusted_duration_hours:.2f} hours")
print(f"- {adjusted_duration_days:.2f} days")
print(f"Lotus recommendation based on flow rate ({flow_rate} gallons/second):")
print(f"- {lotus_advice}")

# Validate output
is_correct = input("Is the predicted duration correct? (yes/no): ").strip().lower()
log_summary = [
    f"Date: {user_date}",
    f"Temperature: {temperature}°F",
    f"Flow rate: {flow_rate} gallons/second",
    f"Contaminant concentration: {contaminants_concentration} ppm",
    f"Predicted duration: {adjusted_duration_hours:.2f} hours, {adjusted_duration_days:.2f} days",
    f"Lotus recommendation: {lotus_advice}",
    f"Original coefficients: m = {original_m:.5f}, c = {original_c:.5f}",
    f"User validation: {is_correct}"
]

if is_correct == "no":
    actual_duration = float(input("Enter the correct duration in hours: "))
    new_m, new_c = update_coefficients(temperature, actual_duration)
    log_summary.append(f"Correct duration provided: {actual_duration} hours")
    log_summary.append(f"Updated coefficients: m = {new_m:.5f}, c = {new_c:.5f}")
    print("Updated coefficients:")
    print(f"m = {new_m:.5f}")
    print(f"c = {new_c:.5f}")
    print("The coefficients have been updated. For detailed guidance, refer to the steps below:")
    guide_for_updating_coefficients()

# Log the entire summary
print("\n### Log Summary ###")
for event in log_summary:
    print(event)


