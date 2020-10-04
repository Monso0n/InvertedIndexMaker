# InvertedIndexMaker
Given a cacm file, this program constructs an inverted index for search engine processing

How to Run Programs
1.	Run the test.py program.
2.	If you want word stemming to be used (via Porter’s Stemming algorithm), input ‘y’. Otherwise, input ‘n’.
3.	If you want stop words to be removed (from common_words file), input ‘y’. Otherwise, input ‘n’. 
4.	Please wait while the program writes the required files. The program will output when it is done compiling
5.	Run the test.py program.
6.	If you used stemming in step 2, input ‘y’. Otherwise, input ‘n’. 
7.	Input a single query term. Please ensure there are no punctuations or non-alphanumeric characters in the term. 
8.	View the output of the test program. Observe document frequency of the term, the documents in which the term occurred in. Furthermore, observe the title, document ID, term frequency, and highlights the term in the context of the document. 
9.	The program loops again, see step 7.
What the Programs Do
Invert.py
The program invert.py fulfills the requirement of the assignment to read the cacm.all file and write the required dictionary.txt and postings.txt files. 
The dictionary.txt file contains all the valid terms within the relevant documents along side it, lists its document frequency. The format in the dictionary .txt file is: TERM [DOC_FREQ]. The postings.txt file contains the postings for these terms. 
The postings.txt file contain the postings for each valid term. The term postings correspond to the same line number as in dictionary.txt, therefore both files have the same amount of lines. The format for the postings for each term is: (DOC_ID, TERM_FREQ). The number of tuples is equivalent to the document frequency for each term. The term position is not recorded, as when questioned about its requirement, the professor stated that it is not a requirement.
In the invert program, the program asks the user whether they want to enable stemming and stop word removal. The word stemming algorithm used is the Porter’s Stemmer algorithm, from the source the professor has linked in the resources. The stop word removal uses the list from the provided common_words file to detect if a word should be removed. The program always removes punctuation and converts the words to lowercase, to make the program process faster and reduce the size of the dictionary and postings files.
Additionally, for debugging purposes and visual analysis, the invert program also writes a inverted_index.txt file, which is just an amalgamation of the dictionary and postings for each term to create an inverted index. The invert program also creates a documents.txt, this is used in the test program. This contains all the valid document information from the cacm.all file.  

Test.py
The program test.py prompts the user to input a single term for its query and then searches the compiled dictionary.txt and postings.txt for an instance of that term and displays an output. The output shows the term frequency of the entered term, and a list of all the documents containing the term. When displaying the documents, the test program also shows the document ID of the document displayed, the document title, the term frequency, and also highlights the term occurring within the document.
Before a query can be inputted, the program prompts the user whether stemming was used in the invert program. The user should input ‘y’ if it was, and ‘n’ if it was not. After this, the user is asked to input a single term, and the before-mentioned output is shown. 
