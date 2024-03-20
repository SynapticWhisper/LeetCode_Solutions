from functools import reduce

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        self.queue = sorted(set(tasks))
        
        self.tasks: dict = {key: 0 for key in self.queue}
        for task in tasks:
            self.tasks[task] += 1
        
        result = 0

        self.task_list = []
        
        while len(self.queue) > 0:
            
            for _ in range(n+1):
                if self.queue:
                    self.task_list.append(self.queue.pop(0))
                else:
                    self.task_list.append(False)

            while reduce(lambda x, y: bool(x) | bool(y), self.task_list):
                for i in range(n+1):
                    if not self.task_list[i]:
                        if reduce(lambda x, y: bool(x) | bool(y), self.task_list):
                            result += 1
                        else:
                            break
                    else:
                        result += self.check(i)
                else:
                    continue
                break
        
        return result
                

    def check(self, index: int):
        task = self.task_list[index]
        count = self.tasks.get(task)
        value = 0

        if count > 0:
            self.tasks[task] -= 1
            value += 1

        if self.tasks.get(task) == 0:
            if not self.queue:
                self.task_list[index] = False
                return value
            else:
                new_val = self.queue.pop(0)
                self.task_list[index] = new_val
                return value
        
        return value
        

if __name__ == "__main__":
    print(Solution().leastInterval(["A","A","A","B","B","B", "C","C","C", "D", "D", "E"], 2))