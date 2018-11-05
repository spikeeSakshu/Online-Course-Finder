from bs4 import BeautifulSoup
import urllib3
import collections
import re
import threading
import time

http = urllib3.PoolManager()
final_list = {}
urllib3.disable_warnings()
Visited = collections.deque()
UnVisited = collections.deque()
AllLinks = collections.deque()

def CourseEra(query):

    query = query.split(" ")
    search = ""
    for item in query:
        search += "%20" + item

    base_url = "https://www.coursera.org"

    def urlParse(url):
        next_link = url
        Visited.append(next_link)
        print("NEXT LINK", next_link)
        r = http.request('GET', next_link)
        soup = BeautifulSoup(r.data, 'html.parser')
        return soup

    def getRatings(url):
        soup = urlParse(url)
        content = []
        try:
            rating = soup.find('span', {'class': 'H4_1k76nzj-o_O-weightBold_uvlhiv-o_O-bold_1byw3y2 m-l-1s m-r-1 m-b-0'})
            people = soup.find('div', {'class': 'P_gjs17i-o_O-weightNormal_s9jwp5-o_O-fontBody_56f0wi m-r-1s'})
            people = people.get_text().split(" ")[0]
            rate = rating.get_text()

        except:
            rating = soup.find('div', {'class': "ratings-text headline-2-text"})
            rating = rating.text
            process = rating.split(" ")
            rate = process[1]
            people = process[6]

        content_list = soup.find_all('h2', {'class': "H2_1pmnvep-o_O-weightBold_uvlhiv-o_O-bold_1byw3y2 m-b-2"})
        if len(content_list) == 0:
            content_list = soup.find_all('div', {'class': "module-name headline-2-text"})

        for item in content_list:
            content.append(item.get_text())
        # print("content", content)
        people=str(people).split(" ")
        # final_list.append([rate, people[0], url, content])
        final_list[url]=[rate,people[0],content]


    def parallel():
        threads = [threading.Thread(target=getRatings, args=(url,)) for url in UnVisited]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()


    def fun():
        i = 0
        while i != 1:
            soup = urlParse("https://www.coursera.org/courses?query=" + search)
            a = soup.find_all("a", href=re.compile("/learn"))
            for link in a:
                url = str(link.get("href"))
                print("url ", url)
                if url.startswith('https'):
                    continue
                else:
                    if url in UnVisited or url in Visited:
                        print("present or visited")
                    else:
                        UnVisited.append(base_url + url)
                        AllLinks.append(base_url + url)
            t1 = time.time()
            parallel()
            t2 = time.time()
            print("total time", t2 - t1)
            i += 1

    fun()


    # for key in final_list:
    #     print(key," ",final_list[key])

    return final_list

