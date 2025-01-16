import time

from bs4 import BeautifulSoup
import requests
print("What are some skills you are unfamiliar with?")
unfamiliar_skill = input("=>")
print(f"Filtered out {unfamiliar_skill}")


def find_jobs():
    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=Python&txtKeywords=Python&txtLocation=").text
    soup = BeautifulSoup(html_text, "lxml")
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
    for index, job in enumerate(jobs):
        job_published = job.find("span", class_="sim-posted").span.text
        if "few" in job_published:
            company_name = job.find("h3", class_="joblist-comp-name").text.replace(" ", "")
            skills = job.find("span", class_="srp-skills").text.replace(" ", "")
            job_link = job.header.h2.a["href"]
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()}\n")
                    f.write(f"Required skills: {skills.strip()}\n")
                    f.write(f"More info: {job_link}\n")
                print(f"File saved: {index}\n")


if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait*60)
