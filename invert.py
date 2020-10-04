from PorterStemmer import PorterStemmer

def updateDict():
    #This method reads the cacm file and saves all relavent lines, filtered by the fields, into a variable called docs so it may be processed

    includedFields = {'.I', '.T', '.W', '.B', '.A'}
    excludedFields = {'.N', '.X', '.K', '.C'}
    Fields = includedFields.union(excludedFields)

    currField = ""
    doc = ""


    for i in docs.splitlines():
        if i.split(' ')[0] in Fields:
            currField = i.split(' ')[0]
            #print(f"currField {currField}") #set current field
            if currField == '.I': #If new document is detected, then send off saved doc to addTerms() method and clear docs variable
                docId = int(i.split(' ')[1]) - 1
                print(f"\n{docId} \n")
                #print(doc)
                print(doc)
                wDocs.write(f"{docId}")
                wDocs.write(f"\n{doc}\n")

                addTerms(docId, doc)

                doc=""
            continue

        if currField in excludedFields:
            continue
        else:
            doc+= i + "\n"



def addTerms(docId, doc):
    #this method adds terms to dictionary data structure

    punctuation = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    doc = doc.lower() #make everything in the doc lowercase
    #print("BEFORE")
    #print(doc)

    for char in doc: #this loop removes all punctuation
        if char in punctuation:
            doc = doc.replace(char, " ")

    words = doc.split() #doc after punctuation is removed, made into a list of strings


    #STEM FINDER FUNCTION
    if STEMMER_ENABLED:
        for w in words:
            doc = doc.replace(w, p.stem(w, 0, len(w)-1))

    #print("AFTER")
    #print(doc)

    words = doc.split()

    #print(words)

    for t in words:
        if SW_ENABLED and t in stopwords: #if the term is a stopword, the continue
            continue
        elif t in dict: #if the term exists in the dictionary, then update
            #print("DUPLICATE")
            #print(f"duplicate term is {t}")

            l = dict[t]

            if l.find(str(docId))==-1:
                string = f", ({docId},{words.count(t)})"
                new = dict[t] + string
                dict[t] = new


            #print(f"dict[{t}] = {dict[t]}")
            #print("\n")
        else: #if the term does not exist in the dictonary, then add it
            #print("NEW")
            string = f"({docId},{words.count(t)})"
            dict[t] = string
            #print(f"dict[{t}] = {dict[t]}")
            #print('\n')



def writeFiles(): #this function will create and write to dictionary.txt
    dictionary = open("dictionary.txt", 'w')
    postings = open("postings.txt", 'w')
    invertedindex = open("inverted_index.txt", 'w')

    for i in sorted(dict):
        #print(f"{i}: {dict[i]}")
        dictionary.write(f"{i} [{dict[i].count('(')}] \n")
        postings.write(f"{dict[i]} \n")
        invertedindex.write(f"{i} [{dict[i].count('(')}] >> {dict[i]} \n")


    dictionary.close()

if __name__=="__main__":
    d = open("cacm/cacm.all", 'r')
    sw = open("cacm/common_words", 'r')
    p = PorterStemmer()
    wDocs = open("documents.txt", 'w')

    while True:
        x = input("Do you want to enable stemming? (y/n): ")
        x = x.lower()

        if x == "y":
            STEMMER_ENABLED = True
            print("Input accepted.")
            break
        elif x == "n":
            STEMMER_ENABLED = False
            print("Input accepted")
            break
        else:
            print("Invalid entry")

    while True:
        x = input("Do you want to enable stop word removal? (y/n): ")
        x = x.lower()

        if x == "y":
            SW_ENABLED = True
            print("Input accepted")
            break
        elif x == "n":
            SW_ENABLED = False
            print("Input accepted")
            break
        else:
            print("Invalid entry")

    #load into memory
    docs = d.read()

    #fields to record include .I (doc ID), .T(title), .W(abstract), B(publication date), .A (author list)

    stopwords = sw.read()
    stopwords = set(stopwords.split()) #create the set of stopwords


    dict = {} #this will hold the term and document frequency

    updateDict()
    writeFiles()


    d.close() #close master file
    sw.close()#close stopWords file

    print("\nFINISHED BUILDING DICTIONARY AND POSTINGS \n")



