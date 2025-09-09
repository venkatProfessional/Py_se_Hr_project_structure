import pytest

from pages.HolidayCalender import HolidayAndCalender


@pytest.mark.usefixtures("driver", "login")
class  TestHolidayAndCalendarPage():


    def test_holiday_and_calendar_page(self,driver):
        page = HolidayAndCalender(driver)
        page.navigate_to_calender()
        page.implementing_calender()
