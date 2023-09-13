import string

Letters = string.ascii_lowercase

# input field for the encryoted message, inputting "lower" makes it so it treats uppercase letters as lowercase
message = input("Enter the encrypted message: ").lower() 

for key in range(len(Letters)):
   translated = ''
   for ch in message:
      if ch in Letters:
         num = Letters.find(ch)
         num = num - key
         if num < 0:
            num = num + len(Letters)
         translated = translated + Letters[num]
      else:
         translated = translated + ch
   print('Decryption key is %s: %s' % (key, translated))
