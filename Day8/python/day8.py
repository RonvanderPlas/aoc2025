import math

class JunctionConnection:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.distance = self.calculate_distance()

    def calculate_distance(self):
        return math.sqrt((self.point1[0]-self.point2[0])**2 + (self.point1[1]-self.point2[1])**2 + (self.point1[2]-self.point2[2])**2)

class Circuit:
    def __init__(self):
        self.connections = []
        self.junction_boxes = set()
        self.total_distance = 0
        self.connection_count = 0
    
    def add_connection(self, connection):
        self.connections.append(connection)
        self.total_distance += connection.distance
        self.junction_boxes.add(connection.point1)
        self.junction_boxes.add(connection.point2)
        self.connection_count += 1
    
    def is_in_circuit(self, connection):
        for conn in self.connections:
            if {conn.point1, conn.point2} == {connection.point1, connection.point2}:
                return True
        return False

    def is_connected_to_circuit(self, connection):
        for conn in self.connections:
            if connection.point1 in [conn.point1, conn.point2] or connection.point2 in [conn.point1, conn.point2]:
                return True
        return False

class partA:
    def read_file(self, input_path):
        with open(input_path, "r") as f:
            inputs = []
            for line in f:
                inputs.append(tuple(map(int, line.rstrip("\n").split(","))))
        return inputs

    def solve(self, input_path):
        connections = []
        junction_boxes = self.read_file(input_path)
        for first_junction in junction_boxes:
            for second_junction in junction_boxes:
                if first_junction == second_junction:
                    continue
                connection = JunctionConnection(first_junction, second_junction)
                connections.append(connection)
        
        #sort connections by distance
        connections.sort(key=lambda x: x.distance)

        #limit to 10
        connections = connections[:10]
        #add lowest distance to circuit
        circuit_connections = []
        first_circuit = Circuit()
        first_circuit.add_connection(connections[0])
        circuit_connections.append(first_circuit)
        for connection in connections:
            print(f"checking connection between {connection.point1} and {connection.point2} with distance {connection.distance}")
            in_circuits = []
            for idx, circuit in enumerate(circuit_connections):
                if circuit.is_in_circuit(connection):
                    print(f'Connection between {connection.point1} and {connection.point2} with distance {connection.distance} already in circuit')
                    break
                if circuit.is_connected_to_circuit(connection):
                    in_circuits.append(idx)
            if len(in_circuits) == 0:
                new_circuit = Circuit()
                new_circuit.add_connection(connection)
                print(f'Creating new circuit with connection between {connection.point1} and {connection.point2} with distance {connection.distance}')
                circuit_connections.append(new_circuit)
            elif len(in_circuits) == 1:
                print(f'Adding connection between {connection.point1} and {connection.point2} with distance {connection.distance} to existing circuit')
                circuit_connections[in_circuits[0]].add_connection(connection)
            else:
                # Merge all involved circuits
                print(f'Merging circuits for connection between {connection.point1} and {connection.point2} with distance {connection.distance}')
                # Collect circuits to merge
                circuits_to_merge = [circuit_connections[idx] for idx in in_circuits]
                merged_circuit = Circuit()
                for c in circuits_to_merge:
                    for conn in c.connections:
                        merged_circuit.add_connection(conn)
                merged_circuit.add_connection(connection)
                # Remove merged circuits from circuit_connections
                circuit_connections = [c for i, c in enumerate(circuit_connections) if i not in in_circuits]
                circuit_connections.append(merged_circuit)
        
        #print first cicuit details
        #for connections in circuit_connections[0].connections:
         #   print(f'Circuit connection between {connections.point1} and {connections.point2} with distance {connections.distance}')
        # count size of 3 largest circuits
        circuit_connections.sort(key=lambda x: x.connection_count, reverse=True)
        largest_circuits = circuit_connections[:3]
        total_size = 1
        for circuit in largest_circuits:
            print(f"ammount of junction boxes in circuit: {len(circuit.junction_boxes)}")
            total_size *= len(circuit.junction_boxes)
        return total_size

class partB:
    def solve(self, input_path):
        pass
