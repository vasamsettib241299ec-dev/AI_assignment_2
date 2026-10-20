import csv

# Read CSV, validate records and write valid records
def process_csv(input_file, output_file):
    valid_records = []
    invalid_count = 0

    try:
        with open(input_file, "r", newline="") as file:
            reader = csv.DictReader(file)

            required_columns = {
                "name", "attendance", "assignment", "exam"
            }

            if not required_columns.issubset(reader.fieldnames or []):
                print("Error: Required columns are missing.")
                return

            for row_number, row in enumerate(reader, start=2):
                try:
                    name = row["name"].strip()

                    if not name:
                        raise ValueError("Missing student name")

                    attendance = float(row["attendance"])
                    assignment = float(row["assignment"])
                    exam = float(row["exam"])

                    # Validate numerical ranges
                    if not 0 <= attendance <= 100:
                        raise ValueError("Invalid attendance")

                    if not 0 <= assignment <= 100:
                        raise ValueError("Invalid assignment marks")

                    if not 0 <= exam <= 100:
                        raise ValueError("Invalid exam marks")

                    valid_records.append({
                        "name": name,
                        "attendance": attendance,
                        "assignment": assignment,
                        "exam": exam
                    })

                except (ValueError, TypeError, AttributeError) as error:
                    invalid_count += 1
                    print(f"Row {row_number} skipped: {error}")

        # Write valid records into a new CSV file
        with open(output_file, "w", newline="") as file:
            fieldnames = [
                "name", "attendance", "assignment", "exam"
            ]

            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(valid_records)

        print("\nCSV processing completed.")
        print("Valid records:", len(valid_records))
        print("Invalid records:", invalid_count)
        print("Output file:", output_file)

    except FileNotFoundError:
        print("Error: Input CSV file not found.")

    except PermissionError:
        print("Error: Permission denied while accessing a file.")

    except csv.Error as error:
        print("CSV error:", error)

    except OSError as error:
        print("File handling error:", error)


# Main program
process_csv("students.csv", "valid_students.csv")