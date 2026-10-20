import statistics

# 1. Calculate mean, median and standard deviation  
def calculate_statistics(data):
    mean = statistics.mean(data)
    median = statistics.median(data)
    std_dev = statistics.pstdev(data)

    return mean, median, std_dev


# 2. Min-max normalization
def normalize_data(data):
    minimum = min(data)
    maximum = max(data)

    if minimum == maximum:
        return [0.0] * len(data)

    return [(x - minimum) / (maximum - minimum) for x in data]


# 3. Identify missing or invalid values
def find_invalid_values(data):
    invalid = []

    for i, value in enumerate(data):
        if value is None:
            invalid.append((i, value, "Missing value"))
        elif not isinstance(value, (int, float)) or isinstance(value, bool):
            invalid.append((i, value, "Invalid value"))

    return invalid


# 4. Generate summary report
def summary_report(data):
    valid_data = [
        x for x in data
        if isinstance(x, (int, float))
        and not isinstance(x, bool)
    ]

    if not valid_data:
        print("No valid numerical data available.")
        print("Invalid values:", find_invalid_values(data))
        return

    mean, median, std_dev = calculate_statistics(valid_data)

    print("\n----- SUMMARY REPORT -----")
    print("Original data:", data)
    print("Valid data:", valid_data)
    print("Mean:", mean)
    print("Median:", median)
    print("Standard deviation:", std_dev)
    print("Normalized data:", normalize_data(valid_data))
    print("Missing/Invalid values:", find_invalid_values(data))


# Main program
data = [10, 20, 30, 40, None, "abc", 50]

summary_report(data)