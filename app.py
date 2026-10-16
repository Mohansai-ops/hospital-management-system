def add_patient(name, age):
    if not name:
        raise ValueError("Patient name is required")
    if age <= 0:
        raise ValueError("Age must be positive")
    return {"name": name, "age": age}


if __name__ == "__main__":
    patient = add_patient("Ravi", 25)
    print("Patient registered successfully:", patient)
