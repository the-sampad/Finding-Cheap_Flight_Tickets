import requests
from flight_details import Flight_Details
from flight_sheets import Sheet
from flight_data import Flight_data
from message import Message
# from users_sheet import UserSheet
# from users_mail import Mail

flight = Flight_Details()
sheet = Sheet()

origin_city = 'London'

dest_data_sheet = sheet.get_sheet_data()

dest_cities = sheet.get_city_names()

# adding IATA codes and update sheet
for ci in dest_cities:
    iata_code = flight.get_iata_code(ci)
    for dic in dest_data_sheet:
        if ci == dic['city']:
            sheet.update_iata_code(code=iata_code,city=ci)

updated_data_sheet = sheet.get_sheet_data()
# user_mail = Mail()
# user_sheet = UserSheet()
# user_sheet.add_user()

# Check cheapest flight data in flight_details for all required destinations in sheet
org_code = flight.get_iata_code(origin_city)
for detail in updated_data_sheet:
    dest_code = detail['iataCode']
    try:
        price_data = flight.get_available_flights(fly_from_code=org_code, fly_to_code=dest_code)
        flightdata = Flight_data(
            org_city=price_data['city_from'],
            org_airport_code=price_data['airport_from'],
            dest__city=price_data['city_to'],
            dest_airport_code=price_data['airport_to'],
            cheap_price=price_data['price'],
            airlines=price_data['airline'],
            flight_num=price_data['flight_no'],
            dep_time=price_data['dep_time'],
            arr_time=price_data['arr_time']
        )
        message_txt = (
            f'''Flight✈️ to {flightdata.dest__city} got cheaper.
            Price = {flightdata.cheap_price}
            Departure : {flightdata.org_city} ({flightdata.org_airport_code})  {flightdata.dep_time}
            Arrival : {flightdata.dest__city} ({flightdata.dest_airport_code})  {flightdata.arr_time}
            Airplane : {flightdata.airlines}-{flightdata.flight_num}'''
        )

        mess = Message()
        mess.send_message(message_text=message_txt)
        # user_sheet.get_users()
        # for user in user_sheet:
        #     u_email = user['email']
        #     user_mail.send_mail(msg_text=message_txt, user_email=u_email)

    except IndexError:
        pass
    

