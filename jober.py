from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime
import os

# Ensure the directory exists
output_dir = "job_posts"
os.makedirs(output_dir, exist_ok=True)

# Job specific details
def find_jobs():
    try:
        # Fetch the job page again
        url = 'https://isecjobs.com/?reg=7&key=&exp=EN&sal='
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15'}
        html_page = requests.get(url, headers=headers).text

        # Retrieve all open jobs
        soup = BeautifulSoup(html_page, 'lxml')
        jobs = soup.find_all('li', class_='list-group-item list-group-item-action p-1')

        if not jobs:
            print("No jobs found. The site might not have been loaded correctly.")
            return

        # Generate a timestamp for the file name
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        file_name = os.path.join(output_dir, f"jobs_{timestamp}.txt")

        with open(file_name, "w") as f:
            for index, job in enumerate(jobs):
                job_title = job.find('h2', class_='h5 text-body-emphasis text-break mt-1').text.strip()
                company = job.find('p', class_='m-0 text-muted').text.strip()
                requirements = job.find_all('span', class_='badge rounded-pill text-bg-light')
                perks = job.find_all('span', class_='badge rounded-pill text-bg-success')
                salary = job.find('span', class_='badge rounded-pill text-bg-success d-none d-md-inline-block')
                more_info = job.find('a', class_='col pt-2 pb-3')

                job_details = {
                    'Location': job.find('span', class_='d-none d-md-block text-break mb-1').text.strip(),
                    'Perks': [perk.text.strip() for perk in perks],
                    'Requirements': [req.text.strip() for req in requirements]
                }

                f.write(f"Job {index + 1}:\n")
                f.write(f"Company:\t {company}\n")
                f.write(f"Job Title:\t {job_title}\n")
                f.write(f"Location:\t {job_details['Location']}\n")
                f.write(f"Skills:\t\t {', '.join(job_details['Requirements'])}\n")

                # Handle jobs with no salary
                if salary is None:
                    f.write(f"Salary:\t\t Not Specified\n")
                else:
                    f.write(f"Salary:\t\t {salary.text.strip()}\n")

                # Link to job description
                if more_info:
                    link = more_info.get('href')
                    f.write(f"More info:\t https://isecjobs.com{link}\n")

                f.write("\n" + "-"*50 + "\n\n")

        print(f"Jobs written to {file_name}\n")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run program at an interval
if __name__ == "__main__":
    while True:
        print("Starting job fetch...")
        find_jobs()
        waiting_time = 1  # Time in minutes
        print("Sleeping...\n\n")
        time.sleep(waiting_time * 60)

