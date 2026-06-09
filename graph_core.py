class NetworkGraph:
    def __init__(self):
        # Graph represented natively using an Adjacency List Dictionary
        self.adj_list = {}

    def add_node(self, ip_address):
        if ip_address not in self.adj_list:
            self.adj_list[ip_address] = []

    def connect_link(self, source, destination):
        self.add_node(source)
        self.add_node(destination)
        self.adj_list[source].append(destination)
