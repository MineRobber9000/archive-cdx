from archivecdx.grab import get
from time import sleep

# no resumption key/counter support, if you need them then make a PR and handle them yourself
DONT_USE = "showResumeKey resumeKey showDupeCount showSkipCount".split()

class Listing:
	def __init__(self,url,delay=1,**kwargs):
		self.url = url
		if not "page_count" in kwargs:
			kwargs["showNumPages"]="true"
			self.page_count = get(url,lambda x: x,**kwargs)
			del kwargs["showNumPages"]
			sleep(delay)
		else:
			self.page_count = kwargs["page_count"]
			del kwargs["page_count"]
		if "page" not in kwargs: kwargs["page"]=0
		kwargs["page"] = self.page_count if kwargs["page"]>self.page_count else kwargs["page"]
		self.page = kwargs["page"]
		self.kwargs = kwargs
		for key in DONT_USE:
			if key in kwargs: del kwargs[key]
		self.listing = get(url,**kwargs)
	def __getitem__(self,k):
		return self.listing[k]
	@property
	def next_page(self):
		if self.page>self.page_count:
			return None # no next page
		self.kwargs["page"]=self.page+1
		self.kwargs["page_count"]=self.page_count
		return self.__class__(self.url,**self.kwargs)
