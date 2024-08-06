from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def search_youtube_for_mac_and_cheese_recipes():
    # Set up the WebDriver (ensure you have the appropriate driver installed)
    driver = webdriver.Chrome()  # You can use other drivers like Firefox, Edge, etc.
    
    # Open YouTube
    driver.get('https://www.youtube.com')

    # Find the search box and perform the search
    search_box = driver.find_element(By.NAME, 'search_query')
    search_box.send_keys('mac and cheese recipes')
    search_box.send_keys(Keys.RETURN)
    
    time.sleep(3)  # Wait for the search results to load

    # Extract video information
    videos = driver.find_elements(By.XPATH, '//ytd-video-renderer')
    video_data = []

    for video in videos:
        try:
            title_element = video.find_element(By.ID, 'video-title')
            title = title_element.get_attribute('title')
            url = title_element.get_attribute('href')
            channel_element = video.find_element(By.XPATH, './/yt-formatted-string[@id="text"]/a')
            channel = channel_element.text
            if url:
                video_data.append({
                    'title': title,
                    'url': url,
                    'channel': channel
                })
        except Exception as e:
            print(f"Skipping video due to error: {e}")
            continue

    driver.quit()
    return video_data

# Example usage
video_data = search_youtube_for_mac_and_cheese_recipes()
for data in video_data:
    print(f"Title: {data['title']}\nURL: {data['url']}\nChannel: {data['channel']}\n")
