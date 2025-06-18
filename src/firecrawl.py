import os
from firecrawl import FirecrawlApp, ScrapeOptions
from dotenv import load_dotenv

load_dotenv()


class FirecrawlService:
    def __init__(self):
        api_key = os.getenv("FIRECRAWL_API_KEY")
        if not api_key:
            raise ValueError("Missing FIRECRAWL_API_KEY environment variable")
        self.app = FirecrawlApp(api_key=api_key)

    def search_companies(self, query: str, num_results: int = 5):
        try:
            result = self.app.search(
                query=f"{query} company pricing",
                limit=num_results,
                scrape_options=ScrapeOptions(
                    formats=["markdown"] # This remains markdown for search results
                )
            )
            return result
        except Exception as e:
            print(f"Error during search: {e}")
            return []

    def scrape_company_pages(self, url: str):
        try:
            result = self.app.scrape_url(
                url,
                formats=["pdf"] # CHANGED: Now scrapes in PDF format
            )
            # When scraping as PDF, the 'result' will typically be a dictionary
            # containing 'content' which is the raw PDF bytes, and 'url'
            # Example: {'content': b'%PDF-1.4...', 'url': 'https://example.com'}
            return result
        except Exception as e:
            print(f"Error during PDF scraping of {url}: {e}")
            return None

# Example Usage (demonstrating how to save the PDF):
if __name__ == "__main__":
    service = FirecrawlService()

    # --- Example 1: Scrape a URL as PDF ---
    test_url = "https://www.google.com/search?q=example+pdf" # Or any URL that Firecrawl can render
    pdf_scrape_result = service.scrape_company_pages(test_url)

    if pdf_scrape_result and pdf_scrape_result.get('content'):
        pdf_bytes = pdf_scrape_result['content']
        output_filename = "scraped_page.pdf"
        try:
            with open(output_filename, "wb") as f:
                f.write(pdf_bytes)
            print(f"Successfully scraped '{test_url}' and saved as '{output_filename}'")
        except Exception as e:
            print(f"Failed to save PDF to file: {e}")
    else:
        print(f"Failed to scrape '{test_url}' or no PDF content returned.")

    # --- Example 2: Demonstrate search (still returns markdown/text) ---
    print("\n--- Performing a search (still markdown/text) ---")
    search_query = "Apple Inc."
    search_results = service.search_companies(search_query, num_results=1)

    if search_results:
        print(f"Search results for '{search_query}':")
        for i, item in enumerate(search_results['data']):
            print(f"  Result {i+1}:")
            print(f"    Title: {item['title']}")
            print(f"    URL: {item['url']}")
            # print(f"    Content (first 200 chars):\n{item['content'][:200]}...")
            print("-" * 20)
    else:
        print(f"No search results found for '{search_query}'.")