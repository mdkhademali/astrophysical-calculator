import math

def calculate_luminosity():
    print("\nLuminosity Calculation (Stefan-Boltzmann Law)")
    radius = float(input("Enter the radius of the star (in meters): "))
    temperature = float(input("Enter the surface temperature of the star (in Kelvin): "))
    sigma = 5.670374419e-8  # Stefan-Boltzmann constant
    luminosity = 4 * math.pi * radius**2 * sigma * temperature**4
    print(f"Luminosity of the star: {luminosity:.2e} watts\n")

def calculate_gravitational_force():
    print("\nGravitational Force Calculation (Newton's Law of Gravitation)")
    mass1 = float(input("Enter the mass of the first object (in kg): "))
    mass2 = float(input("Enter the mass of the second object (in kg): "))
    distance = float(input("Enter the distance between the objects (in meters): "))
    G = 6.67430e-11  # Gravitational constant
    force = G * mass1 * mass2 / distance**2
    print(f"Gravitational force: {force:.2e} newtons\n")

def calculate_escape_velocity():
    print("\nEscape Velocity Calculation")
    mass = float(input("Enter the mass of the celestial body (in kg): "))
    radius = float(input("Enter the radius of the celestial body (in meters): "))
    G = 6.67430e-11  # Gravitational constant
    velocity = math.sqrt(2 * G * mass / radius)
    print(f"Escape velocity: {velocity:.2f} m/s\n")

def display_copyright():
    print("""
Astrophysical Calculator
(c) 2024 Khadem Ali
Contact: https://github.com/mdkhademali
    """)

def main():
    while True:
        print("\nAstrophysical Calculator")
        print("1. Calculate Luminosity of a Star")
        print("2. Calculate Gravitational Force")
        print("3. Calculate Escape Velocity")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            calculate_luminosity()
        elif choice == "2":
            calculate_gravitational_force()
        elif choice == "3":
            calculate_escape_velocity()
        elif choice == "4":
            print("Exiting Astrophysical Calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    # Display copyright only once
    display_copyright()
    main()