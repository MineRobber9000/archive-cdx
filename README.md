# archive-cdx

A library to interact with the archive.org Wayback Machine CDX server.

## How to

`archivecdx.Listing` is the basic list class.

Pass [CDX URL arguments](https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server#intro-and-usage-1) as keyword args. (For arguments that are Python keywords, append an underscore and the library will automatically remove it for you.)

Special args:

 - `url` - the `url` param
 - `delay` - the delay between automatic page count detection and grabbing the first page

```python
import archivecdx

listing = archivecdx.Listing("archive.org",fl=["original","timestamp","digest"])

print(listing[0]) # "Row(original='http://www.archive.org:80/',timestamp='19970126045828',digest='Q4YULN754FHV2U6Q5JUT6Q2P57WEWNNY')"
```

`archivecdx.PaginatedListing` uses the [Pagination API](https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server#pagination-api) to return less values at once.

It supports the `page` keyword argument and adds a `next_page` attribute, which will automatically pull the next page from the API.

```python
import archivecdx

listing = archivecdx.PaginatedListing("archive.org",page=1,fl=["original","timestamp","digest"])

print(len(listing.listing)) # 15000
```
