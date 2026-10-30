
# Data Analyzer and Transformer Program
# Author: Jaineel Shingala

def calculate_factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)


def dataset_statistics(data):
    return min(data), max(data), sum(data), sum(data) / len(data)


def display_menu():
    print("\nWelcome to the Data Analyzer and Transformer Program")
    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")


def main():
    data = []

    while True:
        display_menu()
        choice = input("Please enter your choice: ").strip()

        if choice == "1":
            try:
                values = input(
                    "\nEnter data for a 1D array (separated by spaces):\n"
                )
                data = [int(x) for x in values.split()]

                if not data:
                    print("No data entered.")
                else:
                    print("\nData has been stored successfully!")

            except ValueError:
                print("Invalid input! Enter numbers only.")

        elif choice == "2":
            if not data:
                print("Please input data first.")
                continue

            print("\nData Summary:")
            print(f"- Total elements: {len(data)}")
            print(f"- Minimum value: {min(data)}")
            print(f"- Maximum value: {max(data)}")
            print(f"- Sum of all values: {sum(data)}")
            print(f"- Average value: {sum(data) / len(data):.2f}")

        elif choice == "3":
            try:
                number = int(input(
                    "\nEnter a number to calculate its factorial: "
                ))

                if number < 0:
                    print("Factorial is not defined for negative numbers.")
                else:
                    print(
                        f"\nFactorial of {number} is: "
                        f"{calculate_factorial(number)}"
                    )

            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "4":
            if not data:
                print("Please input data first.")
                continue

            try:
                threshold = int(input(
                    "\nEnter a threshold value to filter out data above this value:\n"
                ))

                filtered_data = list(
                    filter(lambda x: x >= threshold, data)
                )

                print(f"\nFiltered Data (values >= {threshold}):")
                print(", ".join(map(str, filtered_data)))

            except ValueError:
                print("Please enter a valid threshold.")

        elif choice == "5":
            if not data:
                print("Please input data first.")
                continue

            print("\nChoose sorting option:")
            print("1. Ascending")
            print("2. Descending")

            sort_choice = input("\nEnter your choice: ")

            if sort_choice == "1":
                print("\nSorted Data in Ascending Order:")
                print(", ".join(map(str, sorted(data))))

            elif sort_choice == "2":
                print("\nSorted Data in Descending Order:")
                print(", ".join(map(str, sorted(data, reverse=True))))

            else:
                print("Invalid sorting choice!")

        elif choice == "6":
            if not data:
                print("Please input data first.")
                continue

            minimum, maximum, total, average = dataset_statistics(data)

            print("\nDataset Statistics:")
            print(f"- Minimum value: {minimum}")
            print(f"- Maximum value: {maximum}")
            print(f"- Sum of all values: {total}")
            print(f"- Average value: {average:.2f}")

        elif choice == "7":
            print(
                "\nThank you for using the Data Analyzer and "
                "Transformer Program. Goodbye!"
            )
            break

        else:
            print("Invalid choice! Please select 1 to 7.")


if __name__ == "__main__":
    main()
