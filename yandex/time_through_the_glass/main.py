if __name__ == "__main__":
    h, m = map(int, input().split())

    print(abs(h - 12) % 12, abs(m - 60) % 60)
