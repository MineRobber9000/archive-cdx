from urllib.parse import urlencode,quote
import requests, collections

def process_resp(rows):
	header = rows.pop(0)
	rowc = collections.namedtuple("Row",header)
	ret = []
	e = []
	for row in rows:
		if len(row)==len(header): # data row
			ret.append(rowc._make(row))
		elif len(row)==1: # continue key
			e.append(row)
		# leave off empty separator row
	return ret+e

def get(url,postproc=process_resp,**kwargs):
	kwargs["url"]=url
	kwargs["output"]="json" # force JSON output
	for k in kwargs.keys():
		if type(kwargs[k])==list:
			kwargs[k]=",".join(kwargs[k])
	r = requests.get("http://web.archive.org/cdx/search/cdx?"+urlencode(kwargs,safe="",quote_via=quote))
	r.raise_for_status()
	return postproc(r.json())
