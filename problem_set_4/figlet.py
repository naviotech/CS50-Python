'''
FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 1990s for making 
large letters out of ordinary text, a form of ASCII art:

 _ _ _          _   _     _
| (_) | _____  | |_| |__ (_)___
| | | |/ / _ \ | __| '_ \| / __|
| | |   <  __/ | |_| | | | \__ \
|_|_|_|\_\___|  \__|_| |_|_|___/
Among the fonts supported by FIGlet are those at figlet.org/examples.html.

FIGlet has since been ported to Python as a module called pyfiglet.

In a file called figlet.py, implement a program that:

Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case the first of the two should 
be -f or --font, and the second of the two should be the name of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or the second is 
not the name of a font, the program should exit via sys.exit with an error message.
'''
import sys
import pyfiglet

# Lista de fuentes admitidas
fuentes_admitidas = pyfiglet.FigletFont.getFonts()

def main():
    if len(sys.argv) == 1:
        # Generar texto en una fuente aleatoria
        texto = input("Escribe un texto: ")
        font = pyfiglet.Figlet()
        resultado = font.renderText(texto)
        print(resultado)
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        # Generar texto en una fuente específica
        font_name = sys.argv[2]
        if font_name in fuentes_admitidas:
            texto = input("Escribe un texto: ")
            try:
                font = pyfiglet.Figlet(font=font_name)
                resultado = font.renderText(texto)
                print(resultado)
            except pyfiglet.FontNotFound:
                print(f"Error: La fuente '{font_name}' no existe.")
                sys.exit(1)
        else:
            print(f"Error: La fuente '{font_name}' no está en la lista de fuentes admitidas.")
            sys.exit(1)
    else:
        print("Uso incorrecto. Debes proporcionar cero o dos argumentos de línea de comando.")
        sys.exit(1)

if __name__ == "__main__":
    main()