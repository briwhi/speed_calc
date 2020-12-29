distance = int(input("Distance in miles: "))
speeds = [55, 60, 65, 70, 75, 80]
for speed in speeds:
    print(f"{speed} mph: {round(speed/60,2)} hours")
