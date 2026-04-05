import base64
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import pyperclip
import json
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend

class Base64Tool:
    def __init__(self):
        # Window setup
        self.root = ctk.CTk()
        self.root.title("Base64 & RSA Tool")
        self.root.geometry("500x700")
        self.root.resizable(False, False)
        
        # Center window on screen
        self.center_window()
        
        # Configure appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Create GUI elements
        self.create_widgets()
        
        self.private_key = None
        self.public_key = None
    
    def center_window(self):
        """Center the window on the screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_widgets(self):
        """Create all GUI widgets"""
        # Main container with padding
        main_frame = ctk.CTkFrame(self.root, corner_radius=10)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        title_label = ctk.CTkLabel(main_frame, text="Base64 & RSA Tool", 
                                 font=ctk.CTkFont(size=20, weight="bold"))
        title_label.pack(pady=(20, 10))
        
        # Tabview
        self.tabview = ctk.CTkTabview(main_frame)
        self.tabview.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Create tabs
        self.tabview.add("Base64")
        self.tabview.add("RSA")
        
        # Create Base64 tab content
        self.create_base64_tab()
        
        # Create RSA tab content
        self.create_rsa_tab()
    
    def create_base64_tab(self):
        """Create Base64 tab content"""
        base64_frame = self.tabview.tab("Base64")
        
        # Input section
        input_label = ctk.CTkLabel(base64_frame, text="Input", font=ctk.CTkFont(size=14, weight="bold"))
        input_label.pack(anchor="w", padx=10, pady=(10, 5))
        
        self.b64_input_text = ctk.CTkTextbox(base64_frame, height=120, font=ctk.CTkFont(size=12))
        self.b64_input_text.pack(fill="x", padx=10, pady=(0, 10))
        
        # Buttons section
        button_frame = ctk.CTkFrame(base64_frame)
        button_frame.pack(fill="x", padx=10, pady=5)
        
        self.encode_button = ctk.CTkButton(button_frame, text="Encode", command=self.encode_text,
                                          width=150, height=35, font=ctk.CTkFont(size=12, weight="bold"))
        self.encode_button.pack(side="left", expand=True, padx=(0, 5))
        
        self.decode_button = ctk.CTkButton(button_frame, text="Decode", command=self.decode_text,
                                          width=150, height=35, font=ctk.CTkFont(size=12, weight="bold"))
        self.decode_button.pack(side="right", expand=True, padx=(5, 0))
        
        # Error label
        self.error_label = ctk.CTkLabel(base64_frame, text="", text_color="red", 
                                       font=ctk.CTkFont(size=11))
        self.error_label.pack(pady=5)
        
        # Output section
        output_label = ctk.CTkLabel(base64_frame, text="Output", font=ctk.CTkFont(size=14, weight="bold"))
        output_label.pack(anchor="w", padx=10, pady=(10, 5))
        
        self.b64_output_text = ctk.CTkTextbox(base64_frame, height=120, font=ctk.CTkFont(size=12))
        self.b64_output_text.pack(fill="x", padx=10, pady=(0, 10))
        
        # Copy button
        self.copy_button = ctk.CTkButton(base64_frame, text="Copy to Clipboard", 
                                        command=self.copy_to_clipboard,
                                        width=200, height=35, font=ctk.CTkFont(size=12))
        self.copy_button.pack(pady=10)
    
    def create_rsa_tab(self):
        """Create RSA tab content"""
        rsa_frame = ctk.CTkScrollableFrame(self.tabview.tab("RSA"))
        rsa_frame.pack(fill="both", expand=True)
        
        # Key generation section
        key_frame = ctk.CTkFrame(rsa_frame)
        key_frame.pack(fill="x", padx=10, pady=10)
        
        self.generate_keys_button = ctk.CTkButton(key_frame, text="Generate RSA Keys", 
                                                  command=self.generate_rsa_keys,
                                                  width=200, height=35, font=ctk.CTkFont(size=12))
        self.generate_keys_button.pack(pady=10)
        
        # Key inputs section
        key_inputs_frame = ctk.CTkFrame(rsa_frame)
        key_inputs_frame.pack(fill="x", padx=10, pady=5)
        
        # Public key input
        pub_key_label = ctk.CTkLabel(key_inputs_frame, text="Public Key (for encryption):", 
                                     font=ctk.CTkFont(size=12, weight="bold"))
        pub_key_label.pack(anchor="w", padx=5, pady=(5, 2))
        
        self.public_key_text = ctk.CTkTextbox(key_inputs_frame, height=80, font=ctk.CTkFont(size=10))
        self.public_key_text.pack(fill="x", padx=5, pady=(0, 10))
        
        # Private key input
        priv_key_label = ctk.CTkLabel(key_inputs_frame, text="Private Key (for decryption):", 
                                      font=ctk.CTkFont(size=12, weight="bold"))
        priv_key_label.pack(anchor="w", padx=5, pady=(5, 2))
        
        self.private_key_text = ctk.CTkTextbox(key_inputs_frame, height=80, font=ctk.CTkFont(size=10))
        self.private_key_text.pack(fill="x", padx=5, pady=(0, 10))
        
        # RSA Input section
        rsa_input_label = ctk.CTkLabel(rsa_frame, text="Input Text", font=ctk.CTkFont(size=14, weight="bold"))
        rsa_input_label.pack(anchor="w", padx=10, pady=(10, 5))
        
        self.rsa_input_text = ctk.CTkTextbox(rsa_frame, height=80, font=ctk.CTkFont(size=12))
        self.rsa_input_text.pack(fill="x", padx=10, pady=(0, 10))
        
        # RSA Buttons
        rsa_button_frame = ctk.CTkFrame(rsa_frame)
        rsa_button_frame.pack(fill="x", padx=10, pady=5)
        
        self.encrypt_button = ctk.CTkButton(rsa_button_frame, text="Encrypt", 
                                           command=self.encrypt_with_rsa,
                                           width=150, height=35, font=ctk.CTkFont(size=12, weight="bold"))
        self.encrypt_button.pack(side="left", expand=True, padx=(0, 5))
        
        self.decrypt_button = ctk.CTkButton(rsa_button_frame, text="Decrypt", 
                                           command=self.decrypt_with_rsa,
                                           width=150, height=35, font=ctk.CTkFont(size=12, weight="bold"))
        self.decrypt_button.pack(side="right", expand=True, padx=(5, 0))
        
        # RSA Error label
        self.rsa_error_label = ctk.CTkLabel(rsa_frame, text="", text_color="red", 
                                           font=ctk.CTkFont(size=11))
        self.rsa_error_label.pack(pady=5)
        
        # RSA Output section
        rsa_output_label = ctk.CTkLabel(rsa_frame, text="Output", font=ctk.CTkFont(size=14, weight="bold"))
        rsa_output_label.pack(anchor="w", padx=10, pady=(10, 5))
        
        self.rsa_output_text = ctk.CTkTextbox(rsa_frame, height=120, font=ctk.CTkFont(size=12))
        self.rsa_output_text.pack(fill="x", padx=10, pady=(0, 10))
        
        # RSA Copy button
        self.rsa_copy_button = ctk.CTkButton(rsa_frame, text="Copy to Clipboard", 
                                            command=self.copy_rsa_to_clipboard,
                                            width=200, height=35, font=ctk.CTkFont(size=12))
        self.rsa_copy_button.pack(pady=10)
    
    def encode_text(self):
        """Encode the input text to Base64"""
        input_text = self.b64_input_text.get("1.0", "end-1c").strip()
        if not input_text:
            self.show_error("Please enter some text to encode")
            return
        
        try:
            encoded = base64.b64encode(input_text.encode()).decode()
            self.b64_output_text.delete("1.0", "end")
            self.b64_output_text.insert("1.0", encoded)
            self.hide_error()
        except Exception as e:
            self.show_error(f"Encoding error: {str(e)}")
    
    def decode_text(self):
        """Decode the Base64 input text"""
        input_text = self.b64_input_text.get("1.0", "end-1c").strip()
        if not input_text:
            self.show_error("Please enter some text to decode")
            return
        
        try:
            decoded = base64.b64decode(input_text.encode()).decode()
            self.b64_output_text.delete("1.0", "end")
            self.b64_output_text.insert("1.0", decoded)
            self.hide_error()
        except Exception:
            self.show_error("Fehler: Ungültiger Base64-String!")
    
    def copy_to_clipboard(self):
        """Copy output text to clipboard"""
        output_text = self.b64_output_text.get("1.0", "end-1c").strip()
        if not output_text:
            self.show_error("Nothing to copy")
            return
        
        try:
            pyperclip.copy(output_text)
            # Brief visual feedback
            original_text = self.copy_button.cget("text")
            self.copy_button.configure(text="Copied!")
            self.root.after(1000, lambda: self.copy_button.configure(text=original_text))
        except Exception as e:
            self.show_error(f"Failed to copy: {str(e)}")
    
    def show_error(self, message):
        """Show error message"""
        self.error_label.configure(text=message)
    
    def hide_error(self):
        """Hide error message"""
        self.error_label.configure(text="")
    
    def generate_rsa_keys(self):
        """Generate RSA key pair"""
        try:
            # Generate private key
            self.private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048,
                backend=default_backend()
            )
            self.public_key = self.private_key.public_key()
            
            # Serialize keys for display
            private_pem = self.private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ).decode()
            
            public_pem = self.public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ).decode()
            
            # Display keys in respective textboxes
            self.public_key_text.delete("1.0", "end")
            self.public_key_text.insert("1.0", public_pem)
            
            self.private_key_text.delete("1.0", "end")
            self.private_key_text.insert("1.0", private_pem)
            
            self.show_rsa_error("RSA keys generated successfully!")
        except Exception as e:
            self.show_rsa_error(f"Error generating keys: {str(e)}")
    
    def encrypt_with_rsa(self):
        """Encrypt input text with RSA public key"""
        input_text = self.rsa_input_text.get("1.0", "end-1c").strip()
        if not input_text:
            self.show_rsa_error("Please enter text to encrypt")
            return
        
        # Get public key from textbox
        public_key_pem = self.public_key_text.get("1.0", "end-1c").strip()
        if not public_key_pem:
            self.show_rsa_error("Please enter or generate a public key")
            return
        
        try:
            # Load public key
            public_key = serialization.load_pem_public_key(
                public_key_pem.encode(),
                backend=default_backend()
            )
            
            # Encrypt with RSA
            encrypted = public_key.encrypt(
                input_text.encode(),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            
            # Convert to base64 for display
            encrypted_b64 = base64.b64encode(encrypted).decode()
            
            # Update output
            self.rsa_output_text.delete("1.0", "end")
            self.rsa_output_text.insert("1.0", encrypted_b64)
            self.hide_rsa_error()
        except Exception as e:
            self.show_rsa_error(f"Encryption error: {str(e)}")
    
    def decrypt_with_rsa(self):
        """Decrypt input text with RSA private key"""
        input_text = self.rsa_input_text.get("1.0", "end-1c").strip()
        if not input_text:
            self.show_rsa_error("Please enter text to decrypt")
            return
        
        # Get private key from textbox
        private_key_pem = self.private_key_text.get("1.0", "end-1c").strip()
        if not private_key_pem:
            self.show_rsa_error("Please enter or generate a private key")
            return
        
        try:
            # Load private key
            private_key = serialization.load_pem_private_key(
                private_key_pem.encode(),
                password=None,
                backend=default_backend()
            )
            
            # Decode from base64
            encrypted_data = base64.b64decode(input_text.encode())
            
            # Decrypt with RSA
            decrypted = private_key.decrypt(
                encrypted_data,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            
            # Update output
            self.rsa_output_text.delete("1.0", "end")
            self.rsa_output_text.insert("1.0", decrypted.decode())
            self.hide_rsa_error()
        except Exception:
            self.show_rsa_error("Decryption error: Invalid encrypted text or wrong key!")
    
    def show_rsa_error(self, message):
        """Show RSA error message"""
        self.rsa_error_label.configure(text=message)
    
    def hide_rsa_error(self):
        """Hide RSA error message"""
        self.rsa_error_label.configure(text="")
    
    def copy_rsa_to_clipboard(self):
        """Copy RSA output text to clipboard"""
        output_text = self.rsa_output_text.get("1.0", "end-1c").strip()
        if not output_text:
            self.show_rsa_error("Nothing to copy")
            return
        
        try:
            pyperclip.copy(output_text)
            # Brief visual feedback
            original_text = self.rsa_copy_button.cget("text")
            self.rsa_copy_button.configure(text="Copied!")
            self.root.after(1000, lambda: self.rsa_copy_button.configure(text=original_text))
        except Exception as e:
            self.show_rsa_error(f"Failed to copy: {str(e)}")
    
    def run(self):
        """Start the application"""
        self.root.mainloop()

def main():
    app = Base64Tool()
    app.run()

if __name__ == "__main__":
    main()
