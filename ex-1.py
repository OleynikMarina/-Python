import re

def email_parse(email_address):

    compile_name = re.compile(r'(?P<username>[a-zA-Z0-9._-]+)[@](?P<domain>\w+[.]\w+)')
    parsed = re.match(compile_name, email_address)
    if not parsed:
        raise ValueError(f"wrong email: {email_address}")
    return parsed.groupdict()


print(email_parse('marina.oleynik@mail.ru'))
print(email_parse('marina.oleynik1996@gmail.com'))
print(email_parse('marina.oleynik@mailru'))
