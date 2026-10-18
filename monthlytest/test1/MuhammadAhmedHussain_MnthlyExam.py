patient_names = ["Talha Ali", "Mujahid Hussain", "Muhaimin Asif", "Qasim Ali Shah", "G.M.Akber Khan"]
ages = [25, 24, 23, 26, 25]
temperatures = [99, 100.2, 100.1, 98.8, 100.5]
blood_pressures = [80, 105, 130, 118, 100]

normal_count = 0
attention_count = 0
critical_count = 0
total_temperature = 0

for i in range(len(patient_names)):

    name = patient_names[i]
    age = ages[i]
    temperature = temperatures[i]
    blood_pressure = blood_pressures[i]
    
    total_temperature = total_temperature + temperature
    print('The total temperate is:',total_temperature)
    
    if temperature >= 101 or blood_pressure > 140:
        status = "Critical"
        critical_count = critical_count + 1

    elif temperature > 99.5 and temperature < 101 or blood_pressure >= 120 and blood_pressure <= 139:
        status = "Needs Attention"
        attention_count = attention_count + 1

    elif temperature >= 97 and temperature <= 99.5 and blood_pressure < 120:
        status = "Normal"
        normal_count = normal_count + 1

    else:
        status = "Needs Attention"
        attention_count = attention_count + 1

    average_temperature = total_temperature / len(patient_names)

    print("Patient:", name)
    print("Age:", age)
    print("Temperature:", temperature, "°F")
    print("Systolic Blood Pressure:", blood_pressure, "mmHg")
    print("Health Status:", status)
    print("---------------------")
    print()


print("Healthcare Monitoring Summary")
print("----------------------------")
print("Total Patients:", len(patient_names))
print("Normal:", normal_count)
print("Needs Attention:", attention_count)
print("Critical:", critical_count)
print("Average Temperature:", average_temperature, "°F")
print()
