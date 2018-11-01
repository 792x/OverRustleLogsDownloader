from bs4 import BeautifulSoup
from requests import get
import os

url = 'https://overrustlelogs.net/'
streamers = ['Admiralbulldog', 'Alinity', 'Alkaizer', 'Amouranth', 'Andymilonakis', 'Asmongold', 'Athenelive', 'B0aty',
             'Becca', 'Bullyhunters', 'C9sneaky', 'Cdewx', 'Celeste', 'Cjayride', 'Clintstevenz', 'Cowsep', 'Dafran',
             'Dankquan', 'Dansgaming', 'Darksydephil', 'Dekar173', 'Demolition_d', 'Dendi', 'Destiny', 'Destinygg',
             'Eloise', 'Esfandtv', 'Forsen', 'Geersart', 'Geisha', 'Greekgodx', 'Grossie_gore', 'H3h3productions',
             'Hyubsama', 'Iam_choa', 'Ice_poseidon', 'Jakenbakelive', 'Jaxerie', 'Kaceytron', 'Legendarylea',
             'Loltyler1', 'Mcconnellret', 'Meteos', 'Mitchjones', 'Nani', 'Nmplol', 'Nymn', 'Pajlada', 'Reckful',
             'Sick_nerd', 'Singsing', 'Sodapoppin', 'Trihardgodcx', 'Xqcow']

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

channel_containers = html_soup.find_all('a', class_ = 'list-group-item')
for channel in channel_containers:
    for streamer in streamers:
        if channel['href'].startswith(streamer, 1):
            channels.append(channel['href'])
for id,channel in enumerate(channels):
    months = []
    url = 'https://overrustlelogs.net' + channel
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)
    month_containers = html_soup.find_all('a', class_ = 'list-group-item')
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
        day_containers = html_soup.find_all('a', class_ = 'list-group-item')
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
