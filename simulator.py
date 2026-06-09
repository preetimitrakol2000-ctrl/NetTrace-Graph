from graph_core import NetworkGraph
from detectors import check_routing_loops

if __name__ == "__main__":
    print("🕸️  Assembling NetworkTrace-Graph Topology Pipeline...")
    
    p2p_net = NetworkGraph()
    
    # Setting up standard peer paths
    p2p_net.connect_link("192.168.1.1", "192.168.1.2")
    p2p_net.connect_link("192.168.1.2", "192.168.1.3")
    
    # INJECTING MALICIOUS CYCLIC ROUTING LOOP (Denial of Service simulation)
    p2p_net.connect_link("192.168.1.3", "192.168.1.1")
    
    print("🚨 Scanning infrastructure layers for threat signatures...")
    loop_flag = check_routing_loops(p2p_net, "192.168.1.1")
    
    if loop_flag:
        print("🛑 ALARM: Circular Network Routing Loop / Malicious Ingestion Identified!")
    else:
        print("✅ Traffic lanes clear. Flow validation verified.")
