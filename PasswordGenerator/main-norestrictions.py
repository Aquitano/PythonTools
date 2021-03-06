import requests, string, random

characters = [char for char in string.printable]
remove = ['\n', '\r','\t','\x0b','\x0c']
characters = [elem for elem in characters if elem not in remove]

def checkquota():
    r_url = 'https://www.random.org/quota/?format=plain'
    quota = int(requests.get(r_url).text)
    if quota < 1:
        raise Exception('Quota used up!')
    return quota

def get_random_numbers(num):
    checkquota()
    numbers = requests.get('https://www.random.org/integers/?num={}&min=0&max={}&col=1&base=10&format=plain&rnd=new'.format(
        num, len(characters) -1
    )).text.split('\n')
    numbers.remove('')
    return numbers

def generate_pwd(num):
    pwd = ''
    random.shuffle(characters)
    numbers = get_random_numbers(num)
    for number in numbers:
        pwd += characters[int(number)]
    "".join(pwd.split())
    print(pwd)

psw_length = input('Enter password length: ')

generate_pwd(psw_length)
