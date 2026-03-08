import numpy as np

class SemanticCache:

    def __init__(self, threshold=0.85):

        self.cache = []
        self.threshold = threshold

        self.hit = 0
        self.miss = 0

    def cosine(self,a,b):

        return np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))

    def lookup(self, query_vec):

        best_score = 0
        best_item = None

        for item in self.cache:

            score = self.cosine(query_vec, item["vector"])

            if score > best_score:
                best_score = score
                best_item = item

        if best_score > self.threshold:
            self.hit += 1
            return True, best_item, best_score

        self.miss += 1
        return False, None, best_score

    def store(self, query, vector, result, cluster):

        self.cache.append({
            "query": query,
            "vector": vector,
            "result": result,
            "cluster": cluster
        })

    def stats(self):

        total = self.hit + self.miss

        return {
            "total_entries": len(self.cache),
            "hit_count": self.hit,
            "miss_count": self.miss,
            "hit_rate": self.hit/total if total>0 else 0
        }

    def clear(self):

        self.cache = []
        self.hit = 0
        self.miss = 0
