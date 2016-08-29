import os
from urllib2 import urlopen, URLError, HTTPError

def dlfile(url):
    try:
        f = urlopen(url)
        print "downloading " + url

        with open(os.path.basename(url), "wb") as local_file:
            local_file.write(f.read())

    except HTTPError, e:
        print "HTTP Error:", e.code, url
    except URLError, e:
        print "URL Error:", e.reason, url

def main():
    for index in range(1, 144):
        url = ("http://osoite.fi/kansio/%d.png" % (index))
        dlfile(url)

if __name__ == '__main__':
    main()