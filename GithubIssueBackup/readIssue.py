import requests,json,codecs,sys
import re

# To get a 'TOKEN', see
# https://help.github.com/articles/creating-an-access-token-for-command-line-use/

headers = {'Authorization':'token <TOKEN>'}  

#url = 'https://api.github.com/repos/sanskrit-lexicon/ArabicInSanskrit/issues/1/comments'
#url_project = 'https://api.github.com/repos/sanskrit-lexicon'
def get_issue_main(url):
 r = requests.get(url,headers=headers)
 if r.status_code != 200:
  print "get_issue_main: url=",url
  print "get_issue_main: status = ",r.status_code
  exit(1)
 jr = r.json()
 body = jr['body']
 return body
 print "r.body="
 print body.encode('utf-8')
 return body

def get_issue_comments(url):
 r = requests.get(url,headers=headers)
 if r.status_code != 200:
  print "get_issue_comments: url=",url
  print "get_issue_comments: status = ",r.status_code
  exit(1)
 jr = r.json()
 bodies=[]
 for x in jr:
  if 'body' in x:
   body = x['body']
   bodies.append(body)
 return bodies
 h = r.headers
 link = h['link']
 print "link=\n",link
 parts = re.split(r',',link)
 lastpart = parts[1]
 print "lastpart=\n",lastpart
 m = re.search(r'[<](https:.*?)[?]page=(.*?)[>]',lastpart)
 if not m:
  print "Search for last page unsuccessful"
  print "url=",url
  exit(1)
 baseurl=m.group(1)
 lastpage = m.group(2)
 print "baseurl=",baseurl
 print "lastpage=",lastpage

 #fout = codecs.open(fileout,"w","utf-8")
 icomment=0
 bodies=[] # returned
 for page in xrange(0,int(lastpage)):
  ipage=page+1
  url = "%s?page=%s" % (baseurl,ipage)
  print url,"\n"
  r = requests.get(url,headers=headers)
  if r.status_code != 200:
   print "status_code problem:",r.status_code
   continue
  jr = r.json()
  # assume jr is an array
  for x in jr:
   icomment=icomment+1
   #out = "comment %s\n%s\n" %(icomment,x['body'])
   bodies.append(x['body'])
   #print out.encode('utf-8')
   #fout.write(out)

 #fout.close()
 print icomment,"comments processed"
 return bodies

if __name__=="__main__":
 begend=sys.argv[1] #begissue,endissue
 (beg,end) = re.split(',',begend)
 ibeg = int(beg)
 iend = int(end)
 owner = sys.argv[2] # sanskrit-lexicon
 repo = sys.argv[3] # GreekInSanskrit
 urlbase = 'https://api.github.com/repos'
 url_repo= '%s/%s/%s' %(urlbase,owner,repo)
 url_issues = "%s/%s" %(url_repo,'issues')
 filedir = sys.argv[4]
 separator = "-"*72
 for issuenum in xrange(ibeg,iend+1):
  url_main = "%s/%s" %(url_issues,issuenum)
  issuebody = get_issue_main(url_main)
  # ?page=1&per_page=10000   thanks to Dhaval - otherwise,
  # we get only the default first 30 issue comments.
  url_comments = "%s/%s" %(url_main,"comments?page=1&per_page=10000")
  issuecomments = get_issue_comments(url_comments)
  fileout = "%s/issue_%s" %(filedir,issuenum)
  fout = codecs.open(fileout,"w","utf-8")
  fout.write("%s\n" % url_main)
  fout.write("%s\n" % separator)
  fout.write(issuebody)
  for comment in issuecomments:
   fout.write("%s\n" % separator)
   fout.write("%s\n" % comment)
  fout.close()
  print len(issuecomments)," comments for issue#",issuenum,"in %s/%s" %(owner,repo)
