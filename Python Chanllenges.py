def calculate_allocation(num_students):
    try:
        # Convert the input to an integer
        num_students = int(num_students)

        # Calculate the number of classes needed
        num_classes = (num_students + 29) // 30

        # Calculate the distribution of students per class
        students_per_class = num_students // num_classes
        remaining_students = num_students % num_classes

        # Create the allocation dictionary
        allocation = {}
        assigned_students = 0
        for i in range(1, num_classes + 1):
            # assign remaining students
            if i <= remaining_students:
                class_size = students_per_class + 1
            else:
                class_size = students_per_class

            allocation[f"Class {i}"] = class_size
            assigned_students += class_size

        # Print the proposed allocation and the allocation dictionary
        print(f"Proposed Allocation: {num_classes} classes")
        print(allocation)

# Exception handling for non-numeric value
    except ValueError:
        print("Error: Invalid input. Please enter a numeric value for the number of students.")



