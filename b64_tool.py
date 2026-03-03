import base64
import sys

def main():
    print("--- Base64 Tool ---")
    mode = input("Möchtest du (e)ncoden oder (d)ecoden? ").lower()
    text = input("Gib den Text ein: ")

    if mode == 'e':
        encoded = base64.b64encode(text.encode()).decode()
        print(f"Ergebnis: {encoded}")
    elif mode == 'd':
        try:
            decoded = base64.b64decode(text.encode()).decode()
            print(f"Ergebnis: {decoded}")
        except Exception:
            print("Fehler: Ungültiger Base64-String!")
    else:
        print("Ungültige Auswahl.")

if __name__ == "__main__":
    main()