import pyfiglet
name=input("Enter a  Your Name:-")
print("========================")
print("banner2-D")
print("Doom")
print("Digital")
print("Diamond")
print("epic")

font_style=input("Choose Your Font Style:-")
font=pyfiglet.figlet_format(f"{name}",f"{font_style}")
print(font)