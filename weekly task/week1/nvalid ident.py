n = int(input("Enter the length of identifiers: "))

first_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
other_chars = first_chars + '0123456789'

if n < 1:
    print("Length must be at least 1")
else:
    stack = [("", 0)]

    while stack:
        current, length = stack.pop()

        if length == n:
            print(current)
        else:
            chars = first_chars if length == 0 else other_chars
            for ch in reversed(chars):
                stack.append((current + ch, length + 1))
