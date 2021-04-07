import termcolor
import colorama

colorama.init(strip="False") #for pycharm's console to return colors and not weird symbols
print("To server: ", end="")
print(termcolor.colored("Message", "yellow"))