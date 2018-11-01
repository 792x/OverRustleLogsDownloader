# OverRustleLogsDownloader
Python script to download OverRustle (Twitch) logs

Script to download all available chatlogs from the available twitch streamers on [OverRustle Logs](https://overrustlelogs.net/)

#### Setup:
```bash
git clone https://github.com/792x/OverRustleLogsDownloader.git
```

or alternatively download app.py manually.

#### Run:
```bash
cd OverRustleLogsDownloader
python app.py
```
A `logs` folder will be created with the following structure:
`logs\name\month_year\year_month_day.txt`

#### Dependencies:
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
- [Requests](https://pypi.org/project/requests/)
