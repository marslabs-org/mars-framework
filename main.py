import mars_core

def main():
    print("Testing C++ Core Engine via Python:")
    print(f"10 + 5 = {mars_core.add(10, 5)}")
    print(f"10 - 5 = {mars_core.subtract(10, 5)}")
    print(f"10 * 5 = {mars_core.multiply(10, 5)}")
    print(f"10.0 / 5.0 = {mars_core.divide(10.0, 5.0)}")

if __name__ == "__main__":
    main()
