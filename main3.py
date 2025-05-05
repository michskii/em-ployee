class Vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def fare(self):
        total_fare = super().fare()
        total_fare += total_fare * 0.1
        return total_fare


# Example usage
if __name__ == "__main__":
    school_bus = Bus("School Bus", 50)
    print(f"Total Bus Fare: {school_bus.fare()}")