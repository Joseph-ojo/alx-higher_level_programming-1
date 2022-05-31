#!/usr/bin/python3
for i in range(0, 100):
    a, b = i // 10, i % 10
    if a < b:
        if i < 89:
            print(f"{i:d}", end=", ")
        else:
            print(f"{i:d}")
