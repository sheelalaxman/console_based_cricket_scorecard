import urllib.request as req 
import json

x=req.urlopen('http://cricapi.com/api/cricket/?apikey=I6wNZPIIr0PcJZrDMSw8lSFCbTA2')
js =json.load(x)
descdic={}
titledic={}
for data in js['data']:
	 descdic[data['unique_id']]=data['description']
	 titledic[data['unique_id']]=data['title']  
    
#print('{}\n\n\n\n{}\n\n\n\n{}\n'.format(uniqueid,description,title))  
def main():

    print("current matches are:\n")
    print("matchid\t\t\tdescription\t\t\ttitle\n\n")

    for x in descdic.keys():
	    print('{}\t\t\t{}\t\t\t'.format(x,descdic[x]))

    id=input("enter the match id for score card:")
    url='http://cricapi.com/api/cricketScore?apikey=I6wNZPIIr0PcJZrDMSw8lSFCbTA2&&unique_id='+str(id)
    x= req.urlopen(url)
    score_info = json.load(x)

    if score_info['matchStarted']:
        print(score_info['team-1'],"Vs",score_info['team-2'])
        print('match started:{}'.format(score_info['matchStarted']))
        print(score_info['score'])
        #print(score_info['innings-requirement'])
    else:
         print('match started:{}'.format(score_info['matchStarted']))    

if __name__=="__main__":
    main()