from selenium import webdriver
chrome_path=r"C:\Users\Spikee\Downloads\chromedriver.exe"
driver=webdriver.Chrome(chrome_path)







def online_stanford(query):
    list_query=query.split(" ")
    search_query="https://online.stanford.edu/courses?keywords="
    for i in list_query:
        search_query=search_query+"%20"+i
    search_query+="&availability[available]=available"
        
    driver.get(search_query)
    driver.minimize_window()
    
    
    
    
    c_providers=list()
    
    
    course_providers=driver.find_elements_by_tag_name("h3")
    for i in course_providers:
        c_providers.append(i.text)
    #link=driver.find_element_by_class_name("node node--type-course")
    # link=driver.find_elements_by_partial_link_text("/courses/")
    link=driver.find_elements_by_css_selector("#search-results > a")
    course_link=list()
    topics=list()
    preq=list()
    author=list()
    date=list()
    days=list()
    time=list()
    units=list()
    fees=list()
    course_fee=list()
    course_topics=list()
    course_preq=list()
    course_author=list()
    course_days=list()
    course_date=list()
    stanford_dict={}
    for i in link:
          course_link.append(i.get_attribute("href"))
    count=0
    for j in course_link[0:4]:
        #print(j)
        driver.get(j)
        topics=driver.find_elements_by_css_selector("#block-stanfordonline-content > div > div:nth-child(4) > div:nth-child(1) > ul.tight > li")
        for i in topics:
            course_topics.append(i.text)
        try:
            preq=driver.find_element_by_css_selector("#block-stanfordonline-content > div > div:nth-child(4) > div:nth-child(1) > p:nth-child(9)")
            course_preq.append(preq.text)
        except:
            preq="no prerequisites mentioned"
            course_preq.append(preq)
        try:
            author=driver.find_element_by_css_selector("#block-stanfordonline-content > div > div:nth-child(4) > div:nth-child(1) > ul.list-unstyled > li")
            course_author.append(author.text)
        except:
            try:
                author=driver.find_element_by_css_selector("#block-stanfordonline-content > div > div:nth-child(4) > div:nth-child(2) > div > div > div > div > table:nth-child(2) > tbody > tr:nth-child(1) > td:nth-child(2) > ul > li:nth-child(1) > a")
                course_author.append(author.text)
            except:
                author="instructor not specified"
                course_author.append(author)
    
        try:
            date=driver.find_element_by_css_selector("#block-stanfordonline-content > div > div:nth-child(4) > div:nth-child(2) > div > div > div > div > table:nth-child(2) > tbody > tr:nth-child(1) > td:nth-child(2)")
            days=driver.find_element_by_css_selector("#block-stanfordonline-content > div > div:nth-child(4) > div:nth-child(2) > div > div > div > div > table:nth-child(2) > tbody > tr:nth-child(2) > td:nth-child(2)")
            course_date.append(date.text)
            course_days.append(days.text)
            # time=driver.find_element_by_css_selector("#block-stanfordonline-content > div > div:nth-child(4) > div:nth-child(2) > div > div > div > div > table:nth-child(2) > tbody > tr:nth-child(3) > td:nth-child(2)")
            # units=driver.find_element_by_css_selector("#block-stanfordonline-content > div > div:nth-child(4) > div:nth-child(2) > div > div > div > div > table:nth-child(2) > tbody > tr:nth-child(4) > td:nth-child(2)")
            fees=driver.find_element_by_css_selector("#block-stanfordonline-content > div > div:nth-child(4) > div:nth-child(2) > div > div > div > div > table:nth-child(3) > tbody > tr > td:nth-child(2) > span")
        except:
           date=""
           days=""
           time=""
           units=""
           fees=""
           course_date.append(date)
           course_days.append(days)
           course_fee.append(fees)
    
    
        stanford_dict[j]=[c_providers[count],course_author,"--","--",course_preq,course_topics]
        count=count+1
        course_fee = []
        course_topics = []
        course_preq = []
        course_author = []
        course_days = []
        course_date = []
    
    # print(date.text)
    # print(days.text)
    # print(time.text)
    # print(author.text)
    # print(units.text)
    # print(fees.text)
    #
    # print(preq.text)
    # for i in topics:
    #       print(i.text)
    
    #for i in stanford_dict.values():
     #   print(i)
    return stanford_dict