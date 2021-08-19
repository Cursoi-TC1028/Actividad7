# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    (
        # Inputs
        ["-8"],
        # Outputs
        ["Dame un número: ", "Par negativo"],
        # Error message
        "Revisa la condición y la indentación. Revisa el signo"
    ),
    (
        # Inputs
        ["-31"],
        # Outputs
        ["Dame un número: ", "Impar negativo"],
        # Error message
        "Revisa la condición y la indentación. Revisa el signo"
    ),
    (
        # Inputs
        ["31"],
        # Outputs
        ["Dame un número: ", "Impar positivo"],
        # Error message
        "Revisa la condición y la indentación. Revisa el signo"
    ),
    (
        # Inputs
        ["30"],
        # Outputs
        ["Dame un número: ", "Par positivo"],
        # Error message
        "Revisa la condición y la indentación. Revisa el signo"
    )
    ]