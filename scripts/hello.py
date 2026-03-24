# Day 44 simple test script

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    result = add_numbers(2, 3)
    print("Result:", result)

    assert result == 5, "Test failed: Expected 5"

    print("All tests passed successfully.")
