"""
    desc: A basic web scrapper that fetches the developper job listings from indeed
    author: Ka-son Chau
    last updated: 2020-03-21
    2020-03-20 update: v.1.0 of the script
    2020-03-21 update: added next page feature
"""

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
        print(index,': ',job.findAll(text=True),'\n')
        joblist.append('https://ca.indeed.com'+job['href'])
        index+=1
    return joblist

def openJob(returnedJobList,URL):
    userChoice=0
    jobListToShow = returnedJobList
    baseURL = URL
    pageURL = 'https://ca.indeed.com/jobs?q=Web+Developer&l=Montr%C3%A9al%2C+QC&start='
    pageIndex = 0
    while(userChoice!='n'):
        print('\n\ninput the index to the job listing')
        print('type n to end the search / "d" for next page')
        userChoice = input()
        if userChoice == 'n':
            break
        elif userChoice == 'd':
            pageIndex+=1
            jobListToShow = findJobs(pageURL+str(pageIndex*10))
        else:
            webbrowser.open(returnedJobList[int(userChoice)])


def main():
    URL = 'https://ca.indeed.com/Web-Developer-jobs-in-Montr%C3%A9al,-QC'
    
    returnedJobList = findJobs(URL)
    openJob(returnedJobList,URL)
    
    


if __name__ == "__main__":
    main()