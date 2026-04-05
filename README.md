# Base64 & RSA Tool

> A lightweight desktop application for Base64 encoding/decoding and RSA encryption/decryption with a clean dark-mode interface.

## 🚀 Features

- 🎨 **Modern Dark UI** - Built with CustomTkinter
- 🔐 **Base64 Operations** - Quick encoding and decoding
- 🔑 **RSA Encryption** - 2048-bit key generation and cryptography
- 📋 **Clipboard Integration** - One-click copy functionality
- ⚡ **Zero Dependencies** - Single .exe file, no installation
- 🛡️ **Error Handling** - User-friendly error messages
- 📜 **Scrollable Interface** - Compact window with scrollable RSA tab

## 📥 Download

Get the latest version from [Releases](https://github.com/lukh2010/base64-en-decoder/releases)

### Quick Start Options

#### 🎯 Option 1: Direct Download (Recommended)
1. Go to [Releases](https://github.com/lukh2010/base64-en-decoder/releases)
2. Download `en_decoder.exe`
3. Double-click to run - no installation needed!

#### 🔧 Option 2: Build from Source (Advanced)
1. Clone this repository
2. Run `build.bat` to create your own executable
3. Find your build in `dist/en_decoder.exe`

## 💻 Usage

### Base64 Tab
1. Enter your text in the input field
2. Click **Encode** to convert to Base64 or **Decode** to convert back
3. Copy the result with **Copy to Clipboard**

### RSA Tab
1. Click **Generate RSA Keys** to create a new key pair
2. The public key appears in the "Public Key" field (share this for encryption)
3. The private key appears in the "Private Key" field (keep this secret for decryption)
4. Enter text to encrypt/decrypt in the "Input Text" field
5. Click **Encrypt** (uses public key) or **Decrypt** (uses private key)
6. Copy the result from the "Output" field

### Key Management
- **Generate Keys**: Creates a new 2048-bit RSA key pair
- **Public Key**: Share with others for them to encrypt messages to you
- **Private Key**: Keep secret - only you can decrypt messages with this
- **Manual Input**: You can also paste existing keys into the respective fields

## 🔧 Development

### Prerequisites
- Python 3.11+
- Windows OS (for .exe build)

### Local Development Setup
```bash
# Clone the repository
git clone https://github.com/lukh2010/base64-en-decoder.git
cd base64-en-decoder

# Install dependencies
pip install -r requirements.txt

# Run the application in development mode
python b64_tool.py

# Build executable for local testing
build.bat
```

### Project Structure
```
base64-en-decoder/
├── b64_tool.py          # Main application code
├── requirements.txt     # Python dependencies
├── build.bat            # Build script for Windows
├── README.md            # This file
├── .github/
│   └── workflows/
│       └── release.yml  # CI/CD pipeline
└── .gitignore          # Git ignore patterns
```

**Note for Developers**: The `build.bat` script is included in the repository for easy local development and testing. Only build artifacts (`dist/`, `build/`, `*.spec`) are excluded from git.

##  Deployment

**Important**: Regular commits to `main` branch do NOT trigger releases. 
Only pushing version tags (e.g., `v1.0.0`) will create a new release.

## 📦 Tech Stack

- **UI Framework**: CustomTkinter - Modern dark-mode interface
- **Cryptography**: Python cryptography library with RSA-2048 support
- **Encoding**: Built-in base64 module for reliable encoding/decoding
- **Clipboard**: pyperclip for cross-platform clipboard access
- **Packaging**: PyInstaller for creating standalone executables
- **CI/CD**: GitHub Actions for automated builds and releases

## 🔒 Security Notes

### RSA Implementation
- Uses **2048-bit RSA keys** - sufficient for educational purposes
- Implements **OAEP padding** with SHA-256 for secure encryption
- Keys are generated using Python's cryptography library
- No keys are stored permanently - generated in memory only

### Best Practices
- **Public Keys**: Safe to share, used only for encryption
- **Private Keys**: Keep secret, used for decryption only
- **Key Storage**: Consider using a password manager for long-term key storage
- **Production Use**: This tool is educational - use established libraries for production systems

## 🐛 Troubleshooting

### Common Issues

#### "Executable not found"
- Ensure you're in the correct directory
- Check that `en_decoder.exe` exists in the `dist/` folder
- Try rebuilding with `build.bat`

#### "RSA encryption fails"
- Make sure you have a public key in the Public Key field
- Try generating new keys with "Generate RSA Keys"
- Check that your input text isn't empty

#### "Base64 decode fails"
- Ensure the text is valid Base64 format
- Check for extra spaces or newlines
- Try encoding first to verify the format

#### Clipboard issues
- Ensure no other application is blocking clipboard access
- Try restarting the application
- Check system clipboard permissions

### Getting Help
1. Check this troubleshooting section
2. Search existing [Issues](https://github.com/lukh2010/base64-en-decoder/issues)
3. Create a new issue with:
   - Your operating system
   - Steps to reproduce
   - Error messages (if any)

## 📝 License

Open source - feel free to contribute or fork!

### Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

**⚠️ Important Notice**: This tool is for educational purposes. For production security needs, always use well-established, audited cryptographic libraries and follow security best practices. The developers are not responsible for any security incidents resulting from the use of this tool.
