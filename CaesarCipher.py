def encrypt_text(plaintext, n):
    ans = ""
    
    for i in range(len(plaintext)):
        ch = plaintext[i]

        # check if space is there, then simply add space
        if ch == " ":
            ans += " "
        # check if a character is uppercase 
        elif ch.isupper():
            ans += chr((ord(ch) + n - 65) % 26 + 65)
        # check if a character is lowercase 
        else:
            ans += chr((ord(ch) + n - 97) % 26 + 97)

    return ans

# Take input from the user for plaintext and shift pattern (n)
plaintext = input("Enter the plaintext: ")
n = int(input("Enter the shift pattern: "))

print("-------------PIZZA PIZZA----------------")
print("Cipher Text is : " + encrypt_text(plaintext, n))
