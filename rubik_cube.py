class Cube:
    def __init__(self):
        self.faces = list(range(55))
        self.original = list(range(55))
        # 底层
        self.layer1 = [46, 47, 48, 49, 50, 51, 52, 53, 54, 43, 44, 45, 10, 19, 28, 18, 27, 36, 1, 2, 3]
        self.layer2 = [46, 47, 48, 49, 50, 51, 52, 53, 54, 43, 44, 45, 10, 19, 28, 18, 27, 36, 1, 2, 3, 11, 20, 29, 40, 41, 42, 17, 26, 35, 4, 5, 6]

        self.face_names = [None, 
                        'B1', 'B2', 'B3', 
                        'B4', 'B5', 'B6',
                        'B7', 'B8', 'B9',
            
    'L1', 'L2', 'L3',   'U1', 'U2', 'U3',   'R1', 'R2', 'R3',   
    'L4', 'L5', 'L6',   'U4', 'U5', 'U6',   'R4', 'R5', 'R6',
    'L7', 'L8', 'L9',   'U7', 'U8', 'U9',   'R7', 'R8', 'R9',

                        'F1', 'F2', 'F3',
                        'F4', 'F5', 'F6',
                        'F7', 'F8', 'F9',

                        'D1', 'D2', 'D3',
                        'D4', 'D5', 'D6',
                        'D7', 'D8', 'D9'
                        ]
                                            
    
    def _permutation(self, permutation):
        """
        对列表cube中指定位置的元素进行循环置换。
        
        :param positions: 一个列表，包含了参与置换的元素的索引位置。
        """
        
        # 保存最后一个位置的元素，因为它将被移动到第一个位置
        last_element = self.faces[permutation[-1]]
        
        # 从后向前循环，每个元素移动到下一个位置
        for i in range(len(permutation) - 1, 0, -1):
            self.faces[permutation[i]] = self.faces[permutation[i-1]]
        
        # 将最后一个元素移动到第一个位置
        self.faces[permutation[0]] = last_element
    
    def _permutations(self, permutations):
        """
        对列表cube中指定位置的元素进行循环置换。
        
        :param permutations: 一个列表，包含了参与置换的元素的索引位置。
        """
        for permutation in permutations:
            self._permutation(permutation)
    
    def rotate(self, moves: str):
        """
        旋转魔方。
        
        :param instruction: 一个字符串，包含了旋转魔方的指令。
        """
        moves = moves.replace("'", "i")
        for move in moves.split(' '):
            getattr(self, move)
        return self


    @staticmethod     
    def representation(permutation):
        """
        返回魔方的表示。
        """
        assert len(permutation) == 55

        note = [False] * 55
        cycles = []

        for i in range(55):
            if note[i]:
                continue
            cycle = [i]
            next = permutation[i]
            while next != i:
                note[next] = True
                cycle.append(next)
                next = permutation[next]
            if len(cycle) > 1:
                cycles.append(cycle[::-1])
        return cycles
    
    def readable_representation(self, permutation):
        """
        返回魔方的可读表示。
        """
        cycles = self.representation(permutation)
        return [[self.face_names[i] for i in cycle] for cycle in cycles]

        
    def is_solved(self):
        """
        判断魔方是否已经还原。
        """
        result = [self.faces[i] == self.original[i] for i in range(55)]
        return all(result)
    
    def layer1_solved(self):
        """
        判断魔方第一层（底层）是否已经还原。
        """
        result = [self.faces[i] == i for i in self.layer1]
        return all(result)
    
    def layer2_solved(self):
        """
        判断魔方第二层是否已经还原。
        """
        result = [self.faces[i] == i for i in self.layer2]
        return all(result)

    @property
    def U(self):
        self._permutations([[13, 15, 33, 31], [22, 14, 24, 32], [16, 39, 30, 7], [25, 38, 21, 8], [34, 37, 12, 9]])
        return self

    @property
    def Ui(self):
        self._permutations([[31, 33, 15, 13], [32, 24, 14, 22], [7, 30, 39, 16], [8, 21, 38, 25], [9, 12, 37, 34]])
        return self
    
    @property
    def U2(self):
        return self.U.U
    
    @property
    def R(self):
        self._permutations([[16, 18, 36, 34], [25, 17, 27, 35], [51, 42, 24, 6], [48, 39, 15, 3], [54, 45, 33, 9]])
        return self
    
    @property
    def Ri(self):
        self._permutations([[34, 36, 18, 16], [35, 27, 17, 25], [6, 24, 42, 51], [3, 15, 39, 48], [9, 33, 45, 54]])
        return self
    
    @property
    def R2(self):
        return self.R.R
    
    @property
    def L(self):
        self._permutations([[10, 12, 30, 28], [19, 11, 21, 29], [1, 13, 37, 46], [4, 22, 40, 49], [7, 31, 43, 52]])
        return self
    
    @property
    def Li(self):
        self._permutations([[28, 30, 12, 10], [29, 21, 11, 19], [46, 37, 13, 1], [49, 40, 22, 4], [52, 43, 31, 7]])
        return self
    
    @property
    def L2(self):
        return self.L.L

    @property
    def D(self):
        self._permutations([[46, 48, 54, 52], [47, 51, 53, 49], [43, 36, 3, 10], [44, 27, 2, 19], [45, 18, 1, 28]])
        return self
    
    @property
    def Di(self):
        self._permutations([[52, 54, 48, 46], [49, 53, 51, 47], [10, 3, 36, 43], [19, 2, 27, 44], [28, 1, 18, 45]])
        return self
    
    @property
    def D2(self):
        return self.D.D
    
    @property
    def F(self):
        self._permutations([[37, 39, 45, 43], [38, 42, 44, 40], [46, 30, 33, 36], [47, 29, 32, 35],[48, 28, 31, 34]])
        return self
    
    @property
    def Fi(self):
        self._permutations([[43, 45, 39, 37], [40, 44, 42, 38], [36, 33, 30, 46], [35, 32, 29, 47],[34, 31, 28, 48]])
        return self
    
    @property
    def F2(self):
        return self.F.F
    
    @property
    def B(self):
        self._permutations([[1, 3, 9, 7], [2, 6, 8, 4], [16, 13, 10, 54], [17, 14, 11, 53], [18, 15, 12, 52]])
        return self
    
    @property
    def Bi(self):
        self._permutations([[7, 9, 3, 1], [4, 8, 6, 2], [54, 10, 13, 16], [53, 11, 14, 17], [52, 12, 15, 18]])
        return self
    
    @property
    def B2(self):
        return self.B.B

    
if __name__ == "__main__": 
    cube = Cube()
    print(Cube.readable_representation(cube, cube.rotate("R L U2 F U' D F2 R2 B2 L U2 F' B' U R2 D F2 U R2 U").faces))
