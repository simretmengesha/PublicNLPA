
# Bigram formation
# using list comprehension + enumerate() + split()

# initializing list
test_list = ['በሙቀት ጀምሮ በቅዝቃዜ መጨረስ የዚህ ዓለም መገለጫ ሆኗል እልልታ በኡኡታ፣ ሠርግ በግልግል፣ ማሬ የሚለው ቃል እሬቴ በሚልይለወጣል', 'ጨርሰው የማይሰሩ አሳሳቢ አይደሉም፣ አይሠሩምና። ብልሽት ያለባቸው ማሞቂያዎች ግን ሰውዬው ሲሞክራቸው ይሠራሉ ']

# printing the original list
print ("The original list is : " + str(test_list))

# using list comprehension + enumerate() + split()
# for Bigram formation
res = [(x, i.split()[j + 1]) for i in test_list
	for j, x in enumerate(i.split()) if j < len(i.split()) - 1]

# printing result
print ("The formed bigrams are : " + str(res))
