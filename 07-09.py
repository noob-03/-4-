import operator

trainDic, trainList = {},[]

trainDic =  { 'Thomas' : '토마스', 'Edward' : '에드워드', 'Henry' : '헤리', 'Gothen': '고든' , 'Janes' : '제임스' }

trainList = sorted(trainDic.items(),key = operator.itemgetter(0))

print(trainList)