"""
checker.py: A script for fetching URLs with parameters from the Wayback Machine.

Usage:
    python checker.py (-u url | -l list.txt) [-o output.txt]

Options:
    -u, --url       Specify a single domain name to search for (e.g., domain.com).
    -l, --list         Specify a .txt file containing a list of domains, one per line.
    -o, --output       Specify an optional output .txt file name.

"""
import banner
import argparse
import sys
import requests

#Disable warning of ssl
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def check_url(url):
    pass

def check_list(input_filename,output_filename=None):
    """
    This function is used to fetch url status code from a file
    """
    with open(input_filename, 'r', encoding='utf-8') as input_file:
        urls = input_file.read().splitlines()
        
    unique_urls = list(set(urls))
    
    for url in unique_urls:
        response = requests.get(url,verify=False)
        
        #skip if status code is 404
        if (response.status_code == 404):
            continue
        save_urls(url,output_filename)
        print("[",response.status_code,"]:"+url)
        


def save_urls(url, output_filename=None):
    """
    Process URLs by either printing unique ones to the console or saving them to a file.

    Args:
        url (str): List of URLs to process.
        output_filename (str): The name of the output file. If provided,
            unique URLs will be saved to this file. If not provided, unique URLs
            will be printed to the console.

    Returns:
        None
    """
    if output_filename:
        with open(output_filename, 'a', encoding='utf-8') as output_file:
            output_file.write(url + '\n')


def main():
    banner.display_banner()
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-u', '--url', help='Single url path to check (e.g., domain.com/path/to/url)')
    group.add_argument('-l', '--list', help='Path to a .txt file containing a list of urls')
    parser.add_argument('-o', '--output', help='Specify the output .txt file name')
    
    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])
    
    if args.url:
        check_url(args.url)
        
    elif args.list:
        check_list(args.list,args.output)
        
    
if __name__ == "__main__":
    main()
