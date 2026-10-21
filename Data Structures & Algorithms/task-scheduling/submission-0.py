class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
         # Conta quantas vezes cada tarefa aparece
        freq = Counter(tasks)

        # Transforma as frequencias em negativas pra simular um max-heap
        heap = [-count for count in freq.values()]
        heapq.heapify(heap)

        # Guarda as tarefas que ainda estao em cooldown
        # Cada elemento vai ser (frequencia_restante, tempo_de_liberacao)
        cooldown = deque()

        time = 0

        # Continua enquanto tiver tarefa pra executar ou esperando cooldown
        while heap or cooldown:
            time += 1

            # Se tiver alguma tarefa disponivel, pega a mais frequente
            if heap:
                count = heapq.heappop(heap)

                # Diminui uma execucao da tarefa
                # Como a frequencia e negativa, somar 1 diminui a frequencia real
                count += 1

                # Se ainda faltam execucoes dessa tarefa, ela precisa esperar
                if count < 0:
                    cooldown.append((count, time + n))

            # Se a primeira tarefa da fila ja cumpriu o cooldown,
            # ela pode voltar pro heap e ser executada novamente
            if cooldown and cooldown[0][1] == time:
                count, available_time = cooldown.popleft()
                heapq.heappush(heap, count)

        # Retorna o tempo total, incluindo os intervalos ociosos
        return time
