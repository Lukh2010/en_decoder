import base64
import sys

def main():
    while True:
        print("\n--- Base64 Tool (Tippe 'exit' zum Beenden) ---")
        mode = input("Möchtest du (e)ncoden, (d)ecoden? ").lower()
        if mode == 'exit':
            break
        
        if mode not in ['e', 'd']:
            print("Ungültige Auswahl.")
            continue
        
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

if __name__ == "__main__":
    main()