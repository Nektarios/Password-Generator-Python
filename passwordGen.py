import string
import random
characters = string.ascii_letters + string.punctuation + string.digits + "αβγδεζηθικλμνξοπρστυφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩάέήίόύώΆΈΉΊΌΎΏ" + "!@#$%^&*()_+"
filename = "passwords.txt"

website = input("[WEBSITE] Where are you going to use this password? ")
user = input("[USER/EMAIL] Please type the name or the email you entered to register: ")

password = "".join(random.choice(characters) for x in range(random.randint(4, 8)))
print("You can now use this password ( " + password + " ) at " + website + "")


f = open("passwords.txt", "w+", encoding="utf-8")
f.write("Website: " + website + " | Username/Email: " + user + " | Password: " + password + '\n')
f.close()

print("Data have been saved successfully to file.")