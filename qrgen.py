#!/usr/bin/env python3
"""
qrgen.py — a friendly QR code CLI tool
"""

import sys
import argparse
import qrcode
import os
from io import StringIO

VERSION = "qrgen.py 1.1.0"

def read_stdin():
    if not sys.stdin.isatty():
        return sys.stdin.read().strip()
    return None

def generate_qr(data, output=None, show_ascii=False):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=4,
        border=1,
    )
    qr.add_data(data)
    qr.make(fit=True)

    if show_ascii:
        qr.print_ascii()
        return

    img = qr.make_image(fill_color="black", back_color="white")

    if output:
        output = os.path.expanduser(output)
        # If output is a directory, write output.png there
        if os.path.isdir(output):
            output_file = os.path.join(output, "output.png")
            fmt = "PNG"
        else:
            output_file = output
            _, ext = os.path.splitext(output_file)
            ext = ext.lower()
            if ext in [".png"]:
                fmt = "PNG"
            elif ext in [".jpg", ".jpeg"]:
                fmt = "JPEG"
            elif ext in [".gif"]:
                fmt = "GIF"
            else:
                # Default to PNG if unknown extension
                fmt = "PNG"
                output_file += ".png"

        img_to_save = img
        save_kwargs = {}

        # For JPEG, must ensure mode is correct
        if fmt == "JPEG":
            img_to_save = img.convert("1")  # B/W, sharp
            save_kwargs = dict(quality=100, subsampling=0, optimize=True)
        elif fmt == "PNG":
            img_to_save = img.convert("1")  # Ensure 1-bit
            save_kwargs = dict(optimize=True)
        elif fmt == "GIF":
            img_to_save = img.convert("1")  # GIF needs palette
            save_kwargs = {}

        img_to_save.save(output_file, fmt, **save_kwargs)
        print(f"💾 Saved QR to {output_file}")

    else:
        img.show()

def main():
    parser = argparse.ArgumentParser(description="Generate a QR code from text.")
    parser.add_argument("text", nargs="?", help="Text to encode")
    parser.add_argument("-o", "--output", help="Output image file (e.g., out.png)")
    parser.add_argument("-a", "--ascii", action="store_true", help="Print QR as ASCII")
    parser.add_argument("-v", "--version", action="store_true", help="Show version and exit")

    # For help2man: ensure --help shows usage and exits cleanly (before parsing)
    if "--help" in sys.argv or "-h" in sys.argv:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    if args.version:
        print(VERSION)
        sys.exit(0)

    text = args.text or read_stdin()

    if not text:
        if sys.stdin.isatty():
            try:
                text = input("📶 Enter text to encode as QR: ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\n❌ Canceled by user.")
                sys.exit(0)
            if not text:
                print("⚠️  No input provided.")
                sys.exit(1)
        else:
            print("❌ No input detected.", file=sys.stderr)
            sys.exit(1)

    if args.ascii:
        generate_qr(text, show_ascii=True)
    else:
        generate_qr(text, output=args.output)

if __name__ == "__main__":
    main()
