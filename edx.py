from selenium import webdriver
chrome_path=r"C:\Users\Spikee\Downloads\chromedriver.exe"
driver=webdriver.Chrome(chrome_path)
driver.maximize_window()

def edx(query):
    list_query=query.split(" ")
    search_query="https://www.edx.org/course?search_query="
    for i in list_query:
        search_query=search_query+"+"+i
    
    driver.get(search_query)
    course_avail=list()
    course_dates=list()
    co_providers=driver.find_elements_by_class_name("label")
    courses=driver.find_elements_by_tag_name('h3')
    availabity_courses=driver.find_elements_by_class_name("availability")
    dates=driver.find_elements_by_class_name("date")
    for i in dates:
        course_dates.append(i.text)
        print(i.text)
    for i in availabity_courses:
        course_avail.append(i.text)
    course_providers=list()
    # print("course providers\n")
    for i in co_providers:
        if(i.text.startswith("Schools and Partners:")):
            course_providers.append(str(i.text[22:]))
    # print(course_providers)
    course_names=list()
    edx_courses=courses[9:]
    # print("\ncourses names")
    for i in edx_courses:
        course_names.append(i.text)
    
    
    links=driver.find_elements_by_class_name("course-link")

    course_prices=list()
    contents=list()
    contents_list=list()
    links=driver.find_elements_by_class_name("course-link")
    course_links=[i.get_attribute("href") for i in links]
    # print("\nlinks of the courses")
    # print(course_links)
    pre=list()
    course_pre=list()
    for i in course_links:
        driver.get(i)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        k= driver.find_elements_by_css_selector("#what-you-will-learn > div.course-info-list.wysiwyg-content > ul > li")
        l=driver.find_elements_by_css_selector("#what-you-will-learn > div.course-info-list.wysiwyg-content > ol > li")
        k=k+l
        if(len(k)==0):
            k = driver.find_elements_by_css_selector("#page > main > section > div > div.container > div > div > div:nth-child(1) > div > ul > li")
            l = driver.find_elements_by_css_selector("#page > main > section > div > div.container > div > div > div:nth-child(1) > div > ol > li")
            k=k+l
        if (len(k) == 0):
            k = driver.find_elements_by_css_selector("#job-outlook > ul > li")
            l = driver.find_elements_by_css_selector("#job-outlook > ol > li")
            k=k+l
        if (len(k)==0):
            k= driver.find_elements_by_css_selector("#expected-learning > ul > li")
            l = driver.find_elements_by_css_selector("#expected-learning > ol > li")
            k=k+l
        contents_list=[i.text for i in k]
        contents.append(contents_list)
        contents_list = []
        prerequisites = driver.find_elements_by_css_selector("#course-summary-area > div.prerequisites > ul > li")
        if (len(prerequisites) == 0):
            # page > main > section > div > div.container > div > div > div:nth-child(3) > div > ul > li:nth-child(1
            prerequisites = driver.find_elements_by_css_selector("#course-summary-area > div.prerequisites > ol > li")
        if (len(prerequisites) == 0):
            try:
                prerequisites = driver.find_element_by_css_selector("#page > main > section > div > div.container > div > div > div:nth-child(3) > div")
            except:
                try:
                    prerequisites = driver.find_element_by_css_selector("# page > main > section > div > div.container > div > div > div:nth-child(3) > div > br")
                except:
                    try:
                        k=driver.find_element_by_xpath(""" //*[@id="course-summary-area"]/div[2]/p[2]/a """)
                        prerequisites.append(k)
                        prerequisites.append(k.get_attribute("href"))
                    except:
                        try:
                            prerequisites=driver.find_element_by_xpath(""" //*[@id="course-summary-area"]/div[2]/p  """)
    
                        except:
                            prerequisites.append("no prerequisites mentioned")
    
    
        if (type(prerequisites) == list):
            for i in prerequisites:
                try:
                    pre.append(i.text)
                except:
                    try:
                        pre.append(i)
                    except:
                        pass
        else:
            pre.append(prerequisites.text)
        course_pre.append(pre)
        pre = []
        prerequisites = []
        pr=""
        # try:
        #     price = driver.find_element_by_css_selector("#course-summary-area > ul:nth-child(1) > li:nth-child(3) > span.block-list__desc")
        #     pr=price.text[38:42]
        #     course_prices.append(pr)
        # except:
        #     try:
        #         price = driver.find_element_by_css_selector(
        #             "#page > main > section > div > header > div > div > div.course-stats.col-xl-8 > div.course-stat.first.col-md > div > div.highlight")
        #         pr=price.text
        #         course_prices.append(pr)
        #     except:
        #         try:
        #             price = driver.find_element_by_css_selector("#course-summary-area > ul > li:nth-child(3) > span.block-list__desc >")
        #             course_prices.append(price.text)
        #         except:
        #             price="unknown"
        #             course_prices.append(price)
        #             pass
        #
        # price = []
    #
    # print("\ncontents of the courses")
    # for i in contents:
    #     print(i)
    #
    # print("\n prerequisites of the course")
    # for i in course_pre:
    #     print(i)
    # for i in course_prices:
    #     print(i)
    edx_dict=dict()
    count=0
    for i in course_links:
        edx_dict[i]=[course_names[count],course_providers[count],"---","---",course_pre[count],contents[count]]
        count=count+1
   # for i in edx_dict.values():
    #    print(i)
    print("Done... Edx")
    return edx_dict