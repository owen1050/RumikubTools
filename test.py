t = ['bl1 0','bl2 1','bl3 2','bl4 3','bl5 4','bl6 5','bl7 6','bl8 7','bl9 8','bl10 9','bl11 10','bl12 11','bl13 12','bk1 13','bk2 14','bk3 15','bk4 16','bk5 17','bk6 18','bk7 19','bk8 20','bk9 21','bk10 22','bk11 23','bk12 24','bk13 25','or1 26','or2 27','or3 28','or4 29','or5 30','or6 31','or7 32','or8 33','or9 34','or10 35','or11 36','or12 37','or13 38','re1 39','re2 40','re3 41','re4 42','re5 43','re6 44','re7 45','re8 46','re9 47','re10 48','re11 49','re12 ','re13 ']
for i in t:
    i0 = i.find(" ")
    print("\"" + i[:i0] + "\"", end = ",")