import mechanize
from http.cookiejar import CookieJar
from bs4 import BeautifulSoup
import json
from tqdm import tqdm


br = mechanize.Browser()
cj = CookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)')]
# User-Agent (this can be changed to mimic different browsers)

def login():
    print("Loggingi into TPPC....")
    login_url = 'https://www.tppcrpg.net/login.php'
    br.open(login_url)
    br.select_form(nr=0)
    br.form['LoginID'] = 'username'
    br.form['NewPass'] = 'password'
    response = br.submit()
    assert response.code == 200
    print("Login sucessful")


def scrape_profile(id_list=[]):
    results = {}
    print("Scraping profiles.....")
    for id_ in tqdm(id_list):
        url = f"https://www.tppcrpg.net/profile.php?id={id_}&View=All"

        br.open(url)
        html_content = br.response().read()

        soup = BeautifulSoup(html_content, 'html.parser')
        ul_list = soup.find('ul', {'id': 'allPoke'})
        if ul_list:
            poke_list = [li.get_text().strip() for li in ul_list.find_all('li')]
            golds = [x for x in poke_list if "Golden" in x]
            U_s = [x for x in poke_list if "(?)" in x]
            level_4s = [x for x in poke_list if "(Level: 4)" in x]
        results[str(id_)] = {"Golds": golds, "Us": U_s, "Level 4s": level_4s}

    print("Done.")
    json.dump(results, open("results.json", "w"), indent=4)


if __name__ == "__main__":
    ids = open("ids.txt").read().split()
    # breakpoint()
    login()
    scrape_profile(ids)