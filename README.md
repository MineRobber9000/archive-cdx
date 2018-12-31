# archive-cdx

A library to interact with the archive.org Wayback Machine CDX server.

## How to

`archivecdx.Listing` is the basic list class.

Pass [CDX URL arguments](https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server#intro-and-usage-1) as keyword args.

Special args:

 - `url` - the `url` param
 - `delay` - the delay between automatic page count detection and grabbing the first page

```python
import archivecdx

listing = archivecdx.Listing("archive.org",fl=["original","timestamp","digest"])

print(listing[0]) # "Row(original='http://www.archive.org:80/',timestamp='19970126045828',digest='Q4YULN754FHV2U6Q5JUT6Q2P57WEWNNY')"
```
