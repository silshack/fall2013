---
title: Grant's Extra-Credit Excercises
author: gmclendon
category: post
layout: post
---


So the full code for this thing is rather long and can be found [here]({{ site.baseurl }}/files/gerbal/grants-code.html).

##Excercise 1  

```python  
def excercise1(book):
    '''
    proccess_file() got rather complicated and too sofisticated for this problem
    So we're just going to rewrite it here. We could define a new method,
    but my preference is to only do that if we need to solve the same problem 3 or more times
    '''
    fp = open(book)
    longstring = str()
    for line in fp:
        line = line.replace('-', ' ')
        for word in line.split(): 
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()
            word = re.sub('[\W_]+','', word) #regular expressions clean up wierd characters not included in string.punctuation
            longstring = longstring + word + " "
    return longstring
```  

The excercise1 takes the argument of a text file and returns it stripped of all nonalphanumeric characters

##Exercise 2  

```python  
def def exercise2(book):
    hist = process_file(book, True)
    return "There are %d unique words in this work" %len(hist)
	
def process_file(filename, guten):
    hist = dict()
    fp = open(filename)
    if guten:
        header = True
    if not guten:
        header = False
    for line in fp:
        if line[:20] == "*** END OF THIS PROJ": # There must be a better way to escape the header and footer
            header = True
        if not header:
            process_line(line, hist)
        if line[:20] == "*END*THE SMALL PRINT" or line[:20]=="*** START OF THIS PR": #this is only for the shakespeares folios "00ws110.tt"
            header = False
            #print "header escaped" #woo, debugging
    return hist

def process_line(line, hist):
    line = line.replace('-', ' ') #clean hyphenated words
    
    for word in line.split(): #re.split('[\W_]+', line) #could do the split with regex, but regex is magic and doesn't strip punctuation quite as nicely
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        word = re.sub('[\W_]+','', word) #this regular expression should get rid of the few special iso characters not in string.punctuation
        
        hist[word] = hist.get(word, 0) + 1
```  

Exercise 2 returns the number of unique words used in a body of text. A cursory examination of a couple of text from different eras suggest modern texts have fewer unique words. This owes mostly to orthographical errors and inconsistency. Though it also does have to do with a contracting vocabulary as older terms fell our of use

##Exercise 3  

```python  
def exercise3(book):
    hist = process_file(book, True)
    output = top_20(hist)
    return output
	
def top_20(hist):
    hist_sorted = sorted(hist.iteritems(), key=operator.itemgetter(1), reverse=True) #according to stackexchange this is a really fast way to sort a dicitonary
    output ="The twenty most common terms in this work are:\n"
    for i in range(0,20):
        output += str(hist_sorted[i]) +"\n"
    return output
```

Exercise 3 returns the 20 most common words in a given book. They are almost always "the" though sometimes Gutenberg makes an appearance if the header and footer ignore mechanism malfunctions.

##Exercise 4  

```python
def exercise4(book):
    output_list = return_true_words(compare_lists(process_file(book, True), process_file("words.txt", False)))
    return output_list #long 
def compare_lists(list1, list2):
    new_list = dict()
    for word1 in list1:
        new_list[word1] = True
        #print word1
        if list2.has_key(word1):
            new_list[word1] = False
    return new_list
```  

Exercise 4 takes two lists of words, a book and a list of common words, compares them and returns the words present in the book not present in the list of common words.  Most of the returned words for newer texts (post ~1820ish) are proper nouns or specialized vocabulary. For older text orthography and vocabulary vary so widely that many more words are returned. Shakespeare and works of that same age often have more words excluded than included in the list of common words. 


And Finally I wrote the following method to call all of the excercise() methods because I was too lazy to type out 'excerciseN()' four times

```python  
def writeitallout():
    for i in range(1,5):
        output = open("execise%d.txt" % i, "w")
        method_name = "exercise%d" % i #because writing four method names is hard

        outtext = eval(method_name) #eval() evaluates a string as python code
        '''
        eval() is kind of dangerous and has the potential to make it much easier
        to excecute malicious, obfuscated code, but it works in this case.
        I suppose this makes this bad code. The other methods I tried to solve this
        problem did not work nearly as well.
        '''
        print "Writing exercise %d to file exercise%d.txt" % (i,i)
        output.write(str(outtext('pg43791.txt')))
        output.close()
```  

As I note in the comments, eval() is a particularly dangerous method and according to the kind folks on StackExchange a mark of poor programming. It does pose serious security concerns as it does allow potentially malicious code to be generated in an obfuscated way. 
