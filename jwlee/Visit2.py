import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# ChromeDriver 설정 
options = uc.ChromeOptions()
options.add_argument("--start-maximized")
driver = uc.Chrome(options=options)

try:
    # 구글 로그인 페이지로 이동
    driver.get('https://accounts.google.com/')

    # 로그인 정보 입력 및 로그인
    email_input = driver.find_element(By.ID, 'identifierId')
    email_input.send_keys('your-email@gmail.com')
    email_input.send_keys(Keys.RETURN)
    time.sleep(7)  # 대기

    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys('your-password')
    password_input.send_keys(Keys.RETURN)
    time.sleep(7)  # 대기

    # 유튜브 시청기록 페이지로 이동
    driver.get('https://www.youtube.com/feed/history')
    time.sleep(7)  # 대기

    # 시청기록 스크롤 및 데이터 수집
    SCROLL_PAUSE_TIME = 2
    last_height = driver.execute_script("return document.documentElement.scrollHeight")

    while True:
        # 페이지 끝까지 스크롤
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

        # 페이지 로드 대기
        time.sleep(SCROLL_PAUSE_TIME)

        # 새로운 스크롤 높이 가져오기
        new_height = driver.execute_script("return document.documentElement.scrollHeight")

        # 더 이상 스크롤이 진행되지 않으면 종료
        if new_height == last_height:
            break
        last_height = new_height

    # 비디오 제목과 채널명 추출
    videos = driver.find_elements(By.TAG_NAME, 'ytd-video-renderer')

    for video in videos:
        title = video.find_element(By.ID, 'video-title').text
        channel = video.find_element(By.XPATH, './/yt-formatted-string[@id="text" and @class="style-scope ytd-channel-name"]').text
        print(f"Title: {title}, Channel: {channel}")

    print("스크롤 및 데이터 수집 완료d")

finally:
    driver.quit()
