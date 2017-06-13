# -*- coding: utf-8 -*-
import json
import time
import io
def loadJsonObjectToDict(filename):
    f = io.open(filename,'r',encoding='utf-8')
    totalLine, errorLine = 0, 0
    critics = {}
    start_time = time.time()
    for line in f:
        try:
            new_line = line.decode('unicode_escape')
        except:
            new_line = line
        new_line.replace(r'\\\\',r'/')
        totalLine += 1
        if (new_line[-2:-1] == ',') :
            # print('new line is {}'.format(new_line[:len(new_line)-2]))
            new_line = new_line[:-2]
        # if (line != line.decode('unicode_escape')) :
        #     print(line)
        #     print(line.decode('unicode_escape'))

        try:
            readDict = json.loads(new_line)
            booklist = readDict['bookList']
            nestedDict = {}
            for book in booklist:
                nestedDict[book['name']] = book['noteInBooklist']
            if readDict['publisher'] not in critics:
                critics[readDict['publisher']] = nestedDict
            else:
                critics[readDict['publisher']].update(nestedDict)
        except Exception as e:
            errorLine += 1
            print("Error @Line " + str(totalLine))
            print(e)
            # print(new_line)
    print (str(totalLine - errorLine) + "/" + str(totalLine) + " has been loaded into critics dict")
    print ("Num of elements in dict:" + str(len(critics)))
    print ("Load time:" + str(time.time() - start_time))
    return critics

#Test
def main():
    testDict = loadJsonObjectToDict("./data/test.json")
    for key, value in testDict[u'最爱小花花'].items():
        print (key + ":" + str(value))

if __name__ == '__main__':
    main()


