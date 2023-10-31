import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd
from user_agent import generate_user_agent

st.set_page_config(
    page_title="Review Scraper",
    page_icon=":star2:",
    #layout="wide",
)   

hide_style = """
        <style>
        header {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_style,unsafe_allow_html=True)

gif_path1 = "Animation1.gif"
gif_path2 = "Animation2.gif"
star1_path = "star1.gif"
star2_path = "star2.gif"
star3_path = "star3.gif"
star4_path = "star4.gif"
star5_path = "star5.gif"

col1,col2,col3 = st.columns(3)
with col1:
    st.image(gif_path1)
with col2:
    st.image(gif_path2)
with col3:
    st.image(gif_path1)

user_agent = generate_user_agent()
options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--headless')
options.add_argument('--start-maximized')
options.add_argument('--window-size=1920,1080')
options.add_argument("--no-sandbox")
options.add_argument("--incognito")
options.add_argument(f"user-agent={user_agent}")

def get_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type="chromium").install()), options=options)
    
driver = get_driver()

st.title("Trendyol Review Scraper")
url = st.text_input("Enter Trendyol Product Review URL:")

col1, col2 = st.columns(2)
with col1:
    on = st.toggle("Purchased from this seller")
with col2:
    on1 = st.toggle("Sort from newest to oldest.")


x = st.slider("The higher the value, the more review it attracts, but the waiting time increases.", min_value=5, max_value=200, value=20)

Stars = [":star:", ":star:"*2, ":star:"*3, ":star:"*4, ":star:"*5]
Star = st.radio("Select how many stars of reviews you want to fetch.",Stars)

start_time = time.time()
progress_bar=st.progress(0)

if st.button("Get the Data"):
    with st.spinner("The process is ongoing..."):
        if url:       
            wait= WebDriverWait(driver,15)
            df = []
            try:
                driver.get(url)
                driver.maximize_window()
                time.sleep(6)
                element = driver.find_element(By.TAG_NAME, "h1")
                web_page_title = element.text                
                st.subheader(f"{web_page_title}")
                if on:
                    time.sleep(3)
                    SelectSeller = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.sc")))
                    SelectSeller.click()
                else:
                    pass
                if on1:
                    Sort = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="rating-and-review-app"]/div/div/div/div[3]/div/div/div[2]/div/div[2]/div/div/div/div')))
                    Sort.click()
                    time.sleep(1)
                    NewReviews =wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="rating-and-review-app"]/div/div/div/div[3]/div/div/div[2]/div/div[2]/div/div/ul/li[2]')))
                    NewReviews.click()
                    time.sleep(3)
                else:
                    Sort = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="rating-and-review-app"]/div/div/div/div[3]/div/div/div[2]/div/div[2]/div/div/div/div')))
                    Sort.click()
                    time.sleep(1)
                    OldReviews =wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="rating-and-review-app"]/div/div/div/div[3]/div/div/div[2]/div/div[2]/div/div/ul/li[3]')))
                    OldReviews.click()
                    time.sleep(3)
                if Star == Stars[0]:
                    yildiz1=driver.execute_script('return document.querySelector("#rating-and-review-app > div > div > div > div:nth-child(1) > div > div.ps-stars > div.styles-module_sliderBase__swkx1 > div.styles-module_slider__o0fqa > div:nth-child(5)")')
                    yildiz1.click()
                    time.sleep(3)
                    Review="1-star-reviews"
                    st.image(star1_path)
                if Star == Stars[1]:
                    yildiz2=driver.execute_script('return document.querySelector("#rating-and-review-app > div > div > div > div:nth-child(1) > div > div.ps-stars > div.styles-module_sliderBase__swkx1 > div.styles-module_slider__o0fqa > div:nth-child(4)")')
                    yildiz2.click()
                    time.sleep(3)
                    Review="2-star-reviews"
                    st.image(star2_path)
                if Star == Stars[2]:
                    yildiz3=driver.execute_script('return document.querySelector("#rating-and-review-app > div > div > div > div:nth-child(1) > div > div.ps-stars > div.styles-module_sliderBase__swkx1 > div.styles-module_slider__o0fqa > div:nth-child(3)")')
                    yildiz3.click()
                    time.sleep(3)
                    Review="3-star-reviews"
                    st.image(star3_path)
                if Star == Stars[3]:
                    yildiz4=driver.execute_script('return document.querySelector("#rating-and-review-app > div > div > div > div:nth-child(1) > div > div.ps-stars > div.styles-module_sliderBase__swkx1 > div.styles-module_slider__o0fqa > div:nth-child(2)")')
                    yildiz4.click()
                    time.sleep(3)
                    Review="4-star-reviews"
                    st.image(star4_path)
                if Star == Stars[4]:
                    yildiz5=driver.execute_script('return document.querySelector("#rating-and-review-app > div > div > div > div:nth-child(1) > div > div.ps-stars > div.styles-module_sliderBase__swkx1 > div.styles-module_slider__o0fqa > div:nth-child(1)")')
                    yildiz5.click()
                    time.sleep(3)
                    Review="5-star-reviews"
                    st.image(star5_path)
                g=1
                a=1
                for g in range(1,x+1):
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(1)
                    driver.execute_script("window.scrollBy(0, -6000);") 
                    time.sleep(1)
                    progress_bar.progress(g/x)
                    try:
                        CheckElement=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="rating-and-review-app"]/div/div/div/div[3]/div/div/div[3]/div[2]/div[' + str(a) + ']/div[2]')))
                        a=a+10
                        if CheckElement is not None:
                            continue
                    except:
                        break
                progress_bar.empty()
                page_source = driver.page_source
                soup = BeautifulSoup(page_source, 'html.parser')
                comment_elements = soup.find_all(class_='comment')
                count=len(comment_elements)
                st.success(f"{count} reviews found.", icon="✅")
                for element in comment_elements:
                    paragraph = element.find('p')
                    if paragraph:
                        df.append(paragraph.get_text())
                Review_df = pd.DataFrame(df, columns=["reviews"])
                st.dataframe(Review_df)
                try:
                    Review_df.to_excel(f"{Review}.xlsx", index=False) 
                    Excel_Name = f"{Review}.xlsx"
                    with open(Excel_Name, "rb") as File:
                        st.download_button(
                            label=f"Download the Data",
                            data=File,
                            file_name=Excel_Name,
                        )
                        st.balloons()   
                except Exception as e:
                    st.warning(e)
                st.success("The data has been processed successfully.", icon="✅")            
            except Exception as e:
                st.warning(e)
                st.warning("Something is wrong.",icon="⚠️")
            finally:
                driver.quit()
                end_time = time.time()
                elapsed_time = end_time - start_time
                elapsed_minutes = elapsed_time / 60
                st.write(f"The program lasted for {elapsed_minutes:.2f} minutes.")
                st.stop()      
        else:
            st.warning("Please enter a URL.", icon="⚠️")
            st.stop()   
st.markdown(
    """
    <div style="background-color: rgba(0, 0, 0, 0); padding: 10px; text-align: center;">
        <p style="color: #555;">This application has been created by Ibrahim Ugurca </p>
    </div>
    """,
    unsafe_allow_html=True
)


