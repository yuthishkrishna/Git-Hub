def verify_card_number(digits):
    digits = digits.replace(" ", '').replace('-', '')
    if not digits.isdigit():
        return "INVALID!"
    digits = [int(d) for d in digits]
    total = 0
    for i in range(len(digits) - 2, -1, -2):
        doubled = digits[i] * 2
        if doubled > 9:
            doubled -= 9
        digits[i] = doubled
    total = sum(digits)
    if total % 10 != 0:
        return "INVALID!"
    return "VALID!"