# Multisite-Python-Crawler
## Usage : 
```shell
scrapy crawl mySpider -a url=<enter_complete_url> -a domain=<enter_allowed_domains_seperated_by_&>
```

## Description :

An almost generic web crawler built using Scrapy and Python 3.7 to recursively crawl entire websites. 
Developing a single generic crawler is difficult as different websites require different XPath expressions to retreive content.
This multisite crawler gets the paragraph tag text and outputs a JSON file of the following format :-
```json
{
	"pages" : [
		{
			"page" : "...."
			"content" : "...."
		},
		{
			"page" : "..."
			"content" : "..."
		}
	.
	.
	.
	]
}
```

If required, it can be modified to read text from other tags by including explicit xpath statements too.
After installing scrapy using 'pip install scrapy' copy the entire repository onto any suitable location and use as per the usage.


