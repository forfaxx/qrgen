## `qrgen.py` – Simple QR Code Generator for the Command Line

Generate QR codes instantly from the terminal.
No accounts. No ads. No browser required.


### 🔧 Features

* Accepts direct text or piped input
* Saves images in PNG, JPG, or GIF format (based on --output file extension)
* Output to a directory? Defaults to output.png inside that folder
* Prints QR code as ASCII (`--ascii`)
* Interactive prompt fallback if no input is given
* Share Wi-Fi passwords, OTP secrets, URLs, or any text as a QR code—right from your shell
* Simple and private—never sends your data anywhere
---

## 🚀 Quickstart 

1. Clone this repo and enter the folder: 
```bash
git clone https://github.com/forfaxx/qrgen.git
cd qrgen
```
2. Create a virtual environment and activate it:
```bash
python3 -m venv venv
source venv/bin/activate

```

3. Install requirements
```bash
pip install -r requirements.txt
```

4. Run the tool: 
```bash
python3 qrgen.py "hello from qrgen"
echo "https://adminjitsu.com" | python3 qrgen.py 
```

---

## 🧙‍♂️  Optional: Shell Wrapper for Convenience

If you use a lot of Python CLI tools (especially ones with venvs or asset files), activating the environment and running the script each time can be a real pain:

    Tedious: cd project && source venv/bin/activate && python tool.py

    Easy to forget, so you don’t use the tool as much

With venv-launch.sh and a tiny shell wrapper, you can launch your tool from anywhere with one command—no cd, no manual venv activate, no fuss. Just an extra configuration step and you can launch your complex python scripts with a single command!

This technique will work with any complex python script that requires its own folder and environment. 

1. Put venv-launch.sh somewhere in your PATH (e.g., `~/bin`):
```bash
cp venv-launch.sh ~/bin/
chmod +x ~/bin/venv-launch.sh

```
2. Create a wrapper script for qrgen: 
In ~/bin (or another place in your PATH), put this:

```bash
#!/usr/bin/env bash
# qrgen global launcher

SCRIPT_DIR="$HOME/tools/qrgen"   # <--- change this to wherever you cloned the repo

exec ~/bin/venv-launch.sh "$SCRIPT_DIR/qrgen.py" "$@"
```

3. Make the launcher executable: 
```bash
chmod +x ~/bin/qrgen
```

4. Now you can run: 
```bash
qrgen "https://adminjitsu.com" 
echo "my wifi password" | qrgen --ascii
```

---



## Usage Examples


```bash
# Encode direct string and open QR image
./qrgen.py "https://darkstar.home"

# Pipe text into it and save to file
echo "ssh grumble@bomb20.darkstar.home" | ./qrgen.py --output ssh.png

# Save as PNG
./qrgen.py "https://darkstar.home" --output darkstar.png

# Save as high-quality JPEG (web-optimized)
./qrgen.py "https://darkstar.home" --output darkstar.jpg

# Save to a directory (outputs 'output.png' in dir)
./qrgen.py "https://darkstar.home" --output /tmp/

# Show ASCII art version in terminal
./qrgen.py --ascii "Hello from the shell"

# No arguments? It'll prompt you interactively
./qrgen.py
```

---

## 🧰 Dependencies

* [`qrcode`](https://pypi.org/project/qrcode/)
* [`Pillow`](https://pypi.org/project/Pillow/) (for image rendering)

Install with: 

```bash
pip install -r requirements.txt
```

## License
MIT License – see [LICENSE](LICENSE)


## Conclusion
Written by Kevin Joiner, 2025. 
PRs, feature ideas, and hacks welcome! 