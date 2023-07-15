import hashlib

def SHA1(num1):
    result = hashlib.sha1(num1.encode('utf-8')).hexdigest()
    return result

def SHA256(num1):
    result = hashlib.sha256(num1.encode('utf-8')).hexdigest()
    return result

def SHA3(num1):
    result = hashlib.sha3_512(num1.encode('utf-8')).hexdigest()
    return result

def BLAKE2B(num1):
    result = hashlib.blake2b(num1.encode('utf-8')).hexdigest()
    return result

print('-=' * 20)
print(f'{"HASH GENERATOR" :^40}')
print('-=' * 20)
print()
num1 = str(input('Insert your text, after press ENTER: '))
while True:
    print('Choose a hash to encrypt your file\n'
          '[1] SHA1\n'
          '[2] SHA256\n'
          '[3] SHA3_512\n'
          '[4] BLAKE2B\n')
    option = int(input('Press a number in menu relative your choose: '))
    if option == 1:
       result = SHA1(num1)
       print(f'The result in SHA1 is: {result}')
       cont = str(input('Do you want continue ? [Y/N] ')).upper()
       if cont in 'N':
           break
       else:
         num1 = str(input('Insert your text, after press ENTER: '))
    elif option == 2:
        result = SHA256(num1)
        print(f'The result in SHA256 is: {result}')
        cont = str(input('Do you want continue ? [Y/N] ')).upper()
        if cont in 'N':
            break
        else:
            num1 = str(input('Insert your text, after press ENTER: '))
    elif option == 3:
        result = SHA3(num1)
        print(f' The result in SHA3_512 is: {result}')
        cont = str(input('Do you want continue ? [Y/N] ')).upper()
        if cont in 'N':
            break
        else:
            num1 = str(input('Insert your text, after press ENTER: '))
    elif option == 4:
        result = BLAKE2B(num1)
        print(f'The result in BLAKE2B is: {result}')
        cont = str(input('Do you want continue ? [Y/N] ')).upper()
        print()
        if cont in 'N':
            break
        else:
            num1 = str(input('Insert your text, after press ENTER: '))
print()
print('=' * 10, 'Thank you for choosing us !!!', '=' * 10)
