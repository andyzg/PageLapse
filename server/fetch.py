from git import Repo
from selenium import webdriver
import subprocess

def screen(website_url, output_path):
	driver = webdriver.PhantomJS() # or add to your PATH
	driver.set_window_size(1440, 768) # optional
	driver.get(website_url)
	driver.save_screenshot(output_path) # save a screenshot to disk
	driver.quit()

def fetch(repo_url):

	tmp_path = 'tmp/'
	screen_path = 'screenshots/'
	repo_path = tmp_path + repo_url.split('/')[-1]

	# repo = Repo.clone_from(repo_url, repo_path)

	repo = Repo(repo_path)
	git = repo.git

	# fetch all commits
	commit_list = []
	for commit in repo.iter_commits('master', max_count=2000):
		commit_list.append(commit)
	commit_list.reverse()

	command = "jekyll server --watch -s " + repo_path + " -d " + repo_path + "/_site 1>&2"
	output = subprocess.check_output(command, shell=True)

	while True:
		if "Server running" in output:
			print "Server running"

fetch('https://github.com/markprokoudine/mchacks')





