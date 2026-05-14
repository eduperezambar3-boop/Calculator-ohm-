
### Defino funciones para el calculo de voltaje, corriente y resistencia usando la ley de ohm ### 

def calculate_voltage(current, resistance):  
    """calcula el voltaje usando la ley de ohm: V = I * R"""
    return current * resistance


def calculate_current(voltage, resistance):
    """calcula la corriente usando la ley de ohm: I = V / R"""
    if resistance == 0: ## Control de error R>0.  
        raise ValueError("Resistance cannot be zero.") 
    return voltage / resistance


def calculate_resistance(voltage, current):
    """calcula la resistencia usando la ley de ohm: R = V / I"""
    if current == 0: ## Control de error I>0.  
        raise ValueError("Current cannot be zero.") 
    return voltage / current


### Esta parte del código se encarga de validar que el usuario ingrese un número válido para los cálculos ### 


def get_float(prompt):
    while True:
        User_imput = input(prompt)  
        try:
            return float(User_imput)
        except ValueError:
            print("Invalid input. Please enter a number.") 



### Función para guardar el historial de cálculos en un archivo de texto ###    

def save_history(text):
    """Guarda el historial de cálculos en un archivo de texto llamado history.txt. Cada cálculo se guarda en una nueva línea."""
    with open("history.txt", "a") as f:  ## se utiliza with para asegurar que el archivo se cierre correctamente después de escribir en él. El modo "a" (append) se utiliza para agregar texto al final del archivo sin sobrescribir su contenido.
        f.write(text + "\n")



### Ejecuciopn principal del programa ###   

def main():
    """La funcion main realiza un bucle permitiendo al usuario elegir qué cálculo realizar (voltaje, corriente o resistencia) y luego solicita los valores necesarios para realizar el cálculo. El resultado se muestra al usuario y se guarda en el historial."""
    print("Welcome to the Ohm's Law Calculator!")

    while True:
        print("\nChoose an option:")
        print("V - Voltage")
        print("I - Current")
        print("R - Resistance")
        print("Q - Quit")

        choice = input("Your choice: ").upper()

        try:
            if choice == 'V':
                current = get_float("Enter current (I): ")
                resistance = get_float("Enter resistance (R): ")
                voltage = calculate_voltage(current, resistance)
                result = f"V = {current} * {resistance} = {voltage}"
                print("Voltage:", voltage)
                save_history(result)

            elif choice == 'I':
                voltage = get_float("Enter voltage (V): ")
                resistance = get_float("Enter resistance (R): ")
                current = calculate_current(voltage, resistance)
                result = f"I = {voltage} / {resistance} = {current}"
                print("Current:", current)
                save_history(result)

            elif choice == 'R':
                voltage = get_float("Enter voltage (V): ")
                current = get_float("Enter current (I): ")
                resistance = calculate_resistance(voltage, current)
                result = f"R = {voltage} / {current} = {resistance}"
                print("Resistance:", resistance)
                save_history(result)

            elif choice == 'Q':
                print("Exiting program...")
                break

            else:
                print("Invalid option. Try again.")

        except ValueError as e:
            print("Error:", e)


if __name__ == "__main__":
    main()

