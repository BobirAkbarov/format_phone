def format_phone(num: str):
    return "{}{}{}{}({}{}) {}{}{}-{}{}-{}{}".format(*list(num))
print(format_phone('+998935656328'))