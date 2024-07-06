import feedparser
import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header

# RSS feed URL for Upwork jobs (you'll need to replace this with the correct URL)
FEED_URL = "https://www.upwork.com/ab/feed/jobs/rss?paging=NaN-undefined&q=%22a%22&sort=recency&api_params=1&securityToken=891f2395d7e337f7068820b592fbab7aa0d0a27b040432dbbaefeb9fa41452d9b63c0dd50ee68e5ebb74426c207bbdda0d2351a888a7c4d572f7682687c98790&userUid=1710270497882107904&orgUid=1710270497882107905"

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "jariwalatrial@gmail.com"
SENDER_PASSWORD = "ppmd vize rzml zbir"  # This is your app password
RECIPIENT_EMAIL = "jariwalatrial@gmail.com"

def send_email(subject, body):
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

def check_new_jobs():
    feed = feedparser.parse(FEED_URL)
    latest_entry = feed.entries[0]
    return latest_entry.title, latest_entry.link, latest_entry.published

def main():
    last_job_title = ""
    while True:
        try:
            job_title, job_link, job_date = check_new_jobs()
            if job_title != last_job_title:
                subject = "New Upwork Job Posted"
                body = f"Title: {job_title}\nLink: {job_link}\nDate: {job_date}"
                send_email(subject, body)
                last_job_title = job_title
            time.sleep(1)  # Check every 5 minutes
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            time.sleep(1)  # Wait 5 minutes before retrying

if __name__ == "__main__":
    main()
