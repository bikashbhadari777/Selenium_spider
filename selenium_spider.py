from selenium import webdriver
import time
import pandas as pd

class selenium():

    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(path)

    def nextpage(self):
        nextButton = self.driver.find_element_by_xpath('/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/list-search/page-layout/div/div/form/div[2]/results/div/div/div[1]/div/results-info/h3/a[2]/span[1]/div/span')
        if nextButton:
            nextButton.click()
            self.All_data()


    def Transaction(self):
        self.var = self.driver.find_elements_by_css_selector('.column-id-identifier .identifier-label')
        self.Transactions= []
        for name in self.var:
            self.Transactions.append(name.text)

    def Organization(self):
        self.var = self.driver.find_elements_by_css_selector('.column-id-funded_organization_identifier .identifier-label')
        self.organization = []
        for name in self.var:
            self.organization.append(name.text)

    def Funding_type(self):
        self.var = self.driver.find_elements_by_css_selector('.column-id-investment_type .layout-align-start-center')
        self.funding = []
        for name in self.var:
            self.funding.append(name.text)

    def money(self):
        self.var = self.driver.find_elements_by_css_selector('.column-id-money_raised .cb-margin-medium-horizontal')
        self.monney = []

        for name in self.var:
            self.monney.append(name.text)



    def Announced(self):
        self.var = self.driver.find_elements_by_css_selector('.column-id-announced_on .cb-margin-medium-horizontal')
        self.announc = []

        for name in self.var:
            self.announc.append(name.text)

    def Pre(self):
        self.var = self.driver.find_elements_by_css_selector('.column-id-pre_money_valuation .cb-margin-medium-horizontal')
        self.pre_money = []
        for name in self.var:
            self.pre_money.append(name.text)

    def Equity(self):
        self.var = self.driver.find_elements_by_css_selector('.column-id-is_equity .cb-margin-medium-horizontal')
        self.equaty_only_funding = []
        for name in self.var:
            self.equaty_only_funding.append(name.text)

    def Organization_industry(self):
        self.var = self.driver.find_elements_by_css_selector('.column-id-funded_organization_categories .field-type-identifier-multi')
        self.organization_indus = []
        for name in self.var:
            self.organization_indus.append(name.text)

    def Organization_Desc(self):
        self.var = self.driver.find_elements_by_css_selector('.field-type-text_long')
        self.orgaDes = []
        for name in self.var:
            self.orgaDes.append(name.text)

    def Organization_Location(self):
        self.var = self.driver.find_elements_by_css_selector('.column-id-funded_organization_location .layout-align-start-center')
        self.orga_location = []
        for name in self.var:
            self.orga_location.append(name.text)

    def website(self):
        self.var = self.driver.find_elements_by_css_selector('.column-id-funded_organization_website .layout-align-start-center')
        self.org_website = []
        for name in self.var:
            self.org_website.append(name.text)

    def NumberofInvestors(self):
        self.var = self.driver.find_elements_by_css_selector('.column-id-num_investors .cb-margin-medium-horizontal')
        self.no_investor = []
        for name in self.var:
            self.name_of_investor.append(name.text)
        self.make_column()


    def Investors_Name(self):
        self.var = self.driver.find_elements_by_css_selector('.column-id-investor_identifiers .layout-align-start-center')
        self.name_of_investor = []
        for name in self.var:
            self.name_of_investor.append(name.text)

    def lead_investor(self):
        self.var = self.driver.find_elements_by_css_selector('.column-id-lead_investor_identifiers .cb-margin-medium-horizontal')
        self.ld_investor = []
        for name in self.var:
            self.ld_investor.append(name.text)


    def fundingS(self):
        self.var = self.driver.find_elements_by_css_selector('.column-id-funded_organization_funding_stage .layout-align-start-center')
        self.fundingStatus = []
        for name in self.var:
            self.fundingStatus.append(name.text)

    def Number_of_funding(self):
        self.var = self.driver.find_elements_by_css_selector('.column-id-funded_organization_num_funding_rounds .cb-margin-medium-horizontal')
        self.noOffunding = []
        for name in self.var:
            self.noOffunding.append(name.text)

    def revenue(self):
        self.var = self.driver.find_elements_by_css_selector('.column-id-funded_organization_revenue_range .cb-margin-medium-horizontal')
        self.orga_revenue = []
        for name in self.var:
            self.orga_revenue.append(name.text)
        print(self.orga_revenue)


    def make_column(self):

        df = pd.DataFrame(list(zip(*[self.Transactions, self.organization,self.funding, self.monney, self.announc, self.pre_money,self.equaty_only_funding, self.organization_indus, self.orgaDes, self.orga_location, self.org_website,self.name_of_investor, self.name_of_investor,self.ld_investor,self.fundingStatus,self.noOffunding,self.orga_revenue,self.totalfundin])))
        df.to_csv('completedProject.csv',index=False,mode= "a")
        print(df)
        self.driver.implicitly_wait(4)
        self.nextpage()
    # 18 columns

    def totalfunding(self):
        self.var = self.driver.find_elements_by_css_selector('.column-id-funded_organization_funding_total .cb-margin-medium-horizontal')
        self.totalfundin = []
        for name in self.var:
            self.totalfundin.append(name.text)
        print(self.totalfundin)
        # make a list inside tuple
        # we will make a list of datas and call a func here to make the data in csv file

    def __init__(self):
        url = 'https://www.crunchbase.com/lists/vs-01/90e26de7-5cc5-4f94-af50-ee3b6e24f6e9/funding_rounds'
        self.driver.get(url)
        self.driver.implicitly_wait(20)
        email_storage = self.driver.find_element_by_id('mat-input-1')
        password = self.driver.find_element_by_id('mat-input-2')
        email_storage.send_keys('crunchbase@claudio.nu')
        time.sleep(2)
        password.send_keys('Thr0wAway')

        password.submit()
        time.sleep(4)
        self.driver.implicitly_wait(10)

    def All_data(self):

        self.driver.implicitly_wait(14)
        #1 - 18 columns
        self.Transaction() #1
        self.driver.implicitly_wait(3)
        self.Organization() #2
        self.Funding_type() #3
        self.money() #4
        self.Announced() # 5
        self.Pre() #6
        self.Equity() #7
        self.Organization_industry() # 8
        self.Organization_Desc()#9
        self.Organization_Location()#10
        self.website()#11
        self.revenue()#12
        self.totalfunding()#13
        self.Number_of_funding()#14
        self.fundingS()#15
        self.lead_investor()#16
        self.Investors_Name()#17
        self.NumberofInvestors()#18

        self.driver.implicitly_wait(3)
        # to do call a function

p = selenium()
p.All_data()