def process(l,word):
    word=word.strip() #space removed
    if word in l:
      l.remove(word)
    return l1
    

l1=["john","roman","dean","seth","toby"]

l1=process(l1,"  dean ")
print(l1)
