from selenium import webdriver
import time, sys, os, json

github_username = ''
github_password = ''

with open(r"C:\Projects\cli-commands\creds.json", 'r') as f:
  creds = json.load(f)
  github_username = creds['github']['username']
  github_password = creds['github']['password']

driver = webdriver.Chrome('C:\\Projects\\chromedriver.exe')
driver.get('https://github.com/login')

driver.find_element_by_name('login').send_keys(github_username)
driver.find_element_by_name('password').send_keys(github_password)

driver.find_element_by_name('commit').click()

while not driver.find_elements_by_class_name('avatar'):
  time.sleep(1)

driver.get('https://github.com/new')

name_input = driver.find_element_by_xpath('//*[@id="repository_name"]')
name_input.send_keys(sys.argv[1])

classes = name_input.get_attribute("class")
while ('is-autocheck-errored' not in classes) and ('is-autocheck-successful' not in classes):
  time.sleep(1)
  classes = name_input.get_attribute("class")

if 'is-autocheck-errored' in classes:
  print(f"Error: Project name '{sys.argv[1]}' already exists")
  exit

driver.find_element_by_xpath('//*[@id="new_repository"]/div[3]/button').click()

git_link = driver.find_element_by_xpath('//*[@id="empty-setup-push-repo-echo"]/span[1]/span').text

driver.close()

os.system(f'git remote add origin {git_link}')
exit(0)
