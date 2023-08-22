import random

def pattern_1(rows):
    for i in range(1, rows + 1):
        print('* ' * i)

def pattern_2(rows):
    for i in range(rows, 0, -1):
        print('* ' * i)

def pattern_3(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '* ' * i)

def pattern_4(rows):
    for i in range(rows, 0, -1):
        print(' ' * (rows - i) + '* ' * i)

def main():
    rows = int(input("Enter the number of rows: "))
    pattern_functions = [pattern_1, pattern_2, pattern_3, pattern_4]
    selected_pattern = random.choice(pattern_functions)
    
    print("Generated pattern:")
    selected_pattern(rows)

if __name__ == "__main__":
    main()
