import urllib2
import time
import datetime

print "Recording audio..."


dt=datetime.datetime.today().weekday()+1
"""
response = urllib2.urlopen("http://95.81.146.10/4598/sky_151349.mp3")
filename = "/tmp/emission"+str(dt)+".mp3"
f = open(filename, 'wb')

start_time_in_seconds = time.time()
limit = 60

block_size = 1024

while time.time()-start_time_in_seconds<limit:
    try:
        buffer = response.read(block_size)
        if not buffer:
            break
        f.write(buffer)

    except Exception, e:
        logger.exception(e)
f.close()

"""
import fileinput
print datetime.datetime.today()
i=0
for line in fileinput.input("bouy.txt",inplace=True): # Does a list of files, and writes redirects STDOUT to the file in question
    i=i+1
    if i==3:
        linee=line
        dat=time.strftime('%d-%m-%y',time.localtime())
        print line.replace(linee, ">>"+dat+"<<>>http://neilprod92.hostoi.com/Songs/emissionceciestunfake"+str(dt)+".mp3<<\n"),
    else : print line,    

    







print "Bennnnnnnneeene"