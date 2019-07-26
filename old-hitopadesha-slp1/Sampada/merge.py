""" merge.py
 2018-12-29
 python merge.py ../hitokale_slp1_v1.txt sent_105.33-01_sam.txt
 python merge.py filein fileupd
 make a new version of filein based on fileupd.
 No change to ';' lines (comments)
 No change to lines xxx.yyF:
 Replace lines xxx.yyA: from fileupd
"""
import sys,re,codecs

class Rec(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.line = line
  m = re.search(r'^([0-9][0-9][0-9][.][0-9][0-9][FA]: )(.*)$',self.line)
  if m:
   self.code = m.group(1)
   self.text = m.group(2)
  else:
   self.code = 'comment'
   self.text = line
  self.changed = False
  self.newline = self.line

def init_recs(filein):
 with codecs.open(filein,"r","utf-8") as f:
  recs = [Rec(x) for x in f]
 return recs

def update1(recin,recupd):
 recin.newline = recupd.line
 recin.changed = (recin.newline != recin.line)

def update(recsin,recsupd):
 # make a dictionary from the 'Analyzed' lines of recsupd
 d = {}
 for rec in recsupd:
  if rec.code.endswith('A: '):
   if rec.code in d:
    print("update: Duplicate code error:",rec.code,rec.line)
    exit (1)
   d[rec.code] = rec
 # change records of recsin using 'd'
 for rec in recsin:
  if rec.code not in d:
   continue # no change
  recupd = d[rec.code]
  update1(rec,recupd)

if __name__ == "__main__":
 filein = sys.argv[1]
 fileupd = sys.argv[2]
 recsin = init_recs(filein)
 recsupd = init_recs(fileupd)
 update(recsin,recsupd) # modify recsin
 # write recsin back to filein
 with codecs.open(filein,"w","utf-8") as f:
  nchange = 0
  for rec in recsin:
   if rec.changed:
    nchange = nchange + 1
   f.write(rec.newline + '\n')
 #
 print(nchange,"lines changed in",filein)

    
