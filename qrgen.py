#!/usr/bin/env python3
"""
qrgen.py — a friendly QR code CLI tool
"""

import sys
import argparse
import qrcode
from io import StringIO

VERSION = "qrgen.py 1.0.0"

def read_stdin():
    if not sys.stdin.isatty():
        return sys.stdin.read().strip()
    return None

def generate_qr(data, output=None, show_ascii=False):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=6,
        border=1,
    )
    qr.add_data(data)
    qr.make(fit=True)

    if show_ascii:
        qr.print_ascii()
        return

    img = qr.make_image(fill_color="black", back_color="white")
    if output:
        img.save(output)
        print(f"💾 Saved QR to {output}")
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
