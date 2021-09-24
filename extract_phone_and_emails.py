
import re, pyperclip

# TODO: Create a regex for phone number

Phone_regex = re.compile(r'''
# 315-123-2143, 444-0000, (321) 455-0994
(
(\d\d\d | (\d\d\d) | (\(\d\d\d))?        # are code ( optional )
(\s|-)                  # first separator
\d\d\d                  # first 3 digits
-                       # separator
\d\d\d\d                # last 4 digits
)
''', re.VERBOSE)

# TODO: Create a regex for email

email_regex = re.compile(r'''
# some)>+thjing@gmail.com
[a-zA-z0-9_.+]+       # name part
@                     # @symbol
[a-zA-z0-9_.+]+       # domain name part

''', re.VERBOSE)

# TODO: get the data of the clipboard

data = pyperclip.paste()

# TODO: Extract phone numbers and emails from data

extract_phone = Phone_regex.findall(data)
extract_mail_wd = email_regex.findall(data)

#print(extract_phone)
#print(extract_mail_wd)

# TODO: Extract from tuples the hole phone numbers and append to new list
# Remove duplicates of phone numbers

phone_numbers = list()
for phone_number in extract_phone:
    if phone_number not in phone_numbers:
        phone_numbers.append(phone_number[0])
print(phone_numbers)

# Remove the duplicates from the exctact_mail_wd
# "wd" stands for "with duplicates"

extract_mail = set(extract_mail_wd)

extracted_data = '===PHONE NUMBERS===\n' + '\n'.join(phone_numbers) + '\n' + '===EMAILS===\n' + '\n'.join(extract_mail)
pyperclip.copy(extracted_data)

# If you want to import all the extracted data into a txt file you can run line:

data_file = open("C:\\Users\\alexp\\Documents\\data_file.txt", 'a') # here you have to change the path for your txt file.
data_file.write(pyperclip.paste())
