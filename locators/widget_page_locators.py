from selenium.webdriver.common.by import By


class AcordianPageLocators:
   FIRST_SECTION = (By.CSS_SELECTOR, "div[id='section1Heading']")
   FIRST_SECTION_CONTENT =(By.CSS_SELECTOR, "div[id ='section1Content'] p")
   SECOND_SECTION =(By.CSS_SELECTOR, "div[id='section2Heading']")
   SECOND_SECTION_CONTENT =(By.CSS_SELECTOR, "div[id ='section2Content'] p")
   THIRD_SECTION =(By.CSS_SELECTOR, "div[id='section3Heading']")
   THIRD_SECTION_CONTENT =(By.CSS_SELECTOR, "div[id ='section3Content'] p ")

class AutoCompletePageLocators:
   MULTI_INPUT =  (By.CSS_SELECTOR, "input[id='autoCompleteMultipleInput']")
   MULTI_VALUE =  (By.CSS_SELECTOR, "div[class='css-1rhbuit-multiValue auto-complete__multi-value']")
   MULTI_VALUE_REMOVE  =  (By.CSS_SELECTOR, "div[class='css-1rhbuit-multiValue auto-complete__multi-value'] svg path")
   SINGLE_CONTAINER = (By.CSS_SELECTOR, "div[class ='auto-complete__single-value css-1uccc91-singleValue']")
   SINGLE_INPUT = (By.CSS_SELECTOR, "input[id='autoCompleteSingleInput']")


class DatePickerPageLocators:
   DATE_INPUT= (By.CSS_SELECTOR, "input[id='datePickerMonthYearInput']")
   DATE_SELECT_MONTH =(By.CSS_SELECTOR, "select[class='react-datepicker__month-select']")
   DATE_SELECT_YEAR = (By.CSS_SELECTOR, "select[class='react-datepicker__year-select']")
   DATE_SELECT_DAY= (By.CSS_SELECTOR, "div[class^='react-datepicker__day react-datepicker__day']")

   DATE_AND_TIME_INPUT= (By.CSS_SELECTOR, "input[id='dateAndTimePickerInput']")
   DATE_AND_TIME_MONTH=(By.CSS_SELECTOR, "div[class='react-datepicker__month-read-view']")
   DATE_AND_TIME_YEAR=(By.CSS_SELECTOR, "div[class='react-datepicker__year-read-view']")

   DATE_AND_TIME_TIME_LIST=(By.CSS_SELECTOR, "li[class='react-datepicker__time-list-item ']")
   DATE_AND_TIME_MONTH_LIST=(By.CSS_SELECTOR, "div[class='react-datepicker__month-option']")
   DATE_AND_TIME_YEAR_LIST=(By.CSS_SELECTOR, "div[class='react-datepicker__year-option']")

class SlidePageLocators:

   INPUT_SLIDER = (By.CSS_SELECTOR, "input[class='range-slider range-slider--primary']")
   SLIDER_VALUE =(By.CSS_SELECTOR, "input[id='sliderValue']")

class ProgressBarPageLocators:
   PROGRESS_BAR_BUTTON  = (By.CSS_SELECTOR, "button[id='startStopButton']")
   PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, "div[class='progress-bar bg-info']")

class TabPageLocators:
   TABS_WHAT = (By.CSS_SELECTOR, "a[id='demo-tab-what']")
   TABS_WHAT_CONTENT= (By.CSS_SELECTOR, "div[id='demo-tabpane-what']")

   TABS_ORIGIN= (By.CSS_SELECTOR, "a[id='demo-tab-origin']")
   TABS_ORIGIN_CONTENT= (By.CSS_SELECTOR, "div[id='demo-tabpane-origin']")

   TAB_USE= (By.CSS_SELECTOR, "a[id='demo-tab-use']")
   TAB_USE_CONTENT= (By.CSS_SELECTOR, "div[id='demo-tabpane-use']")

   TABS_MORE= (By.CSS_SELECTOR, "a[id='demo-tab-more']")
   TABS_MORE_CONTENT= (By.CSS_SELECTOR, "div[id='demo-tabpane-more']")

class ToolTipsPageLocators:

   TOOL_TIP_BUTTON   = (By.CSS_SELECTOR, "button[id='toolTipButton']")
   TOOL_TIP_BUTTON_SHADDOW = (By.CSS_SELECTOR, "button[aria-describedby='buttonToolTip']")
   TOOL_TIP_FIELD   = (By.CSS_SELECTOR, "input[id='toolTipTextField']")
   TOOL_TIP_FIELD_SHADOW = (By.CSS_SELECTOR, "input[aria-describedby='textFieldToolTip']")
   CONTRARY_LINK =  (By.XPATH, "//*[.='Contrary']")
   CONTRARY_SHADOW = (By.CSS_SELECTOR, "a[aria-describedby='contraryTexToolTip']")
   SECTION_LINK =(By.XPATH, "//*[.='1.10.32']")
   SECTION_SHADOW = (By.CSS_SELECTOR, "a[aria-describedby='sectionToolTip']")
   TOOL_TIP_INNER = (By.CSS_SELECTOR, "div[class='tooltip-inner']")

class MenuPageLocators:

   MENU_ITEM = (By.CSS_SELECTOR, "ul[id = 'nav'] li a")

class SelectMenuPageLocators:
   SELECT_VALUE_BUTTON= (By.CSS_SELECTOR,"div[id= 'withOptGroup']")
   SELECT_VALUE_BUTTON_SELECTOR = (By.CSS_SELECTOR,"div[class='css-26l3qy-menu']")
   SELECT_COLOR =  (By.CSS_SELECTOR,"select[id= 'oldSelectMenu']")




















