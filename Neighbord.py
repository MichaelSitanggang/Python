def find_neighbors():
    num_nodes = int(input("Masukkan jumlah simpul pada graph: "))
    node_neighbors = {}

    # Membaca input dan membangun daftar tetangga untuk setiap simpul
    for i in range(num_nodes):
        node = input("Masukkan nama simpul: ")
        neighbors = input("Masukkan tetangga dari simpul tersebut (dipisahkan dengan spasi): ").split()
        node_neighbors[node] = neighbors
    print(node_neighbors)
    # Mencetak tetangga untuk setiap simpul
    for node, neighbors in node_neighbors.items():
        neighbor_str = ",".join(neighbors)
        print(f"Tetangga dari {node} adalah {neighbor_str}")

find_neighbors()
