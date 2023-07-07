def count(filepath,word_list):
    with open(filepath) as file:
        text=file.read()
    words_count={}
    for word in word_list:
        count=text.count(word)
        words_count[word]=count   
    return words_count

l=['Web','English']
f='C:\\Users\\Brothers pc\\Desktop\python packages\\tweets.csv' 
res=count(filepath=f,word_list=l)
print(res)


          