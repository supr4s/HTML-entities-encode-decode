import argparse
import html
import urllib.parse

def encode_string(input_string, url_encode=False):
    encoded = ''.join(f"&#{ord(char)}" for char in input_string)
    if url_encode:
        encoded = urllib.parse.quote(encoded)
    return encoded

def decode_string(input_string):
    decoded = ''.join(chr(int(entity[1:])) for entity in input_string.split('&')[1:])
    return decoded

def main():
    parser = argparse.ArgumentParser(description="Encode and decode strings using HTML entities.")
    parser.add_argument("--encode", help="Encode input string to HTML entities")
    parser.add_argument("--decode", help="Decode HTML entities to plain text")
    parser.add_argument("--url-encode", action="store_true", help="URL-encode the encoded result")

    args = parser.parse_args()

    if args.encode:
        encoded = encode_string(args.encode, args.url_encode)
        print("Encoded:", encoded)

    if args.decode:
        decoded = decode_string(args.decode)
        print("Decoded:", decoded)

if __name__ == "__main__":
    main()
