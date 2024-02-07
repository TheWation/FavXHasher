import argparse
import mmh3
import requests
import codecs

def logo() -> str:
    """Return the logo/banner."""
    return '''
____    __    ____  ___   .___________. __    ______   .__   __. 
\   \  /  \  /   / /   \  |           ||  |  /  __  \  |  \ |  | 
 \   \/    \/   / /  ^  \ `---|  |----`|  | |  |  |  | |   \|  | 
  \            / /  /_\  \    |  |     |  | |  |  |  | |  . `  | 
   \    /\    / /  _____  \   |  |     |  | |  `--'  | |  |\   | 
    \__/  \__/ /__/     \__\  |__|     |__|  \______/  |__| \__| 

                          FavXHasher v1.0                                       
'''

def generate_favicon_hash(url: str) -> None:
    """Generate hash for a given favicon URL."""
    try:
        response = requests.get(url)
        favicon_content = codecs.encode(response.content, "base64")
        favicon_hash = mmh3.hash(favicon_content)
        print(f'[+] Favicon Hash is: {favicon_hash}')
        print(f'[!] Use http.favicon.hash:{favicon_hash} on Shodan to detect potential phishing websites.')
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")



class CustomArgumentParser(argparse.ArgumentParser):
    def format_help(self):
        return logo() + super().format_help()

def main() -> None:
    parser = CustomArgumentParser(description='This tool calculates the hash value of a favicon from a given URL, enabling the detection of potential phishing websites by leveraging Shodan\'s search capabilities, For more information, visit the project repository: https://github.com/TheWation/FavXHasher')
    parser.add_argument('-u', '--url', type=str, help='Favicon URL to generate Hash')
    args = parser.parse_args()

    if args.url:
        print(logo())
        generate_favicon_hash(args.url)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()