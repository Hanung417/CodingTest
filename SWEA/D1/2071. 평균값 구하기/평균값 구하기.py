T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    total = 0  
    for num in arr:
        total += num
    average = total / 10
    print(f"#{test_case} {round(average)}")