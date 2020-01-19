import sys, webbrowser, pyperclip

if len(sys.argv) > 1:
    # Get the address from the command line
    address = '+'.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open(f'https://www.google.ro/maps/place/{address}')

