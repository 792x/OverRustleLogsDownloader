from bs4 import BeautifulSoup
from requests import get
import os

url = 'https://overrustlelogs.net/'

response = get(url)
channels = []
html_soup = BeautifulSoup(response.text, 'html.parser')
type(html_soup)

if not os.path.exists('./logs'):
    try:
        os.makedirs('./logs')
        print('Made log folder')
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise
else:
    print('Log folder already exists, skipping creating one')

channel_containers = html_soup.find_all('a', class_ = 'collection-item')
for channel in channel_containers:
    channels.append(channel['href'])
for id,channel in enumerate(channels):
    months = []
    url = 'https://overrustlelogs.net' + channel 
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)
    month_containers = html_soup.find_all('a', class_ = 'collection-item')
    for month in month_containers:
        months.append(month['href'])
    for month in months:
        dirname = './logs' + month
        if not os.path.exists(dirname):
            try:
                os.makedirs(dirname)
                print('Made directory: ' + dirname)
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        days = []
        url = 'https://overrustlelogs.net' + month
        response = get(url)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        type(html_soup)
        day_containers = html_soup.find_all('a', class_ = 'collection-item')
        for day in day_containers:
            days.append(day['href'])
        for day in days:
            if os.path.exists('./logs' + day + '.txt'):
                print('Already downloaded, skipping: ' + day)
            else:
                url = 'https://overrustlelogs.net' + day + '.txt'
                response = get(url)
                print('Channel: ' + str(id + 1) + '/' + str(len(channels)) + ' Downloading: ' + url)
                with open('./logs' + day + '.txt', 'wb') as f:
                    f.write(response.content)
                    f.close
