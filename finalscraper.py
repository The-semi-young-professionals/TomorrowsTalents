# import selenium and selenium sub libraries
# install with pip selenium, webdrivermanager, chrome if needed
import selenium
from selenium import webdriver # general webdriver
from selenium.webdriver.common.keys import Keys # Keyboard commands
from webdriver_manager.chrome import ChromeDriverManager # Automatic Updater for driver
import time

#Link list builder


driver = webdriver.Chrome(ChromeDriverManager().install()) # check for latest Webdriver


link_start= "https://ranking.zeit.de/che/de/hochschule/2"
link_base= "https://ranking.zeit.de/che/de/hochschule/"

# click cookie banner
driver.get(link_start)
time.sleep(3)
element = driver.find_element_by_xpath("//div[@id='sp_message_container_574935']").click() #driver.find_element_by_xpath("//div[@id='sp_message_container_574935']").click()
time.sleep(3)

link_list = []
for a in range(2,1000,2):
    link = link_base+str(a)
    #link_list.append(link)
    driver.get(link)
    try:
        #Name Uni
        name_uni = 'NaN'
        name_uni = driver.find_element_by_xpath("//h1[@class='std-headline std-headline--h2']").text
        link_list.append(a)
        print(name_uni)

    except:
        pass
print(link_list)    

driver.quit()

#### dataframe builder

# set up dataframe with all variables I want to scrape
#UNIS
import pandas as pd
#https://ranking.zeit.de/che/de/hochschule/2
#dataframe_uni
data_cols = ['id_uni', 'name_uni', 'city','street_nr', 'plz','homepage',  'type_uni', 'traeger', 'founding_year', 'total_students','total_students_loc','s_beitrag','s_gebuehren', 'lon', 'lat', 'sd_mg', 'sd_nm', 'sd_rws', 'sd_sk', 'sd_in', 'sd_so', 'ab_ba', 'ab_ma', 'ab_la', 'ab_dms','ab_so']
df_unis = pd.DataFrame(columns=data_cols)
print(df_unis)

#https://ranking.zeit.de/che/de/fachbereich/30546
#dataframe_fuckultaet
data_cols = ['id_uni', 'id_fak', 'name_fb', 'city', 'street_nr', 'plz', 'total_doz', 'total_stud', 'total_stud_ma', 'support_start','tframe_grad_ba','tframe_grad_ma', 'lon', 'lat', 'int_ba', 'int_ma', 'foreign_spot', 'sup_doz', 'sup_in_studies', 'curriculum', 'students_orga', 'exams', 'research_conn', 'offer_joborientation','supp_exchange', 'faculties','bib','it_infrastructure','grade_overall', 'total_students_la','la_studies']
df_fbs = pd.DataFrame(columns=data_cols)

print(df_fbs)
#https://ranking.zeit.de/che/de/studiengang/18790
#dataframe_studies
data_cols = ['id_uni', 'id_fak', 'id_stud', 'name_stud', 'kind_stud', 'time_stud', 'credits', 'total_stds', 'total_starter_year', 'total_grads_year', 'tframe_grad', 'ptod_ratio','exstd_ratio','forgeign_lang_ratio','mandatory_exchange', 'foreign_conn', 'access']
df_stds = pd.DataFrame(columns=data_cols)
print(df_stds)



#3## BIG LOOP

import time
import random
#link_base = "https://ranking.zeit.de/che/de/hochschule/"



for link in link_list:

    
    # Start Driver, get site, create link list
    uni_links = [] # list for collection of of sites containing information
    driver = webdriver.Chrome(ChromeDriverManager().install()) # check for latest Webdriver


    driver.get("https://ranking.zeit.de/che/de/hochschule/104")

    time.sleep(3)

    # click cookie banner
    element = driver.find_element_by_xpath("//div[@id='sp_message_container_574935']").click() #driver.find_element_by_xpath("//div[@id='sp_message_container_574935']").click()
    time.sleep(3)

    #time.sleep(random.randint(1,15))
    driver.get(link_base + str(link))
    #Infos Uni Hauptseite

    text = driver.page_source

    #uni Id
    url = driver.current_url 
    id_uni = url.split('/')[-1]
    id_uni = id_uni.split('?')[0]

    #Name Uni
    name_uni = 'NaN'
    name_uni = driver.find_element_by_xpath("//h1[@class='std-headline std-headline--h2']").text
    print(name_uni)


    # homepage
    homepage = 'NaN'
    homepage = driver.find_element_by_xpath("//ul[@class='chelist chemargin']/li/a").text
    print(homepage)

    # Anschrift

    anschrift = driver.find_elements_by_xpath("//ul[@class='chelist']/li")

    list_anschrift = []

    for a in anschrift:
        list_anschrift.append(a.text)
    print(list_anschrift)

    #leere vars initialisieren
    city = 'NaN'
    street_nr = 'NaN'
    plz = 'NaN'
    #values einfuegen
    city = list_anschrift[1]
    city = city.split(' ')
    city = city[1] 

    #plz
    plz = list_anschrift[1]
    plz = plz.split(' ')
    plz = plz[0] 

    #street nr
    street_nr = list_anschrift[0]


    #uni infos
    points = driver.find_elements_by_xpath("//td[@class='checol1 rank']")
    list1 = []
    for p in points:
        list1.append(p.text)
    #print(list1)
    points = driver.find_elements_by_xpath("//td[@class='checol2_rank colSpan2']")
    list2 = []
    for p in points:
        if p == '':
            continue
        else:
            list2.append(p.text)


    #print(list2)
    #uni_combined = dict(zip(list1, list2))
    #print(uni_combined)

    #uni infos
    points = driver.find_elements_by_xpath("//td[@class='checol1 balken']")

    for p in points:
        list1.append(p.text)
    #print(list1)
    points = driver.find_elements_by_xpath("//td[@class='checol2_balken ']")

    for p in points:
        if p == '':
            continue
        else:
            list2.append(p.text)

    print(list1)
    print(list2)
    #print(list2)
    uni_combined = dict(zip(list1, list2))
    print(uni_combined)


    type_uni = 'NaN'
    traeger  = 'NaN'
    founding_year = 'NaN'
    total_students = 'NaN'
    total_students_loc = 'NaN'
    s_beitrag  = 'NaN'
    s_gebuehren = 'NaN'
    sd_mg = 'NaN'
    sd_nm  = 'NaN'
    sd_rws = 'NaN'
    sd_sk = 'NaN'
    sd_in = 'NaN'
    sd_so = 'NaN'
    ab_ba = 'NaN'
    ab_ma = 'NaN'
    ab_la = 'NaN'
    ab_dms = 'NaN'
    ab_so = 'NaN'

    # Uni Attributes
    for a in uni_combined:
        if a == 'Hochschultyp und Trägerschaft':
            type_uni = uni_combined['Hochschultyp und Trägerschaft'].split(",")[0]
            traeger = uni_combined['Hochschultyp und Trägerschaft'].split(",")[1]    
        elif a == 'Gründungsjahr':
            founding_year = uni_combined['Gründungsjahr']
        elif a == 'Studierende der Hochschule insgesamt':
            total_students = uni_combined['Studierende der Hochschule insgesamt']
        elif a == "Studierende der Hochschule an diesem Standort":
            total_students_loc = uni_combined["Studierende der Hochschule an diesem Standort"]
        elif a == 'Semesterbeitrag':
            s_beitrag = uni_combined['Semesterbeitrag']
        elif a == 'Studiengebühren':
            s_gebuehren = uni_combined['Studiengebühren']
        elif a == 'Medizin, Gesundheitswissenschaften':
            sd_mg = uni_combined['Medizin, Gesundheitswissenschaften']
        elif a == 'Naturwissenschaften, Mathematik':
            sd_nm = uni_combined['Naturwissenschaften, Mathematik']
        elif a == "Rechts-, Wirtschafts- und Sozialwissenschaften":
            sd_rws = uni_combined["Rechts-, Wirtschafts- und Sozialwissenschaften"]
        elif a == 'Sprach- und Kulturwissenschaften':
            sd_sk = uni_combined["Sprach- und Kulturwissenschaften"]  
        elif a == 'Ingenieurwissenschaften (inkl. Informatik)':
            sd_in = uni_combined['Ingenieurwissenschaften (inkl. Informatik)']
        elif a == 'Sonstige':
            sd_so = uni_combined['Sonstige']
        elif a == 'Bachelor':
            ab_ba = uni_combined['Bachelor']   
        elif a == 'Master':
            ab_ma = uni_combined['Master']   
        elif a == 'Lehramtsprüfung':
            ab_la = uni_combined['Lehramtsprüfung']   
        elif a == 'Diplom, Magister, Staatexamen':
            ab_dms = uni_combined['Diplom, Magister, Staatexamen'] 
        elif a == 'Sonstige Abschlüsse':
            ab_so = uni_combined['Sonstige Abschlüsse'] 
            


    # Koordinaten lat
    lat = 'NaN'
    lat = text.split('lat:')[1]
    lat = lat.split(',\n')[0]
    print(lat)

    # Koordinaten lon
    lon = 'NaN'
    lon = text.split('lng:')[1]
    lon = lon.split('\n')[0]
    print(lon)

    # insert Variables as column into dataframe. After every iteration a new column with all the newly defined variables is stored in the dataframe.
    df_unis.loc[len(df_unis.index)] = [id_uni, name_uni, city, street_nr, plz, homepage, type_uni, traeger, founding_year, total_students, total_students_loc, s_beitrag, s_gebuehren, lon, lat, sd_mg, sd_nm, sd_rws, sd_sk, sd_in, sd_so, ab_ba, ab_ma, ab_la, ab_dms, ab_so]
    print(df_unis)


    # Links fuer Fakultaetenäü

    links_f = driver.find_elements_by_xpath("//a[@class='contain-link']")
    list_fak = []
    for p in links_f:
        a = p.get_attribute("href")
        list_fak.append(a)
    print(list_fak)


    #start loop fachbereiche 
    ## 
    ### 


    for fak in list_fak:
        #time.sleep(random.randint(1,10))
        driver.get(fak)
        text = driver.page_source

        time.sleep(2)
        
        #FAK ID
        url = driver.current_url 
        id_fak = url.split('/')[-1]
        id_fak = id_fak.split('?')[0]


        #title fakultaet
        name_fb = 'NaN'
        name_fb = text.split("<title>")[1]
        name_fb = name_fb.split(" | ZEIT Campus</title>")[0]
        print(name_fb)


        #strasse institut +number
        street_nr = 'NaN'
        street_nr = text.split("<ul class=\"chelist\" itemscope=\"\" itemtype=\"http://schema.org/PostalAddress\">")[1]
        street_nr = street_nr.split("</li>")[0]
        street_nr = street_nr.split("<li>")[1]
        print(street_nr)


        #PLZ institut
        plz = 'NaN'
        try:
            plz = text.split("<ul class=\"chelist\" itemscope=\"\" itemtype=\"http://schema.org/PostalAddress\">")[1]
            plz= plz.split("&")[0]
            plz = plz.split("<li>")[2]
            print(plz)
        except:
            pass

        # Koordinaten lat
        lat='NaN'
        lat = text.split('lat:')[1]
        lat = lat.split(',\n')[0]
        print(lat)

        # Koordinaten lon
        lon ='NaN'
        lon = text.split('lng:')[1]
        lon = lon.split('\n')[0]
        print(lon)

        ##############################

        points = driver.find_elements_by_xpath("//tr[@class='tableRow trbg1']/td")
        list1 = []
        for p in points:
            list1.append(p.text)
        print(list1)
        while '' in list1:
            list1.remove('')

        attr = []
        vals = []
        for idx, l in enumerate(list1):
            if idx == 0 or idx%2 == 0:
                attr.append(l)
            else:
                vals.append(l)

        fak_combined = dict(zip(attr, vals))
        
        ################################
        '''
        print(elements)
        #fak infos
        points = driver.find_elements_by_xpath("//td[@class='checol1 rank']")
        list1 = []
        for p in points:
            list1.append(p.text)
        #print(list1)
        points = driver.find_elements_by_xpath("//td[@class='checol2_rank colSpan2']")
        list2 = []
        for p in points:
            list2.append(p.text)
        #print(list2)
        fak_combined = dict(zip(list1, list2))
        print(fak_combined)
        '''
        
        #Links Studiengnaenge
        links_f = driver.find_elements_by_xpath("//a[@class='contain-link']")
        list_stds = []
        for p in links_f:
            a = p.get_attribute("href")
            list_stds.append(a)
        print(list_stds)
        
        total_doz = 'NaN'
        total_stud = 'NaN'
        total_stud_ma = 'NaN'
        support_start = 'NaN'
        tframe_grad_ba = 'NaN'
        tframe_grad_ma = 'NaN'
        int_ba = 'NaN'
        int_ma = 'NaN'
        foreign_spot = 'NaN'
        sup_doz = 'NaN'
        sup_in_studies = 'NaN'
        curriculum = 'NaN'
        students_orga = 'NaN'
        exams = 'NaN'
        research_conn = 'NaN'
        offer_joborientation = 'NaN'
        supp_exchange = 'NaN'
        faculties = 'NaN'
        bib = 'NaN'
        it_infrastructure = 'NaN'
        grade_overall = 'NaN'
        total_students_la = 'NaN'
        la_studies = 'NaN'


        for a in fak_combined:
            if a == 'Lehrende am Fachbereich':
                total_doz = fak_combined['Lehrende am Fachbereich']
            elif a == 'Studierende insgesamt':
                total_stud = fak_combined['Studierende insgesamt']
            elif a == 'Anzahl Masterstudierende':
                total_stud_ma = fak_combined['Anzahl Masterstudierende']
            elif a == 'Gesamtergebnis Unterstützung am Studienanfang':
                support_start = fak_combined['Gesamtergebnis Unterstützung am Studienanfang']
            elif a == 'Abschlüsse in angemessener Zeit, B/StEx/D':
                tframe_grad_ba = fak_combined['Abschlüsse in angemessener Zeit, B/StEx/D']
            elif a == 'Abschlüsse in angemessener Zeit, Master':
                tframe_grad_ma = fak_combined['Abschlüsse in angemessener Zeit, Master']
            elif a == 'Internationale Ausrichtung Bachelor':
                int_ba = fak_combined['Internationale Ausrichtung Bachelor']
            elif a == 'Internationale Ausrichtung, Master':
                int_ma = fak_combined['Internationale Ausrichtung, Master']
            elif a == 'Genutzte Auslandsplätze':
                foreign_spot = fak_combined['Genutzte Auslandsplätze']
            elif a == 'Betreuung durch Lehrende':
                sup_doz = fak_combined['Betreuung durch Lehrende']
            elif a == 'Unterstützung im Studium':
                sup_in_studies = fak_combined['Unterstützung im Studium']
            elif a == 'Lehrangebot':
                curriculum = fak_combined['Lehrangebot']
            elif a == 'Studienorganisation':
                students_orga = fak_combined['Studienorganisation']
            elif a == 'Prüfungen':
                exams = fak_combined['Prüfungen']
            elif a == 'Wissenschaftsbezug':
                research_conn = fak_combined['Wissenschaftsbezug']
            elif a == 'Angebote zur Berufsorientierung':
                offer_joborientation = fak_combined['Angebote zur Berufsorientierung']
            elif a == 'Unterstützung für Auslandsstudium':
                supp_exchange = fak_combined['Unterstützung für Auslandsstudium']
            elif a == 'Räume':
                faculties = fak_combined['Räume']
            elif a == 'Bibliotheksausstattung':
                bib = fak_combined['Bibliotheksausstattung']
            elif a == 'IT-Infrastruktur':
                it_infrastructure = fak_combined['IT-Infrastruktur']
            elif a == 'Allgemeine Studiensituation':
                grade_overall = fak_combined['Allgemeine Studiensituation']
            elif a == 'Anzahl Lehramtstudierende':
                total_students_la = fak_combined['Anzahl Lehramtstudierende']
            elif a == 'Lehramtstudiengänge':
                la_studies = fak_combined['Lehramtstudiengänge'] 

        df_fbs.loc[len(df_fbs.index)] = [id_uni, id_fak, name_fb, city, street_nr, plz,  total_doz, total_stud, total_stud_ma, support_start,tframe_grad_ba,tframe_grad_ma, lon, lat, int_ba, int_ma, foreign_spot, sup_doz, sup_in_studies, curriculum, students_orga, exams, research_conn, offer_joborientation,supp_exchange, faculties,bib,it_infrastructure,grade_overall, total_students_la,la_studies]
        print(df_fbs)

        for fach in list_stds:
            
            #time.sleep(random.randint(1,10))
            driver.get(fach)
            driver.page_source

            try:
                points = driver.find_elements_by_xpath("//div[@class='openIcon']")
                for p in points:
                    p.click()
            except:
                continue
            #stud ID
            #FAK ID
            url = driver.current_url 
            id_stud = url.split('/')[-1]
            id_stud = id_stud.split('?')[0]

            # Bezeichnung Studiengang inkl fakultät und Uni
            name_stud = 'NaN'
            name_stud = driver.find_elements_by_xpath("//h1[@class='hsr-headline std-headline std-headline--h2']")
            for name in name_stud:
                name_s = name.text
                name_stud = str(name_s).split('\n')[0]


            # Infos Studiengänge
            points = driver.find_elements_by_xpath("//tr[@class='tableRow trbg1']/td")
            list1 = []
            for p in points:
                list1.append(p.text)
            print(list1)
            while '' in list1:
                list1.remove('')

            attr = []
            vals = []
            for idx, l in enumerate(list1):
                if idx == 0 or idx%2 == 0:
                    attr.append(l)
                else:
                    vals.append(l)

            study_combined = dict(zip(attr, vals))
            
            print(study_combined)

            

            kind_stud = 'NaN'
            time_stud = 'NaN'
            credits = 'NaN'
            total_stds = 'NaN'
            total_starter_year = 'NaN'
            total_grads_year = 'NaN'
            tframe_grad = 'NaN'
            ptod_ratio = 'NaN'
            exstd_ratio = 'NaN'
            forgeign_lang_ratio = 'NaN'
            mandatory_exchange = 'NaN'
            foreign_conn = 'NaN'
            access = 'NaN'
            

            for a in study_combined:
            
                if a == '':
                    id_uni = study_combined['']
                elif a == '':
                    id_fa = study_combined['']
                elif a == '':
                    id_stud = study_combined['']
                elif a == 'Art des Studiengangs':
                    kind_stud = study_combined['Art des Studiengangs']
                elif a == 'Regelstudienzeit':
                    time_stud = study_combined['Regelstudienzeit']
                elif a == 'Credits insgesamt':
                    credits = study_combined['Credits insgesamt']
                elif a == 'Anzahl der Studierenden':
                    total_stds = study_combined['Anzahl der Studierenden']
                elif a == 'Studienanfänger pro Jahr':
                    total_starter_year = study_combined['Studienanfänger pro Jahr']
                elif a == 'Absolventen pro Jahr':
                    total_grads_year = study_combined['Absolventen pro Jahr']
                elif a == 'Abschlüsse in angemessener Zeit':
                    tframe_grad = study_combined['Abschlüsse in angemessener Zeit']
                elif a == 'Geschlechterverhältnis':
                    ptod_ratio = study_combined['Geschlechterverhältnis']
                elif a == 'Anteil ausländischer Studierender':
                    exstd_ratio = study_combined['Anteil ausländischer Studierender']
                elif a == 'Anteil fremdsprachiger Lehrveranstaltungen':
                    forgeign_lang_ratio = study_combined['Anteil fremdsprachiger Lehrveranstaltungen']
                elif a == 'Obligatorischer Auslandsaufenthalt':
                    mandatory_exchange = study_combined['Obligatorischer Auslandsaufenthalt']
                elif a == 'Gemeinsames Studienprogramm mit ausländischer Hochschule':
                    foreign_conn = study_combined['Gemeinsames Studienprogramm mit ausländischer Hochschule']
                elif a == 'Zulassungsbeschränkung':
                    access = study_combined['Zulassungsbeschränkung']
            
            df_stds.loc[len(df_stds.index)] = [id_uni, id_fak,id_stud, name_stud, kind_stud, time_stud, credits, total_stds, total_starter_year, total_grads_year, tframe_grad, ptod_ratio, exstd_ratio, forgeign_lang_ratio, mandatory_exchange, foreign_conn, access]
            print(df_stds)
    driver.quit()   
driver.quit()      

df_unis.to_excel('./list_unis.xlsx')
df_fbs.to_excel('./list_unis.xlsx')
df_stds.to_excel('./list_unis.xlsx')