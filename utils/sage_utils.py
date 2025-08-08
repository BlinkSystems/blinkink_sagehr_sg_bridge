import json
from pprint import pprint, pformat
import logging

logger = logging.getLogger(__name__)
import urllib3
import constants

http = urllib3.PoolManager()


def get_sage_user(user_id, team_history=False, position_history=False, employment_status_history=False):
    """
    Get a user from SageHR
    :param user_id: User ID
    :param employment_status_history:
    :param position_history:
    :param team_history:
    :return:
    {
      "data": {
        "id": 19,
        "email": "john@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "picture_url": "https://example.com/john.png",
        "employment_start_date": "2014-08-25",
        "date_of_birth": "1991-02-13",
        "team": "Sage HR",
        "team_id": 6742,
        "position": "Api developer",
        "position_id": 123,
        "reports_to_employee_id": 5,
        "work_phone": "555-0505",
        "home_phone": "555-0506",
        "mobile_phone": "555-0507",
        "gender": "Male",
        "street_first": "84 Glenwood Street",
        "street_second": "Peoria",
        "city": "London",
        "post_code": 99999,
        "country": "GB",
        "employee_number": "A1",
        "irregular_contract_worker": true,
        "employment_status": "Full-time",
        "nationality": "Spanish",
        "marital_status": "Married",
        "personal_identification_number": "1",
        "tax_number": "1",
        "team_history": [
          {
            "team_id": 1,
            "start_date": "2018-01-01",
            "end_date": "201-01-01",
            "team_name": "Some Team"
          }
        ],
        "employment_status_history": [
          {
            "employment_status_id": 1,
            "start_date": "2018-01-01",
            "end_date": "201-01-01",
            "employment_statu_name": "Full time"
          }
        ],
        "position_history": [
          {
            "position_id": 1,
            "start_date": "2018-01-01",
            "end_date": "201-01-01",
            "position_name": "Developer",
            "position_code": "1234"
          }
        ]
      }
    }
    """
    url = f"{constants.SAGEHR_API_URL}/api/employees/{user_id}"

    if team_history or position_history or employment_status_history:
        url += "?"
        if team_history:
            url += "team_history=true&"
        if position_history:
            url += "position_history=true&"
        if employment_status_history:
            url += "employment_status_history=true"

    response = http.request('GET', url)

    data = json.loads(response.data.decode('utf-8'))
    if data:
        return data.get("data", [])


def get_sage_leave_requests():
    """
    Get all leave requests from SageHR
    :return:
    {
      "data": [
        {
          "id": 2902504,
          "status": "Approved",
          "status_code": "approved",
          "policy_id": 1,
          "employee_id": 1,
          "replacement": {
            "id": 2,
            "full_name": "John Doe"
          },
          "details": "Birthday lunch",
          "is_multi_date": false,
          "is_single_day": true,
          "is_part_of_day": true,
          "first_part_of_day": false,
          "second_part_of_day": true,
          "start_date": "2018-05-24",
          "end_date": "2018-05-24",
          "request_date": "2018-05-22",
          "approval_date": {},
          "hours": 3.5,
          "fields": [
            {
              "title": "Approved by manager?",
              "answer": "yes"
            }
          ]
        }
      ],
      "meta": {
        "current_page": 1,
        "next_page": 2,
        "previous_page": {},
        "total_pages": 2,
        "per_page": 50,
        "total_entries": 75
      }
    }
    """
    url = f"{constants.SAGEHR_API_URL}/api/leave-management/requests"
    response = http.request('GET', url)

    data = json.loads(response.data.decode('utf-8'))
    if data:
        return data.get("data", [])
