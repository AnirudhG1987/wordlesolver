import numpy as np
import pandas as pd

def common_letters(array):
    dict_char = {}
    for word in array:
        for i in range(len(word)):
            if word[i] in dict_char.keys():
                dict_char[word[i]] += 1
            else:
                dict_char[word[i]] = 1
    #print(dict_char)
    return dict_char
    #print(max(dict_char,key=dict_char.get))
    #return max(dict_char,key=dict_char.get)


def common_position(top_char, array):
    dict_char = {}
    for i in range(len(word)):
        for word in array:
            if word[i] in dict_char.keys():
                if len(dict_char[word[i]])==i+1:
                    dict_char[word[i]][i] = dict_char[word[i]][i]+1
                else:
                    dict_char[word[i]]=np.append(dict_char[word[i]],1)
            else:
                dict_char[word[i]] = np.array([1])
    #print(dict_char)
    #print(max(dict_char,key=dict_char.get))
    return np.argmax(dict_char[top_char])
#TIRED AROSE LIVER
def best_guess(array):
    dic_chars = common_letters(array)
    print(dic_chars)
    #print(common_position(top_char,array_dummy))
    best_word = array[0]
    word_value = 0
    for word in array:
        if len(set(word))==5:
            if dic_chars[word[0]]+dic_chars[word[1]]+dic_chars[word[2]]+dic_chars[word[3]]+dic_chars[word[4]]>word_value:
                word_value = dic_chars[word[0]]+dic_chars[word[1]]+dic_chars[word[2]]+dic_chars[word[3]]+dic_chars[word[4]]
                best_word = word

    return best_word


def green_boxes_func(dict_string,array):
    dict_green = dict()
    for text in dict_string.split(','):
        key_str = int(text.split(':')[0])
        val_str = text.split(':')[1]
        dict_green[key_str]=val_str

    #print(dict_green)
    for key in dict_green.keys():
        array_new = np.array([])
        for word in array:
            if word[key] == dict_green[key]:
                array_new = np.append(array_new,word)
        array=array_new
    return array

def remove_green(dict_string,array):
    dict_green = dict()
    for text in dict_string.split(','):
        key_str = int(text.split(':')[0])
        val_str = text.split(':')[1]
        dict_green[key_str]=val_str

    #print(dict_green)
    for i in range(len(array)):
        for key in dict_green.keys():
            if array[i][key]==dict_green[key]:
                array[i] = array[i][:key]+array[i][key+1:]
    print(array)
    return array


def yellow_boxes_func(dict_string,array):
    dict_yellow = dict()
    for text in dict_string.split(','):
        key_str = text.split(':')[0]
        val_str = int(text.split(':')[1])
        dict_yellow[key_str]=val_str

    for c in dict_yellow.keys():
        array_new = np.array([])
        for word in array:
            if c in word and word[dict_yellow[c]]!=c:
                array_new = np.append(array_new,word)
        array=array_new
    return array

def grey_boxes_func(char_string,array):
    for c in char_string.split(','):
        array_new = np.array([])
        for word in array:
            if c not in word:
                array_new = np.append(array_new,word)
        array=array_new
    return array

df = pd.read_excel('wordsfive.xlsx')
array = np.asarray(df)
array = array.reshape(5756)[:-1]

while len(array)!=1:
    green_string = input("Green Characters:")
    if len(green_string)!=0:
        array  = green_boxes_func(green_string,array)
        #print(array)
    yellow_string = input("Yellow Characters:")
    if len(yellow_string) != 0:
        array = yellow_boxes_func(yellow_string, array)
        #print(array)

    grey_string = input("Grey Characters:")
    if len(grey_string) != 0:
        array = grey_boxes_func(grey_string, array)
    print(array)
    array_dummy = np.copy(array)
    #if len(green_string)!=0:
    #    array_dummy = remove_green(green_string,array_dummy)
    print(best_guess(array_dummy))
