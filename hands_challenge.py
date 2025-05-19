def get_positions(n):
    return (n % 3, n % 9 // 3, n % 27 // 9)

if __name__ == "__main__":
    print(get_positions(5))