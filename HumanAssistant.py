import os
import nltk
from nltk.tokenize import word_tokenize
import spacy

nlp=spacy.load('en_core_web_md')

#get verb position from user query
def get_verb_position(doc):
    tag_list=[]
    for t in doc:
        tag_list.append(t.tag_)
    if 'VB' in tag_list:
        return tag_list.index('VB')
    return -1

#get list of possible commands from user query
def get_possible_commands(verb_position,text):
    temp_list=text.split()[verb_position+1:]
    commands_list=[]
    if len(temp_list)>1:
        unigram=temp_list[0]
        bigram=' '.join(temp_list[0:2])
        commands_list.append(unigram)
        commands_list.append(bigram)
    else:
       commands_list.append(temp_list[0])
    return commands_list


while True:
    input_str=input("How can i help you (type \"exit\" to quit):").lower()
    if 'exit' not in input_str:
        document=nlp(input_str)
        word_list=input_str.split()
        verb_position=get_verb_position(document)
        if verb_position!=-1 and len(word_list)>2:
            command_list=get_possible_commands(verb_position,input_str)
            counter=1
            for command in command_list:
                status_code=os.system(command)
                counter=counter+1
                if status_code!=0:
                    if counter>len(command_list):
                        print('Command not recognized from your input')
                    continue
                else:
                    break
            continue
        else:
            status_code=os.system(input_str)
            if status_code==0:
                continue
            else:
                print('Command not recognized')
            continue
    else:
        print('Good day..Bye!!')
        break