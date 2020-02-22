school = [{'class': '4a', 'scores': [3,4,4,5,2]},
{'class': '5а', 'scores': [4,5,2]},
{'class': '7в', 'scores': [3,5,2]},
{'class': '10б', 'scores': [3,4,4,5,2]}]

school_avg = 0
for class_ in school:
    print(sum(class_["scores"])/len(class_["scores"]))
    class_avg = sum(class_["scores"])/len(class_["scores"])
    school_avg += class_avg
print(school_avg)
print(school_avg/len(school))
   
# for score in (class_["scores"]):
#     x += score

# y = x/len(class_["scores"])
# print(y)
# school_avg += y
# print(school_avg/len(school))