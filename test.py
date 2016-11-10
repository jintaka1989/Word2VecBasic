v1 = dictionary.search_vector_from_word("i")
v2 = dictionary.search_vector_from_word("am")
v3 = dictionary.search_vector_from_word("he")
sub_v = v2-v1
v4 = v3+sub_v
dictionary.search_word_from_vector(v4)
dictionary.search_words_rankings_from_vector(v4)
