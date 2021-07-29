import requests
import jsonpickle
from alarm import Alarm
BASE_URL="/tmf-api/alarmManagement/v1"
class AlarmRemoteService:
    
    def __init__(self, baseURL, username, password):
        self.baseURL = baseURL
        self.username = username
        self.password = password

    def create_alarm(self,alarm):
        data = alarm.__dict__
        response = requests.post(self.baseURL+BASE_URL+"/alarm", json=data)
         if (response.status_code == 200):
            print("Successfully created alarm")
                # Code here will only run if the request is successful
        else:
            print("failed request")
        return response

if __name__ == '__main__':
      webserice = AlarmRemoteService("http://localhost","username","password")
      alarm = Alarm()
      alarm.setSourceSystemId("ems-1")
      alarm.setExternalAlarmId("5551212")
      alarm.setState("raised")
      alarm.setAlarmType("environmentalAlarm")
      alarm.setPerceivedSeverity("minor")
      alarm.setProbableCause("rectifierLowVoltage")
      alarm.setSourceSystemId("ems-1")
      alarm.setAlarmRaisedTime("2019-07-03T03:32:17.235Z")
      alarm.setAlarmReportingTime("2019-07-03T03:32:17.552Z")
      response = webserice.create_alarm(alarm)
      response_str = jsonpickle.encode(response)
      print(response_str)

      
    