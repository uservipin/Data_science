#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import html
import requests
import pandas as pd
import numpy as np
import re 
import time

from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
nltk.download('punkt')


# In[2]:


sheet_positive_negetive_stop_words_constrain_uncertanity_words= pd.read_excel('C:/Users/kumar/OneDrive/Programm/Project/NLP/NLP_problem_Statement/sheet_of_Positive_negative_Stop_Word_constrain_uncertenity_words.xlsx')
sheet_positive_negetive_stop_words_constrain_uncertanity_words


# In[3]:



CIK1=[]
CONAME1=[]
FYRMO1=[]
FDATE1=[]
FORM1=[]
SECFNAME1=[]
pos_score =[]
neg_score = []
pol_score= []
avg_sen_len = []
percentage_of_com_words= []
f_ind= []
complex_wor_count= []
word_counter =[]
uncer_score = []
const_score = []
pos_wor_prop= []
neg_wor_prop= []
uncer_wor_prop= []
cons_wor_prop= []
constraning_words_whole_report=[]


# In[4]:


def fetch_data(link):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
#     url= "https://wwlinkw.sec.gov/Archives/edgar/data/3662/0000950170-98-000413.txt"
    data = requests.get(link,headers)
    time.sleep(5)
    return data


# In[5]:


# data.status_code


# In[6]:


# data.content


# In[7]:


def BeautifulSoup_data(input_data_content, par):
    soup = BeautifulSoup(input_data_content, par)
#     print(soup)
#     print(soup.prettify())
#     [type(item) for item in list(soup.children)]
#     list(soup.children)
#     html_text = list(soup.children)[1].get_text()
#     type(html_text)
    return soup    


# In[ ]:





# In[8]:


def establish_connection(link):
    data=  fetch_data(link)
    data.status_code
    while(data.status_code != 200):
        data = fetch_data(link)
        print('data not connected to source')
        if(data.status_code == 200):
            print('welcome data connect successfully')
            break
    return data


# In[9]:


# soup


# In[10]:


# soup = BeautifulSoup(data.content, 'html.parser')
# soup


# In[11]:


# print(soup.prettify())


# In[12]:


# [type(item) for item in list(soup.children)]


# In[13]:


# len(list(soup.children))


# In[14]:


# soup.children


# In[15]:


def get_text_from_report(soup):
    [type(item) for item in list(soup.children)]
    html_text = list(soup.children)[1].get_text()
    return html_text   


# In[16]:


# text_from_report = get_text_from_report(soup)


# In[17]:


# html_text = list(soup.children)[1].get_text()
# html_text


# In[18]:


# type(html_text)


# # Search by Tags

# In[19]:


def search_by_tag(soup1):
    list_of_tag= [tag.name for tag in soup1.find_all()]
    set_of_tag = set()
    for tags in list_of_tag:
        set_of_tag.add(tags)
#     lenght = len(soup.find_all("text"))
    return set_of_tag    


# In[20]:


# tag_name = search_by_tag(soup)


# In[21]:


# list_of_tag= [tag.name for tag in soup.find_all()]


# In[22]:


# set_of_tag = set()


# In[23]:


# for tags in list_of_tag:
#     set_of_tag.add(tags)


# In[24]:


# set_of_tag


# In[25]:


# print(len(soup.find_all("text")))


# In[26]:


# soup.find_all("text")


# t =soup.find_all('p', class_='note')
# t

# soup.find_all(id="header")

# f = open('file.txt', 'r')
# f.read()

# # Apply NLP

# 1. word tokenizer 
# 2. sentence tokenizer 

# Extracting Derived variables
# 1. Positive score
# 2. Negative score
# 3. polarity 
# 4. subjectivity

# Sentiment score categorization
# This is determined by grouping the Polarity score values in the following groups.
#  
# 1. Most Negative: Polarity Score below -0.5
#  
# 2. Negative: Polarity Score between -0.5 and 0
#  
# 3. Neutral: Polarity Score equal to 0
#  
# 4. Positive: Polarity Score between 0 and 0.5
#  
# 5. Very Positive: Polarity Score above 0.5
# 

# Analysis of Readability
# 1. Average Sentence Length 
# 2. Percentage of Complex words 
# 3. Average Number of Words Per Sentence
# 4. Complex Word Count
# 5. Word Count
# 6. Syllable Count Per Word
# 7. Passive Words
# 8. Average Word Length
# 
# 
# 

# # Word Tokenizer

# In[27]:


def word_token(text_from_report):
    word_token = word_tokenize(text_from_report)
    return word_token
    
    


# In[28]:


# w_token = word_token(text_from_report)


# # Sentence Tokenizer

# In[29]:


def sen_token(text_from_report):
    sent_token = sent_tokenize(text_from_report)
    return sent_token


# In[30]:


# s_token = sen_token(text_from_report)


# In[31]:


# s_token


# In[32]:


# print(type(s_token))
# print(len(s_token))
# print(type(w_token))
# print(len(w_token))


# # Total No of Sentence

# In[ ]:





# In[33]:


def total_no_of_sentence(s_token):
    Total_sentence= len(s_token)
    return Total_sentence


# In[34]:


# Total_no_of_sentence=total_no_of_sentence(s_token)
# Total_no_of_sentence


# # Filter text using Regular Expression 

# In[35]:


def filter_word_using_re(w_token):
    clean_test=[]
    clean= ''
    for word in w_token:
        res= re.sub(r'[^\w\s]|[^\D]',"",word)
        if res != "":
            clean= res
            clean_test.append(clean)
            
    clean_test_in_lower_case= []
    for word in clean_test:
        t= word.lower()
        clean_test_in_lower_case.append(t)

    return clean_test_in_lower_case 


# In[36]:


# clean_test_in_lower_case = filter_word_using_re(w_token)


# In[37]:


# clean_test_in_lower_case


# clean word_token list 
# remove all non word and digit character

# # Total No. of Words after removing Non text character

# In[38]:


def Total_No_of_Words_after_removing_Non_text_character(clean_test_in_lower_case):
    Total_words= len(clean_test_in_lower_case)
    return Total_words     


# # Total_No_of_Words

# In[39]:


# Total_no_of_words =  Total_No_of_Words_after_removing_Non_text_character(clean_test_in_lower_case)
# Total_no_of_words


# 
# sent_token = sent_tokenize(f.read())

# # Stop word removal count  words_after removing stop word

# We count the total cleaned words present in the text by 
# removing the stop words (using stopwords class of nltk package).

# # Convert_Pandas_Series_to_Int

# In[40]:


def convert_pandas_series_to_int(List_of_stop_words):
    List_of_stop_words = List_of_stop_words.to_list()
    return List_of_stop_words    


# In[41]:


def count_words(List_of_stop_words):
    List_of_stop_words= convert_pandas_series_to_int(List_of_stop_words)
    list_of_words_after_stop_words= []
    for word in clean_test_in_lower_case :
        if not word in List_of_stop_words:
            list_of_words_after_stop_words.append(word)
    return len(list_of_words_after_stop_words)


# ## Word Count

# In[42]:


list_of_words_after_stop_words = sheet_positive_negetive_stop_words_constrain_uncertanity_words['Stop_Words'].dropna()
# word_count = count_words(list_of_words_after_stop_words)
# word_count


# # Extracting Derived variables

# In[43]:


def count(text_list,list_search):
    list_search= convert_pandas_series_to_int(list_search)
    counter =0
    for word in text_list:
        if word in list_search :
            counter +=1
    return counter


# # Positive Score 

# This score is calculated by assigning the value of +1 for each word if 
# found in the Positive Dictionary and then adding up all the values.

# clean_test_in_lower_case_of_lemitization
# List_of_Positive_words_after_removing_stop_word
# List_of_Negative_words_after_removing_stop_word
# clean_test_in_lower_case

# In[44]:


# List_of_Posative_words=  sheet_positive_negetive_stop_words_constrain_uncertanity_words['Posative_Words'].dropna()
# Positive_score = count(list_of_words_after_stop_words,List_of_Posative_words)
# Positive_score


# # Tokenize

# # Negative Score

# Negative Score: This score is calculated by assigning the value of -1
# for each word if found in the Negative Dictionary and then adding up all
# the values. We multiply the score with -1 so that the score is a
# positive number.
# 

# In[45]:


# List_of_Negative_words=  sheet_positive_negetive_stop_words_constrain_uncertanity_words['Negative_words'].dropna()
# Negative_score = count(list_of_words_after_stop_words,List_of_Negative_words)
# Negative_score


# # uncertainty_score

# In[46]:


# sheet_positive_negetive_stop_words_constrain_uncertanity_words.columns


# In[47]:


# sheet_positive_negetive_stop_words_constrain_uncertanity_words['Uncertanity_Word'] = sheet_positive_negetive_stop_words_constrain_uncertanity_words['Uncertanity_Word'].str.lower()


# In[48]:


# sheet_positive_negetive_stop_words_constrain_uncertanity_words['Uncertanity_Word'] = sheet_positive_negetive_stop_words_constrain_uncertanity_words['Uncertanity_Word'].str.lower()
# Series_of_uncertanity_words = sheet_positive_negetive_stop_words_constrain_uncertanity_words['Uncertanity_Word'].dropna()
# uncertanity_score = count(list_of_words_after_stop_words,Series_of_uncertanity_words)
# uncertanity_score


# # constraining_score

# In[49]:


# sheet_positive_negetive_stop_words_constrain_uncertanity_words['Constraning_Word']= sheet_positive_negetive_stop_words_constrain_uncertanity_words['Constraning_Word'].str.lower()


# In[50]:


# sheet_positive_negetive_stop_words_constrain_uncertanity_words['Constraning_Word']= sheet_positive_negetive_stop_words_constrain_uncertanity_words['Constraning_Word'].str.lower()
# Series_of_uncertanity_words = sheet_positive_negetive_stop_words_constrain_uncertanity_words['Constraning_Word'].dropna()
# constraining_score =count(list_of_words_after_stop_words,Series_of_uncertanity_words)
# constraining_score


# # Polarity 

# Polarity Score: This is the score that determines if a given text is
# positive or negative in nature. It is calculated by using the formula: 
# 
# Polarity Score = (Positive Score – Negative Score)/ ((Positive Score + Negative Score) + 0.000001)
# Range is from -1 to +1

# In[51]:


def polarity(Positive_score,Negative_score):
    Polarity_Score = (Positive_score-Negative_score)/(Positive_score+Negative_score)+0.000001
    
    return Polarity_Score
    


# In[52]:


# Polarity_Score = polarity(Positive_score,Negative_score)
# Polarity_Score


# # Subjectivity Score

# Subjectivity Score: This is the score that determines if a given text is
# objective or subjective. It is calculated by using the formula: 
# 
# Subjectivity Score = (Positive Score + Negative Score)/ ((Total Words after cleaning) + 0.000001)
# Range is from 0 to +1

# In[53]:


def sub_score(Positive_score,Negative_score):
    Subjectivity_Score = (Positive_score+Negative_score)/(len(clean_test_in_lower_case)) + 0.000001
    return Subjectivity_Score
    


# In[ ]:





# In[54]:


# Subjectivity_Score = sub_score(Positive_score,Negative_score)
# Subjectivity_Score


# # Sentiment score categorization

# 
# This is determined by grouping the Polarity score values in the following groups.
#  
# Most Negative: Polarity Score below -0.5
#  
# Negative: Polarity Score between -0.5 and 0
#  
# Neutral: Polarity Score equal to 0
#  
# Positive: Polarity Score between 0 and 0.5
#  
# Very Positive: Polarity Score above 0.5
# 

# In[55]:


def sent_score(Polarity_Score):
    
    if (Polarity_Score < -.5):
        print("Most Negative: Polarity Score below -0.5  and polarity is : ", Polarity_Score)

    elif(Polarity_Score >= -0.5  and Polarity_Score < 0 ):
        print("Negative: Polarity Score between -0.5 and 0 and polarity is : ", Polarity_Score)
    if (Polarity_Score == 0):
        print("Neutral: Polarity Score equalto 0  and polarity is : ", Polarity_Score)

    elif(Polarity_Score > 0  and Polarity_Score <= .5 ):
        print("Positive: Polarity Score between 0 and 0.5 and polarity is : ", Polarity_Score)

    elif(Polarity_Score > 0.5):
        print("Very Positive: Polarity Score above 0.5 and polarity is : ", Polarity_Score)
   
    
    return Polarity_Score


# In[56]:


#Sentiment score categorization
# sentimental_score =  sent_score(Polarity_Score)


# In[ ]:





# # Average_Sentence_Length

# Average Sentence Length = the number of words / the number of sentences
# 

# In[57]:


def avg_snet_len(Total_no_of_words,Total_no_of_sentence ):
    Average_Sentence_Length = Total_no_of_words/Total_no_of_sentence
    
    return Average_Sentence_Length


# In[58]:


# Average_Sentence_Length
# Average_Sentence_Length =avg_snet_len(Total_no_of_words,Total_no_of_sentence )

# Average_Sentence_Length


# # Tokenize the syllable

# In[59]:


def syllable_tokenizer(list_of_words_after_stop_words):
    
    from nltk.tokenize import SyllableTokenizer
    # Create a reference variable for Class word_tokenize
    tk = SyllableTokenizer()

    # Use tokenize method
    syllable = tk.tokenize(list_of_words_after_stop_words)
    return syllable


# In[60]:


def count_complex_word(list_of_words_after_stop_words):
    list_of_syllable= []

    for word in list_of_words_after_stop_words:
        list_single_word_syllable=[]
        syllable_list = syllable_tokenizer(word)
    #     print(syllable_list)
        list_single_word_syllable.append(syllable_list)
        list_of_syllable.append(list_single_word_syllable)
        
#     print(list_of_syllable)
        
    list_of_count_syllable= []
    for ls in list_of_syllable:
        for co in ls:
            counter = ''
            counter = len(co)
            list_of_count_syllable.append(counter)
#     print(list_of_count_syllable)
    
    Total_No_of_complex_word = 0
    for i in list_of_count_syllable:
        if i > 2:
            Total_No_of_complex_word +=1
    return Total_No_of_complex_word  


# # Complex Word Count

# In[61]:


# Complex Word Count
# Total_No_of_complex_word =count_complex_word(list_of_words_after_stop_words)
# Total_No_of_complex_word


# # Percentage_of_complex_word

# Complex words are words in the text that contain more than two syllables
# 
# Percentage of Complex words = the number of complex words / the number of words 

# In[62]:


def Percentage_of_complex_word(Total_No_of_complex_word,Total_no_of_words):
    Percentage_of_complex_word =  (Total_No_of_complex_word/Total_no_of_words)*100
    return Percentage_of_complex_word


# In[63]:


#Percentage_of_complex_word
# Percentage_of_complex_word = Percentage_of_complex_word(Total_No_of_complex_word,Total_no_of_words)
# Percentage_of_complex_word


# # Fog Index 

# In[64]:


def fog(Average_Sentence_Length , Percentage_of_complex_word):
    
    Fog_Ind = 0.4 * (Average_Sentence_Length + Percentage_of_complex_word)
    return Fog_Ind


# Fog Index = 0.4 * (Average Sentence Length + Percentage of Complex words)

# In[65]:


# Fog Index
# Fog_Index =  fog(Average_Sentence_Length , Percentage_of_complex_word)
# Fog_Index


# # Average Word Length

# Average Word Length is calculated by the formula:
# 
# Sum of the total number of characters in each word/Total number of words

# In[66]:


def avg_word_len(word_count):
    char_counter =0
    for words in clean_test_in_lower_case:
        for char in words:
            char_counter += 1
            
    Avg_len_0f_word= char_counter/word_count
    return Avg_len_0f_word            
    


# In[67]:


# Average Word Length
# Average_word_length=avg_word_len(word_count)
# Average_word_length


# The absolute values of “Positive/Negative Scores” are equal to the number of positive/negative words in each report of 
# 10-Q/K; so the (Loughran-McDonald) positive/negative word proportion can be simply calculated as “Positive/Negative Scores 
# divided by Word Count 

# # Propotion

# In[68]:


def word_prop(score,count):
    proportion = score/count
    return proportion


# # positive_word_proportion

# In[69]:


# positive_word_proportion = word_prop(Positive_score,word_count)
# positive_word_proportion


# # negative_word_proportion

# In[70]:


# negative_word_proportion = word_prop(Negative_score,word_count)
# negative_word_proportion


# # uncertainty_word_proportion

# In[71]:


# uncertainty_word_proportion = word_prop(uncertanity_score,word_count)
# uncertainty_word_proportion


# # constraining_word_proportion

# In[72]:


# constraining_word_proportion =word_prop(constraining_score,word_count)
# constraining_word_proportion


# # constraining_words_whole_report

# In[73]:


constraining_words_whole_report = ''


# par = 'html.parser'
# 
# 
# 
# 
# data = establish_connection()
# print(data.status_code)
# 
# input_data_content = data.content
# 
# soup = BeautifulSoup_data(input_data_content,par)
# 
# text_from_report = get_text_from_report(soup)
# 
# tag_name = search_by_tag(soup)
# 
# w_token = word_token(text_from_report)
# 
# s_token = sen_token(text_from_report)
# 
# # No. of sentence
# Total_no_of_sentence=total_no_of_sentence(s_token)
# 
# # filer text using regx 
# clean_test_in_lower_case = filter_word_using_re(w_token)
# 
# 
# # total No. of words after removing not text character 
# Total_no_of_words =  Total_No_of_Words_after_removing_Non_text_character(clean_test_in_lower_case)
# 
# 
# # ........................
# # word_count 
# list_of_words_after_stop_words = sheet_positive_negetive_stop_words_constrain_uncertanity_words['Stop_Words'].dropna()
# word_count = count_words(list_of_words_after_stop_words)
# word_counter.append(word_count)
# 
# 
# 
# #.......................
# # Positive score 
# List_of_Posative_words=  sheet_positive_negetive_stop_words_constrain_uncertanity_words['Posative_Words'].dropna()
# Positive_score = count(list_of_words_after_stop_words,List_of_Posative_words)
# pos_score.append(Positive_score)
# 
# 
# 
# 
# #.......................
# #Negative score
# List_of_Negative_words=  sheet_positive_negetive_stop_words_constrain_uncertanity_words['Negative_words'].dropna()
# Negative_score = count(list_of_words_after_stop_words,List_of_Negative_words)
# neg_score.append(Negative_score)
# 
# #..........................
# # Polarity 
# Polarity_Score = polarity(Positive_score,Negative_score)
# pol_score.append(Polarity_Score)
# 
# 
# #..........................
# # Average_Sentence_Length
# Average_Sentence_Length =avg_snet_len(Total_no_of_words,Total_no_of_sentence )
# avg_sen_len.append(Average_Sentence_Length)
# 
# 
# 
# # .........................
# # Complex Word Count
# Total_No_of_complex_word =count_complex_word(list_of_words_after_stop_words)
# complex_wor_count.append(Total_No_of_complex_word)
# 
# #..........................
# #Percentage_of_complex_word
# Percentage_of_complex_word = Percentage_of_complex_word(Total_No_of_complex_word,Total_no_of_words)
# percentage_of_com_words.append(Percentage_of_complex_word)
# 
# 
# #...........................
# # Fog Index
# Fog_Index =  fog(Average_Sentence_Length , Percentage_of_complex_word)
# f_ind.append(Fog_Index)
# 
# 
# #........................
# # uncertanity score
# sheet_positive_negetive_stop_words_constrain_uncertanity_words['Uncertanity_Word'] = sheet_positive_negetive_stop_words_constrain_uncertanity_words['Uncertanity_Word'].str.lower()
# Series_of_uncertanity_words = sheet_positive_negetive_stop_words_constrain_uncertanity_words['Uncertanity_Word'].dropna()
# uncertanity_score = count(list_of_words_after_stop_words,Series_of_uncertanity_words)
# uncer_score.append(uncertanity_score)
# 
# 
# #.........................
# # constraning score
# sheet_positive_negetive_stop_words_constrain_uncertanity_words['Constraning_Word']= sheet_positive_negetive_stop_words_constrain_uncertanity_words['Constraning_Word'].str.lower()
# Series_of_uncertanity_words = sheet_positive_negetive_stop_words_constrain_uncertanity_words['Constraning_Word'].dropna()
# constraining_score =count(list_of_words_after_stop_words,Series_of_uncertanity_words)
# const_score.append(constraining_score)
# 
# 
# 
# # selectivity score
# Subjectivity_Score = sub_score(Positive_score,Negative_score)
# 
# #Sentiment score categorization
# sentimental_score =  sent_score(Polarity_Score)
# 
# # Average Word Length
# Average_word_length=avg_word_len(word_count)
# 
# 
# 
# #..................................
# # positive_word_proportion
# positive_word_proportion = word_prop(Positive_score,word_count)
# pos_wor_prop.append(positive_word_proportion)
# 
# 
# #..................................
# # negative_word_proportion
# negative_word_proportion = word_prop(Negative_score,word_count)
# neg_wor_prop.append(negative_word_proportion)
# 
# 
# #.................................
# # uncertainty_word_proportion
# uncertainty_word_proportion = word_prop(uncertanity_score,word_count)
# uncer_wor_prop.append(uncertainty_word_proportion)
# 
# 
# # ................................
# # constraining_word_proportion
# constraining_word_proportion =word_prop(constraining_score,word_count)
# cons_wor_prop.append(constraining_word_proportion)
# 
# #..................................
# # constraining_words_whole_report
# constraining_words_whole_report = ''
# constraning_words_whole_report.append(constraining_words_whole_report)
# 

# In[74]:


read_exc= pd.read_excel('cik_list.xlsx')
read_exc


# In[75]:


read_exc['compet_link'].dropna()


# In[76]:


web_link=  read_exc['compet_link'].dropna().to_list()


# In[77]:


# type(data_set)


# In[78]:


web_link


# In[79]:


par = 'html.parser'

for link in web_link:
    print(link)
    print(type(link))

    data = establish_connection(link)
    print(data.status_code)
    
#     break

    input_data_content = data.content

    soup = BeautifulSoup_data(input_data_content,par)

    text_from_report = get_text_from_report(soup)

    tag_name = search_by_tag(soup)

    w_token = word_token(text_from_report)

    s_token = sen_token(text_from_report)

    # No. of sentence
    Total_no_of_sentence=total_no_of_sentence(s_token)

    # filer text using regx 
    clean_test_in_lower_case = filter_word_using_re(w_token)


    # total No. of words after removing not text character 
    Total_no_of_words =  Total_No_of_Words_after_removing_Non_text_character(clean_test_in_lower_case)


    # ........................
    # word_count 
    list_of_words_after_stop_words = sheet_positive_negetive_stop_words_constrain_uncertanity_words['Stop_Words'].dropna()
    word_count = count_words(list_of_words_after_stop_words)
    word_counter.append(word_count)



    #.......................
    # Positive score 
    List_of_Posative_words=  sheet_positive_negetive_stop_words_constrain_uncertanity_words['Posative_Words'].dropna()
    Positive_score = count(list_of_words_after_stop_words,List_of_Posative_words)
    pos_score.append(Positive_score)




    #.......................
    #Negative score
    List_of_Negative_words=  sheet_positive_negetive_stop_words_constrain_uncertanity_words['Negative_words'].dropna()
    Negative_score = count(list_of_words_after_stop_words,List_of_Negative_words)
    neg_score.append(Negative_score)

    #..........................
    # Polarity 
    Polarity_Score = polarity(Positive_score,Negative_score)
    pol_score.append(Polarity_Score)


    #..........................
    # Average_Sentence_Length
    Average_Sentence_Length =avg_snet_len(Total_no_of_words,Total_no_of_sentence )
    avg_sen_len.append(Average_Sentence_Length)



    # .........................
    # Complex Word Count
    Total_No_of_complex_word =count_complex_word(list_of_words_after_stop_words)
    complex_wor_count.append(Total_No_of_complex_word)

    #..........................
    #Percentage_of_complex_word
    Percentage_of_complex_w = Percentage_of_complex_word(Total_No_of_complex_word,Total_no_of_words)
    percentage_of_com_words.append(Percentage_of_complex_w)


    #...........................
    # Fog Index
    Fog_Index =  fog(Average_Sentence_Length , Percentage_of_complex_w)
    f_ind.append(Fog_Index)


    #........................
    # uncertanity score
    sheet_positive_negetive_stop_words_constrain_uncertanity_words['Uncertanity_Word'] = sheet_positive_negetive_stop_words_constrain_uncertanity_words['Uncertanity_Word'].str.lower()
    Series_of_uncertanity_words = sheet_positive_negetive_stop_words_constrain_uncertanity_words['Uncertanity_Word'].dropna()
    uncertanity_score = count(list_of_words_after_stop_words,Series_of_uncertanity_words)
    uncer_score.append(uncertanity_score)


    #.........................
    # constraning score
    sheet_positive_negetive_stop_words_constrain_uncertanity_words['Constraning_Word']= sheet_positive_negetive_stop_words_constrain_uncertanity_words['Constraning_Word'].str.lower()
    Series_of_uncertanity_words = sheet_positive_negetive_stop_words_constrain_uncertanity_words['Constraning_Word'].dropna()
    constraining_score =count(list_of_words_after_stop_words,Series_of_uncertanity_words)
    const_score.append(constraining_score)



    # selectivity score
    Subjectivity_Score = sub_score(Positive_score,Negative_score)

    #Sentiment score categorization
    sentimental_score =  sent_score(Polarity_Score)

    # Average Word Length
    Average_word_length=avg_word_len(word_count)



    #..................................
    # positive_word_proportion
    positive_word_proportion = word_prop(Positive_score,word_count)
    pos_wor_prop.append(positive_word_proportion)


    #..................................
    # negative_word_proportion
    negative_word_proportion = word_prop(Negative_score,word_count)
    neg_wor_prop.append(negative_word_proportion)


    #.................................
    # uncertainty_word_proportion
    uncertainty_word_proportion = word_prop(uncertanity_score,word_count)
    uncer_wor_prop.append(uncertainty_word_proportion)


    # ................................
    # constraining_word_proportion
    constraining_word_proportion =word_prop(constraining_score,word_count)
    cons_wor_prop.append(constraining_word_proportion)

    #..................................
    # constraining_words_whole_report
    constraining_words_whole_report = ''
    constraning_words_whole_report.append(constraining_words_whole_report)


# In[ ]:


print(pos_score,neg_score,pol_score,avg_sen_len,percentage_of_com_words,
      f_ind,complex_wor_count,word_counter,uncer_score ,
      const_score ,pos_wor_prop,neg_wor_prop,uncer_wor_prop,
      cons_wor_prop,constraning_words_whole_report)


# # Crete Data Frame as Dict

# In[80]:


d_set =   {'CIK' : CIK1,
          'CONAME' : CONAME1,
          'FYRMO': FYRMO1,
          'FDATE': FDATE1,
          'FORM': FORM1,
           'SECFNAME' : SECFNAME1,
          'positive_score' :pos_score,
          'negative_score': neg_score ,
          'polarity_score' :pol_score,
          'average_sentence_length' : avg_sen_len,
          'percentage_of_complex_words': percentage_of_com_words,
          'fog_index' : f_ind,
          'complex_word_count' : complex_wor_count,
          'word_count' : word_counter,
          'uncertainty_score': uncer_score,
          'constraining_score': const_score,
          'positive_word_proportion' : pos_wor_prop,
          'negative_word_proportion' : neg_wor_prop,
          'uncertainty_word_proportion': uncer_wor_prop,
          'constraining_word_proportion' : cons_wor_prop,
          'constraining_words_whole_report' : constraning_words_whole_report
          }


# In[81]:


data_set = pd.DataFrame.from_dict(d_set, orient='index')
Final_data_set= data_set.transpose()
Final_data_set


# In[82]:





# In[83]:





# In[84]:


Final_data_set


# # Export_to_scv

# In[85]:


export_to_csv= Final_data_set.to_csv('Final_data_set.csv')


# In[ ]:




