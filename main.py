A=0
while True:
    if A!=0:
       time.sleep(43200)
    A+=1
    req = Request("https://www.reddit.com/r/popular/")
    html_page = urlopen(req)

    soup = BeautifulSoup(html_page, "lxml")

    links = []
    fl = []
    for link in soup.findAll('a'):
        k = link.get('href')
        if "comments" in k and k not in fl :
            fl.append(k)
        links.append(k)
   
    for i in fl:
        j = "https://www.reddit.com"+i
    


        base_url = "https://api.telegram.org/bot5760756459:AAGbMmlWjvw4UuTF_tDrJwSBzM1caOvfZQo/sendMessage"


        parameters = {
            "chat_id" : "-1001849713198",
            "text" : j
        }

        resp = requests.get(base_url, data = parameters)
   # print(resp.text)