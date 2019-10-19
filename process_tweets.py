
from string import ascii_letters


def clean_line(line):
    OldLine = line
    line = list(line);
    OldLine = list(OldLine);

    Counter = 0;
    Erased = 0;

    while (Counter < len(OldLine)):
      if OldLine[Counter] in ascii_letters:
        line[Counter-Erased] = OldLine[Counter].lower();
      else:
        if (OldLine[Counter] != " "):
          if(OldLine[Counter] != "@"):
            if(OldLine[Counter] != "#"):
              del(line[Counter-Erased]);
              Erased += 1;
      Counter += 1;


    line = "".join(line);
    return line


def get_tweet_text(line):
    line = line.split(",");
    line = line[1];
    return line


def read_stopwords():
    PieceOfPaper = open("stopwords.txt", "r");
    Lines = [];
    Lines = PieceOfPaper.readlines();

    CorrectedLines = [];

    Counter = 0;

    while(Counter < len(Lines)):
        CorrectedLines.append(Lines[Counter].replace("\n", ""));
        Counter += 1;

    PieceOfPaper.close();
    return CorrectedLines


def process_tweet_text(text):
    stopwords = read_stopwords()
    words = clean_line(text).split()
    result = []
    wordsGuide = clean_line(text).split();

    Counter0 = 0;
    Erased = 0;
    while (Counter0 < len(wordsGuide)):
        Counter1 = 0;
        while (Counter1 < len(stopwords)):
            if wordsGuide[Counter0] == stopwords[Counter1]:
                del(words[Counter0-Erased]);
                Erased += 1;
            Counter1 += 1;
        Counter0 += 1;
    result = words;

    return result


def process_tweet_file(file_name):
    word_freqs = {}
    with open(file_name, encoding='utf-8') as tweets:
        for line in tweets:
            text = get_tweet_text(line)
            words = process_tweet_text(text)
            for  word in words:
                if word not in word_freqs:
                    word_freqs[word] = 1;
                else:
                    word_freqs[word] += 1;
    return word_freqs


def print_statistics(word_freqs):
    Cardinal = 0;
    for  word in word_freqs:
                Cardinal += 1;
    Last = "nope";
    LastFreq = 0;
    for  word in word_freqs:
                if word_freqs[word] > LastFreq:
                    Last = word;
                    LastFreq = word_freqs[word];

    print('The total number of words is:', str(Cardinal));
    print('The total number of different words is:',
          str(len(word_freqs)));
    print('The most frequent word is:', Last);
    print('With a frequency of:', str(word_freqs[Last]));


def write_words(word_freqs, file_name):
    FreqsSheet = open("words.txt", "w", encoding="utf-8");
    for  word in word_freqs:
               DownAllTheDays = str(word)+" "+str(word_freqs[word])+"\n";
               FreqsSheet.write(DownAllTheDays);
    FreqsSheet.close();

wf = process_tweet_file('tweets.txt')
print_statistics(wf)
write_words(wf, 'words.txt')
