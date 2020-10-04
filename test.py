from PorterStemmer import PorterStemmer

def printContext(docId, termFreq, q):

    def getDoc(line, docId): #returns the relavent document
        line = int(line)
        nextIndex = str(int(docId) + 1)

        d = ""

        while True:
            if line == len(docs)-1:
                break
            elif docs[line] == nextIndex:
                break

            d += docs[line]+'\n'
            line+=1

        #print("document: ")
        #print(d)
        return d

    def context(doc, term):
        print("CONTEXT:")

        term = term.lower()
        doc = doc.lower()
        doc = doc.split()

        count = 0
        for word in doc:
            if word.find(term)!=-1:
                break
                print(word)
            count += 1

        if count - 10 < 0:
            start = 0
        else:
            start = count - 10

        if count + 10 > len(doc):
            end = len(doc)
        else:
            end = count + 10


        context = ""
        for i in range(start, end):

            if i == count:
                context+=" >>>"
            elif i == count+1:
                context += "<<< "

            context += doc[i] + " "

        print("..." + context + "...")

    #print(docId)
    #print(termFreq)

    for index in docId: #index are the documents that need to be searched for the context
        line = 0

        for id in docs:
            line += 1
            if id == index:
                #print(f"found at line {line}")
                title = docs[line]
                print(f"Document ID: {id}")
                print(f"Title: {title}")
                print(f"Occurrences in document: {termFreq[docId.index(id)]}")
                document = getDoc(line, index)
                context(document, q)
                print("--------------------------------------------------------------")
                break



def findMatches(q):

    count = 0
    for l in dict:
        count+=1

        bracket = l.find('[') - 1

        if l[:bracket] == q:
            #print(f"Matching term found at line {count}")
            break
        elif l == dict[-1]:
            print(f"THERE IS NO TERM '{q}' IN THE DICTIONARY")
            return

    print(f"DOCUMENT FREQUENCY OF '{q}':{dict[count - 1][len(q):]}\n")
    #print(posts[count - 1])
    listings = posts[count - 1].split(', ')
    #print(listings)
    docID = []
    termFreq = []
    for i in listings:
        docID.append(i[1:i.find(',')])
        termFreq.append(i[i.find(',')+1:-1])

    termFreq[-1] = termFreq[-1][:-1]
    #print(docID)
    #print(termFreq)

    printContext(docID, termFreq, q)


def ProcessQuery(q):
    punctuation = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''

    q = q.lower().strip()#change everything to lowercase

    for c in q:
        if c in punctuation:
            q = q.replace(c, " ")

    print(f"Post-punctuation removal: {q}")

    l = q.split()

    if STEMMER_ENABLED:
        for w in l:
            q = q.replace(w, p.stem(w, 0, len(w)-1))

        print(f"Post-stemming: {q}")

    return q

if __name__=="__main__":
    p = PorterStemmer() #create stemmer object
    dictionary = open("dictionary.txt", 'r') #open dictionary and postings file
    postings = open("postings.txt", 'r')
    documents = open("documents.txt", 'r')

    dict = dictionary.read().splitlines() #load dictionary and postings into memory
    posts = postings.read().splitlines()
    docs = documents.read().splitlines()

    while True:
        x = input("Did you enable stemming for invert.py? (y/n): ")
        x = x.lower()

        if x == "y":
            STEMMER_ENABLED = True
            print("Input accepted. Stemming enabled for queries.")
            break
        elif x == "n":
            STEMMER_ENABLED = False
            print("Input accepted. Stemming disabled for queries.")
            break
        else:
            print("Invalid entry.")




    #add stopword enable or disable

    while True:
        q = input("Enter in a single term (or 'ZZEND to stop'): ")

        if q.lower() == 'zzend':
            print("Terminating Program.")
            break
        elif len(q.split())>1:
            print("Multiple terms were inputted, enter only one term")
        else:
            print(f"Input query: {q}")

            ppq = ProcessQuery(q)
            print(f"Post-processed query: {ppq}\n")

            findMatches(ppq)


        print("\n")

    documents.close()
    dictionary.close()
    postings.close()
