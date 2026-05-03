

def seconds_to_minutes(seconds):
    return seconds / 60

def frequency_to_period(frequency):
    return 1 / frequency

print(seconds_to_minutes(120))  # Output: 2.0
print(seconds_to_minutes(90))   # Output: 1.5

print(frequency_to_period(440))  # Output: 0.0022727272727272726
print(frequency_to_period(50))  # Output: 0.02
