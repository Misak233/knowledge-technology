There are three docs in this code file.

Train.py: this doc is used to recognize blend words from the candidates, it includes two restriction functions which are: repeat and interp[1].

fine_blend.py: this doc is used to find component words for each blends, it includes three ways of calculate similarity which are : global distance[3], jaro-winkler[4] and N-gram[2]. You can change it by choose the cal_dis functions. And some insights about finding restrictions of component words (like find words start with two same letters) come from [1].

compare.py: this doc is used to calculate the evaluation metrics which contains: precision and recall

Citation:
[1]Cook, P., & Stevenson, S. (2010). Automatically identifying the source words of lexical blends in English. Computational Linguistics, 36(1), 129-149.
[2] Steven Bird and Liling Tan. Natural Language Toolkit from "https://www.nltk.org/" 
[3] Michaël Meyer. Editdistance from "https://pypi.org/project/Distance/"
[4]Jean-Bernard Ratte. Jaro Winkler from "https://pypi.org/project/pyjarowinkler/"