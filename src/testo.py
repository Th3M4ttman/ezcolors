from ezcolors.Colors import choice, LCyan, cBool, ColoredException, LPurple

x = choice("Do you want", ("Anal", "Vaginal", "oral"), short=False, return_choice=True)
print(x)
print(cBool(LCyan.name != "Light Cyan"))

