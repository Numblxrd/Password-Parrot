import random
import pyperclip

print(r'''
   
 █▀█ ▄▀█ █▀ █▀ █░█░█ █▀█ █▀█ █▀▄   █▀█ ▄▀█ █▀█ █▀█ █▀█ ▀█▀
 █▀▀ █▀█ ▄█ ▄█ ▀▄▀▄▀ █▄█ █▀▄ █▄▀   █▀▀ █▀█ █▀▄ █▀▄ █▄█ ░█░
 
                         __,---.
                        /__|o\  )
                         `-\ / /
                           ,) (,
                          //   \\
                         {(     )}
                   =======""===""=======
                           |||||
                            |||
                             |
      
              [Just A Simple Password Generator]
                        [By Numblxrd]
''')

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWQYZ1234567890!@#$%^&*?'

def generate_a_password():

    password = ''.join([random.choice(characters) for _ in range(how_many)])

    return password

while True:

  how_many = int(input('\nHow Many Characters You Want For Password? '))

  generated_password = generate_a_password()

  print('\n--->',generated_password)

  pyperclip.copy(generated_password)

  print('\nThe Password Copied To Your Clipboard!\n')

  print('----------------------------------------')
