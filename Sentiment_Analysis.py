#list of punctuation characters to be striped
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# lists of positive words 
positive_words = []
with open("positive_words.txt") as pos_file:
    for lin in pos_file:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

#list of negative words
negative_words = []
with open("negative_words.txt") as neg_file:
    for lin in neg_file:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

#stripping the punctuation characters
def strip_punctuation(string):
    new_string=string
    for char in punctuation_chars:
        if char in string:
            new_string=new_string.replace(char,"")
    return new_string
            
#get the count of positive words
def get_pos(str):
    str=strip_punctuation(str)
    count_of_positive_words=0
    string=str.lower()
    words_in_string=string.split()
    for word in words_in_string:
        if word in positive_words:
            count_of_positive_words+=1
    return count_of_positive_words

#get the count of negative words
def get_neg(str):
    str=strip_punctuation(str)
    count_of_negative_words=0
    string=str.lower()
    words_in_string=string.split()
    for word in words_in_string:
        if word in negative_words:
            count_of_negative_words+=1
    return count_of_negative_words

def run(file):
    file_name=file
    
    #open resulting_file to write data
    result_file=open("resulting_data.csv","w")
    result_file.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score") #writing header line first
    result_file.write("\n")
    
    #open twitter_data file to read data and write into result_file
    # with open(file_name,"r") as twitter_file:
    twitter_file=open(file_name,"r")
    lines=twitter_file.readlines()
    
    for line in lines[1:]: #skip header line
        line_list=line.strip().split(",") 
        if line_list==['']: #if file has an empty line ignore and continue to next line
            continue
        result_string_row="{},{},{},{},{}".format(line_list[1],line_list[2],get_pos(line_list[0]),get_neg(line_list[0]),get_pos(line_list[0])-get_neg(line_list[0]))
        
        result_file.write(result_string_row)
        result_file.write("\n")
    result_file.close()


if __name__ == '__main__':
    run('twitter_data.csv')
