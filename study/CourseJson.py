# open API doc : https://data.seoul.go.kr/dataList/OA-2562/S/1/datasetView.do?tab=S
# API 인증키 : 보안 문제로 생략
# test full url : http://openAPI.seoul.go.kr:8088/API키/json/OnlineCoures/1/100
import requests

class CourseJson:
    API_KEY = ''
    url =''
    CATEGORY_NM2 = ""#카테고리명
    COURSE_NM = "" #강의명 
    
    def __init__(self):
        self.API_KEY='API 키를 넣어주세요. 보안문제로 제거 합니다.'
        self.url ='http://openAPI.seoul.go.kr:8088/'+self.API_KEY+'/json/OnlineCoures/1/100'
        self.CATEGORY_NM2='/'
        self.COURSE_NM='/'
    
    # 두 함수 다 데이터가 없는 경우에 대한 처리는 하지 않았음.
    # 카테고리로 검색해서 해당 정보를 모두 list 형태로 반환하는 함수.
    def search_category(self, category):
        result = []
        self.CATEGORY_NM2+=category
        self.url += self.CATEGORY_NM2
        
        response = requests.get(self.url)
        if response.status_code !=200:
            print("error : ", response.status_code)
        
        try:
            rows = response.json().get('OnlineCoures').get('row')
            for row in rows:
                result.append(row)
        except:
            print("search_category function error")
        return result
    
    # course_nm으로 검색해서 해당 정보를 모두 list 형태로 반환
    def search_course_nm_2(self, course_nm):
        result = []
        local_url = self.url+"/ /"+course_nm
        
        res = requests.get(local_url)
        if(res.status_code != 200):
            print("error : ",res.status_code)
        try:
            rows = res.json().get('OnlineCoures').get('row')
            for row in rows:
                result.append(row)
        except:
            print("search_course_nm2 function error")
        return result
    
    def get_course_nm(self, row):
        course_nm = row['COURSE_NM']
        return course_nm
    def get_course_request_dt(self, row):
        course_request_dt = row['COURSE_REQUEST_DT']
        return course_request_dt
    def get_course_dt(self, row):
        course_dt = row['COURSE_DT']
        return course_dt
    def get_dept_name(self, row):
        dept_name = row['DEPT_NAME']
        return dept_name
    def get_pre_url(self, row):
        return row['PRE_URL']

# using Test
c = CourseJson()
result = c.search_course_nm_2('에너지')
print("강좌명\t\t\t강의신청기간\t강의코스기간\t기관명")
for row in result:
    print(c.get_course_nm(row), c.get_course_request_dt(row), c.get_course_dt(row), c.get_dept_name(row),c.get_pre_url(row) )
