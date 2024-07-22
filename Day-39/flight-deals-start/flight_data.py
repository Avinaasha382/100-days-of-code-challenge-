class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,price,destination_code,departure_date):
        self.price = price
        self.destination_code = destination_code
        self.departure_date = departure_date
        
        