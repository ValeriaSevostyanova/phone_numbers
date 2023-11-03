import phonenumbers
from phonenumbers import geocoder, carrier, timezone

text = input("Example: 'Contact us at +919876543210 or +19697654321'\nInput Text: ")
numbers = phonenumbers.PhoneNumberMatcher(text, 'ru')
for n in numbers:
  print(n)

PhoneNumber = phonenumbers.parse(input('Your PhoneNumber: '))
Carrier = carrier.name_for_number(PhoneNumber, 'ru')
Region = geocoder.description_for_number(PhoneNumber, 'ru')
TimeZone = timezone.time_zones_for_number(PhoneNumber)

print(f'Carrier: {Carrier},\nRegion: {Region},\nTimeZone: {TimeZone},\n{PhoneNumber}')
print(f'Number is Valid: {phonenumbers.is_valid_number(PhoneNumber)},\nNumber is Possible: {phonenumbers.is_possible_number(PhoneNumber)}')