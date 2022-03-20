from zhon.hanzi import punctuation
from opencc import OpenCC

cc = OpenCC('t2s')
length = 5
str = '留下三分暖別人，這是母親常掛在嘴邊的話，也是母親一生堅守的生活準則。記得我們小時候，母親種地時，喜歡剩下一壟不播種，她說種得太靠邊了容易和別人的莊稼混在一起，引起不必要的爭執，最重要的是，如果自家種了玉米，別人家種了花生，會影響別人的莊稼生長。所以母親在家種地十多年，從來沒有因為地界和別人發生過爭執，相反的常有人熱心幫助母親耕犁播種。'
punctuation_str = punctuation
for i in punctuation:
    str = str.replace(i, '\n') #以標點符號斷行
print(str)
cut = '\n' #以換行作為分割的基礎
lst = [] #儲存總共有多少換行符號的索引值
for pos,char in enumerate(str):
    if(char == cut):
        lst.append(pos) #將每出現一個\n就算進索引符號
print(lst)
print(str[0:lst[length-1]]) #擷取使用者輸入的行數
print(cc.convert(str))