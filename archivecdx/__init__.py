from archivecdx.grab import get
from time import sleep

# no resumption key/counter support, if you need them then make a PR and handle them yourself
DONT_USE = "showResumeKey resumeKey showDupeCount showSkipCount".split()

class Listing:
	def __init__(self,url,delay=1,**kwargs):
		self.url = url
		self.delay = delay
		self.kwargs = kwargs
		for key in kwargs:
			if key.endswith("_"):
				self.kwargs[key[:-1]]=self.kwargs[key]
				del self.kwargs[key]
		self.pre_process()
		for key in DONT_USE:
			if key in self.kwargs: del self.kwargs[key]
		self.listing = get(self.url,**self.kwargs)
	def pre_process(self):
		return
	def __getitem__(self,k):
		return self.listing[k]

class PaginatedListing(Listing):
	def pre_process(self):
		if not "page_count" in self.kwargs:
			self.kwargs["showNumPages"]="true"
			self.page_count = get(self.url,lambda x: x,**self.kwargs)
			del self.kwargs["showNumPages"]
			sleep(self.delay)
		else:
			self.page_count = self.kwargs["page_count"]
			del self.kwargs["page_count"]
		if "page" not in self.kwargs: self.kwargs["page"]=0
		self.kwargs["page"] = self.page_count if self.kwargs["page"]>self.page_count else self.kwargs["page"]
		self.page = self.kwargs["page"]
	@property
	def next_page(self):
		if self.page>self.page_count:
			return None # no next page
		self.kwargs["page"]=self.page+1
		self.kwargs["page_count"]=self.page_count
		return self.__class__(self.url,**self.kwargs)
