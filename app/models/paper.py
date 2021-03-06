class Paper(object):
	def __init__(self,
		name,
		authors,
		year,
		arxiv_id,
		note=None,
		other_links=None
	):
		self.name = name
		self.authors = authors
		self.arxiv_id = arxiv_id
		self.year = year
		self.note = note
		self.is_published = False
		if other_links is not None:
			self.other_links = other_links
		else:
			self.other_links = []


class PublishedPaper(Paper):
	def __init__(self, 
		name,
		authors,
		year,
		arxiv_id,
		journal,
		journal_website=None,
		note=None,
		other_links=None
	):
		super(PublishedPaper, self).__init__(name, authors, year, arxiv_id, note=note, other_links=other_links)
		self.is_published = True
		self.journal = journal
		self.journal_website = journal_website


class PaperLink(object):
	def __init__(self, url, text, icon=None):
		self.url = url
		self.text = text
		self.icon = icon


class Author(object):
	def __init__(self, first_name, last_name, website=None, is_me=False):
		self.first_name = first_name
		self.last_name = last_name
		self.website = website
		self.is_me = is_me

	@property
	def name(self):
		return self.first_name + " " + self.last_name
	

class Talk(object):
	def __init__(self, where, when, topic=None):
		self.where = where
		self.when = when
		self.topic = topic