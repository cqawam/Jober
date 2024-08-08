# Jober
This Python script automates the process of scraping entry-level job listings from the [iSecJobs](https://isecjobs.com/) website.  
The script fetches the latest job postings at regular intervals and writes them to timestamped text files, making it easier to monitor and track job opportunities in the cybersecurity field.

### Features:
- **Automated Scraping**: Continuously fetches job listings at defined intervals.
- **Job Details**: Extract key details such as job title, company, location, required skills, salary, and a direct link to the full job description.
- **Timestamped Files**: Saves job postings to uniquely named files based on the current date and time, allowing for easy tracking and analysis over time.
- **Error Handling**: Includes basic error handling to ensure smooth operation even if issues arise during scraping.

### Usage:
1. **Install Dependencie**s: The script requires `requests` and `BeautifulSoup4`. You can install them via pip:
 ```bash
    pip install requests BeautifulSoup4
 ```
2. **Run the script**
 ```bash
    python jober.py
 ```
3. Check Output: The job postings are saved in the `job_posts` directory, with each file named according to the timestamp of when it was created.

### Customization:
- **Interval Time**: Adjust the `waiting_time` variable to change how frequently the script fetches job listings.
- **Output Directory**: Modify the `output_dir` variable if you wish to save the files to a different location.

### Potential Use Cases:
- **Job Hunting**: Automate the collection of job postings for continuous monitoring of new opportunities.
- **Market Analysis**: Track job trends in the cybersecurity field by regularly collecting data over time.

### Future Improvements:
- **Additional Sites**: Expand the script to scrape from multiple job boards.
- **Data Storage**: Save job data in a structured format like CSV or a database for more advanced analysis.
- **Notification System**: Implement email or SMS notifications when new jobs are posted.
