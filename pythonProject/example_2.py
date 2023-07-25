def evens_odds(num):
    odd = 0
    even = 0
    for i in range(num):
        if i % 2 == 0:
            even = even + 1
        elif i%2 != 0:
            odd = odd +1
    print(even)
    print(odd)


print(evens_odds(11))