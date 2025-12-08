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
        self.total_distance = 0
        self.connection_count = 0
    
    def add_connection(self, connection):
        self.connections.append(connection)
        self.total_distance += connection.distance
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

        #add lowest distance to circuit
        circuit_connections = []
        first_circuit = Circuit()
        first_circuit.add_connection(connections[0])
        circuit_connections.append(first_circuit)
        for connection in connections:
            for circuit in circuit_connections:
                if circuit.is_in_circuit(connection):
                    break
                if circuit.is_connected_to_circuit(connection):
                    circuit.add_connection(connection)
                    break
                else:
                    new_circuit = Circuit()
                    new_circuit.add_connection(connection)
                    circuit_connections.append(new_circuit)
                    break
        
        # count size of 3 largest circuits
        circuit_connections.sort(key=lambda x: x.connection_count, reverse=True)
        largest_circuits = circuit_connections[:3]
        total_size = 1
        for circuit in largest_circuits:
            print(f'Circuit with {circuit.connection_count} connections and total distance {circuit.total_distance}')
            total_size += circuit.connection_count
        return total_size

class partB:
    def solve(self, input_path):
        pass
