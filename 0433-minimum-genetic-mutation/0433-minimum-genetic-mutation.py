class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)

        if endGene not in bank:
            return -1

        def find_neighbor(gene):
            neighbors = set()
            choices = ['A', 'C', 'G', 'T']
            for i in range(8):
                for choice in choices:
                    if choice == gene[i]:
                        continue

                    new_gene = gene[:i] + choice + gene[i+1:]
                    if new_gene in bank:
                        neighbors.add(new_gene) 

            return neighbors

        queue = deque([(startGene, 0)])
        seen = set()

        while queue:
            gene, step = queue.popleft()

            if gene == endGene:
                return step

            neighbors = find_neighbor(gene)
            for neighbor in neighbors:
                if neighbor not in seen and neighbor in bank:
                    seen.add(neighbor)
                    queue.append((neighbor, step+1))

        return -1
                
        