from bs4 import BeautifulSoup
import requests
import webbrowser

def findJobs(URL):
    page = requests.get(URL)

    soup = BeautifulSoup(page.content,'html.parser')
    result = soup.find(id='resultsCol')
    jobs = result.find_all(class_='jobtitle turnstileLink')
    joblist=[]
    index=0
    for job in jobs:
        print(index,': ',job.findAll(text=True),end='\n')
        joblist.append('https://ca.indeed.com'+job['href'])
        index+=1
    return joblist

def openJob(returnedJobList):
    userChoice=0
    while(userChoice!='n'):
        print('\n\ninput the index to the job listing')
        print('type n to end the search')
        userChoice = input()
        if userChoice!='n':
            webbrowser.open(returnedJobList[int(userChoice)])

def main():
    URL = 'https://ca.indeed.com/Web-Developer-jobs-in-Montr%C3%A9al,-QC'
    
    returnedJobList = findJobs(URL)
    openJob(returnedJobList)
    
    


if __name__ == "__main__":
    main()