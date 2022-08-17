import nltk
# nltk.download()
# nltk.download('punkt')

paragraph = "Nature is an important and integral part of mankind. It is one of the greatest blessings for human life; " \
            "however, nowadays humans fail to recognize it as one. Nature has been an inspiration for numerous poets, " \
            "writers, artists and more of yesteryears. This remarkable creation inspired them to write poems and stories " \
            "in the glory of it. They truly valued nature which reflects in their works even today. Essentially, nature is " \
            "everything we are surrounded by like the water we drink, the air we breathe, the sun we soak in, the birds we " \
            "hear chirping, the moon we gaze at and more. Above all, it is rich and vibrant and consists of both living and " \
            "non-living things. Therefore, people of the modern age should also learn something from people of yesteryear and " \
            "start valuing nature before it gets too late."
print(len(nltk.sent_tokenize(paragraph)))
print(len(nltk.word_tokenize(paragraph)))