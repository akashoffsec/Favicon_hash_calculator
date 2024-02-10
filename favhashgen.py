import mmh3
import requests
import argparse
import codecs

def download_favicon(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            print(f"Failed to download favicon from {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading favicon: {e}")

def main():
    parser = argparse.ArgumentParser(description="Favicon Hash Calculator")
    parser.add_argument("-u", "--url", help="URL of the favicon", required=True)
    args = parser.parse_args()

    favicon_url = args.url
    
    favicon_data = download_favicon(favicon_url)
    if favicon_data:
        favicon_base64 = codecs.encode(favicon_data, "base64")
        hash_value = mmh3.hash(favicon_base64)
        print(f"Favicon Hash: {hash_value}")
    else:
        print("Favicon data not available. Exiting.")

if __name__ == "__main__":
    main()
