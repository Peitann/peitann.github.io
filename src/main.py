from files import get_file_path, save_to_json
from utilities import fetch_html_content, extract_headlines, parse_headlines


def main():
    site_url = "https://www.republika.co.id/"

    # crawl the site
    html_content = fetch_html_content(site_url)

    #get headline news/trending topics
    headlines = extract_headlines(html_content)

    # parsed headline to dictionary
    parsed_headlines = parse_headlines(headlines)

    #save to json file
    save_to_json(parsed_headlines, get_file_path())

if __name__=="__main__": 
    main()