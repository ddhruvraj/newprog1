# import numpy as np
# from scipy.stats import binom
# import matplotlib.pyplot as plt
# import seaborn as sns
# n=100
# p=0.4
# x=range(0,n)
#
# pmf=binom.pmf(x,n,p)
# # samples[s]=pmf
# print(pmf)
# np.round([pmf],decimals=2)
#
# plt.hist(pmf)
# plt.show()
str1="BANANA"
the_vowel=["a","e","i","o","u"]
res = [str1[i: j] for i in range(len(str1))
          for j in range(i + 1, len(str1) + 1)]

# res1="\n".join(res)
# print(res)
new_res=[]
new_res2=[]
new_res3=[]
# for remove words with vowel
for i in range(len(res)):
        # print(res[i])
    word_list=list(res[i])
    if word_list[0].lower() in the_vowel:
        new_res3.append(res[i])
    else:
        new_res.append(res[i])

# print(new_res)
# for remove duplicates
# count=0
for i in range(len(new_res)):
    if new_res[i] in new_res:
        if new_res[i] not in new_res2:
            new_res2.append(new_res[i])
            # count+=1
# print(new_res2)
# print(count)



# print(new_res3)
list4=[]
for i in range(len(new_res3)):
    if new_res3[i] in new_res3:
        if new_res3[i] not in list4:
            list4.append(new_res3[i])

# print(list4)
# print(len(list4))

if len(list4)<len(new_res2):
    print(f"stuart {len(new_res2)}")
else:
    print(f"kevin {len(list4)}")
