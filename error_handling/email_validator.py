class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


email = input()

while email != 'End':
    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")
    if len(email[:email.index('@')]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")
    if email[email.index('.')::] not in ('.com', '.bg', '.org', '.net'):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org,.net")
    email = input()

# peter@gmail.com
# petergmail.com