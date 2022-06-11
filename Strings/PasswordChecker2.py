"""A password is said to be strong if it satisfies all the following criteria:

It has at least 8 characters.
It contains at least one lowercase letter.
It contains at least one uppercase letter.
It contains at least one digit.
It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).
Given a string password, return true if it is a strong password. Otherwise, return false."""


def strongPasswordCheckerII(password: str) -> bool:

    special = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+"]

    count_char = len(password)
    lower_count = 0
    upper_count = 0
    digit_count = 0
    special_count = 0
    is_adjacted = False

    for i in range(count_char):
        if password[i].islower():
            lower_count += 1
        if password[i].isupper():
            upper_count += 1
        if password[i].isdigit():
            digit_count += 1
        if password[i] in special:
            special_count += 1

    for i in range(count_char - 1):
        if password[i] == password[i + 1]:
            is_adjacted = True

    if (
        count_char >= 8
        and lower_count >= 1
        and upper_count >= 1
        and digit_count >= 1
        and special_count >= 1
        and is_adjacted == False
    ):
        return True
    return False


password = "11A!A!Aa"
print(strongPasswordCheckerII(password))
