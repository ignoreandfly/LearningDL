import pandas as pd

def create_unigram(sentences):
  "Input: List containing sentences, Output: Unigram dataframe"
  dc = {}

  for sentence in sentences:
    for word in sentence.split(' '):
      if word in dc.keys():
        dc[word]+=1
      else:
        dc[word] = 1
  unigram_df = pd.DataFrame(dc, index=['Count'])
  return unigram_df

def create_bigram(sentences):
  "Input: List containing sentences, Output: Bigram dataframe"
  dc_bigram = {}
  for sentence in sentences:
    temp_sentence = sentence.split(' ')
    for i in range(len(temp_sentence)-1):
      if (temp_sentence[i] + " " + temp_sentence[i+1]) in dc_bigram.keys():
        dc_bigram[temp_sentence[i] + " " + temp_sentence[i+1]]+=1
      else:
        dc_bigram[temp_sentence[i] + " " + temp_sentence[i+1]] = 1

  dc = create_unigram(sentences)
  count_list = []
  for word_1 in dc.columns:
    word_list = []
    for word_2 in dc.columns:
      if (word_1 + " " + word_2) in dc_bigram.keys():
        word_list.append(dc_bigram[word_1 + " " + word_2])
      else:
        word_list.append(0)
    count_list.append(word_list)
  bigram_df = pd.DataFrame(count_list, index=[dc.columns], columns=[dc.columns])
  return bigram_df


### Example
#sentences= ["<s> the sunset is nice </s>", "<s> people watch the sunset </s>", "<s> they enjoy the beautiful sunset </s>"]