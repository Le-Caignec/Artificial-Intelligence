 # def Search_5_objectives(self, start_case):
    #     L=[]
    #     n= len(L)
    #     for Obj in self.objectif:
    #         dist_obj = self.Distance(start_case, Obj)
    #         if n<5:
    #             bool=True
    #             for i in range(n):
    #                 if dist_obj <L[i][1] and bool:
    #                     L = L[:i] + [(Obj, dist_obj)] + L[i:]
    #                     bool=False
    #             if bool:
    #                 L.append((Obj,self.Distance(start_case, Obj)))
    #         else:
    #             bool = True
    #             for i in range(n):
    #                 if dist_obj<L[i][1] and bool:
    #                     L = L[:i] + [(Obj, dist_obj)] + L[i:-1]
    #                     bool=False
    #     return L

    # def Parcours(self, i, distance, distance_min, List, bool):
    #     n = len(self.objectif)
    #     distance += self.Distance(List[-1], self.objectif[i])
    #     if distance >= distance_min:
    #         return distance, List, False
    #     elif bool:
    #         List.append(self.objectif[i])
    #         if n == 1:
    #             return distance, List, True
    #         else:
    #             self.objectif.pop(i)
    #             for j in range(n):
    #                 distance, List, bool = self.Parcours(self.objectif, j, distance, distance_min, List, True)
    #                 return 