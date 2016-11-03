import os
import re
from nltk.corpus import stopwords
import pdb
import operator

# Function to go through all the dicrectories and extract words adn create a dictionary
def get_dictionary(dir_path,dictionary,stopwords):
    list_dir = os.listdir(dir_path)
    if len(list_dir)==0:
        return
    else:
        for dir in list_dir:
            path = dir_path +'/'+dir
            if os.path.isdir(path):
                get_dictionary(path,dictionary,stopwords)
            elif os.path.isfile(path) and 'txt' in path:
                file_name = path
                file_read = open(file_name,'rb')
                for line in file_read:
                    line = re.sub('[\d-]','',line)
                    sub_words = line.split()
                    #remove stop words
                    filtered_words = [word for word in sub_words if word.lower() not in stopwords]
                    for word in filtered_words:
                        if word not in dictionary:
                            dictionary[word] = 1
                        else:
                            dictionary[word] = dictionary[word] + 1
        return


def main ():
    dir_path = '/home/sbp3624/CTCSpeechRecognition/prepare_datasets/dict_folder' #argv[0]
    dictionary={}
    stopwords=[]
    file_read = open('/home/sbp3624/nltk_data/corpora/stopwords/english','r')
    for word in file_read:
        stopwords.append(word.strip())
    get_dictionary(dir_path,dictionary,stopwords)
    # sort the dictionary based on value pairs
    sorted_dict = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
    # file for storing top 200000 frequent words
    file_dictionary = open('lexicon.txt','w')
    count = 0
    max_words = len(sorted_dict)
    print "max_count = %d" % (max_words)
    max_words = 200000
    for word,val in sorted_dict:
        if count<max_words:
            file_dictionary.write(word+" "+str(val)+'\n')
            count = count + 1
        else:
            break
    file_dictionary.close()


if __name__=='__main__':
    main()
