class Packet:
    def __init__(self, client_id, client_ip_address, destination_ip_address, payload, total_num_packets, current_packet_id, message_name, security_certificate):
        self.client_id = client_id
        self.client_ip_address = client_ip_address
        self.destination_ip_address = destination_ip_address
        self.payload = payload
        self.total_num_packets = total_num_packets
        self.current_packet_id = current_packet_id
        self.message_name = message_name
        self.security_certificate = security_certificate
