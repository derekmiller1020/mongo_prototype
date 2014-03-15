class Dec(object):
   
    def __init__(self, f):
	self.f = f

    def __call__(self):
	print "this is the start of the call in Dec"
	self.f()
	print "this is the end of the call in Dec"

@Dec
def something():
    print "this is inside something"

something()
