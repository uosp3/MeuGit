# código gerado pelo chatGPT para atualizar o chromedriver
import requests
from bs4 import BeautifulSoup
import zipfile
import os
import shutil
import platform


def get_latest_chromedriver_version():
    url = 'https://sites.google.com/chromium.org/driver/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    version_elem = soup.find('div', {'id': 'chromedriver-version'})
    if version_elem:
        version_text = version_elem.text.strip()
        latest_version = version_text.split()[1]
        return latest_version
    else:
        raise ValueError('Failed to find driver version information on page')


def download_chromedriver(version):
    base_url = 'https://chromedriver.storage.googleapis.com/'
    if platform.system() == 'Windows':
        filename = 'chromedriver_win32.zip'
    elif platform.system() == 'Linux':
        filename = 'chromedriver_linux64.zip'
    elif platform.system() == 'Darwin':
        filename = 'chromedriver_mac64.zip'
    else:
        raise ValueError('Unsupported platform')

    download_url = f'{base_url}{version}/{filename}'
    response = requests.get(download_url)

    download_path = os.path.join(os.getcwd(), filename)
    with open(download_path, 'wb') as f:
        f.write(response.content)

    return download_path


def update_chromedriver():
    try:
        latest_version = get_latest_chromedriver_version()
        current_version = shutil.which('chromedriver')

        if current_version:
            print(f'Current ChromeDriver version: {current_version}')
        else:
            print('ChromeDriver not found. Downloading latest version...')

        if current_version != latest_version:
            print(f'Updating ChromeDriver to version {latest_version}')
            download_path = download_chromedriver(latest_version)

            # Extract chromedriver from zip file
            with zipfile.ZipFile(download_path, 'r') as zip_ref:
                zip_ref.extractall(os.getcwd())

            # Make chromedriver executable (for Unix-based systems)
            if platform.system() != 'Windows':
                os.chmod('chromedriver', 0o755)

            # Clean up
            os.remove(download_path)

            print('ChromeDriver updated successfully')
        else:
            print('ChromeDriver is already up to date')
    except Exception as e:
        print(f'Error updating ChromeDriver: {e}')


if __name__ == '__main__':
    update_chromedriver()
