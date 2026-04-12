INSERT INTO flights_airport (name, city, country, iata_code) VALUES
('Islam Karimov International', 'Tashkent', 'Uzbekistan', 'TAS'),
('Sheremetyevo', 'Moscow', 'Russia', 'SVO'),
('Heathrow', 'London', 'UK', 'LHR');

INSERT INTO aircraft_aircrafttype (name, manufacturer, total_seats) VALUES
('Boeing 737', 'Boeing', 180),
('Airbus A320', 'Airbus', 150);

INSERT INTO aircraft_aircraft (tail_number, aircraft_type_id, is_active) VALUES
('HY-001', 1, true),
('HY-002', 2, true);
