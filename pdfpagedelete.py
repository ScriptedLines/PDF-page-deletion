from pypdf import *
n=input("Enter name of pdf:")
r=PdfReader(n+".pdf")
w=PdfWriter()
l=[]

no=int(input("Enter number of pages to be deleted:"))
for i in range(no):
    paged=int(input("Enter page number:"))
    l.append(paged-1)

x=0

while True:
    try:
        if x in l:
            x+=1
            continue
        else:
            w.add_page(r.pages[x])
            x+=1
    except:
        break

name=input("Enter name of new pdf")
w.write(name+".pdf")

