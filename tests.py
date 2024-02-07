from rubik_cube import Cube


def test105():
    for i, m1 in enumerate(['U', 'R', 'L', 'D', 'F', 'B', ]):
        for j, m2 in enumerate(['D', 'L', 'R', 'U', 'B', 'F']):
            cube = Cube()
            if i != j and m1 != m2:
                print(f'{m1} {m2} Test')
                for k in range(105):
                    getattr(cube, m1).__getattribute__(m2)
                assert cube.is_solved()

    for i, m1 in enumerate(['Ui', 'Ri', 'Li', 'Di', 'Fi', 'Bi', ]):
        for j, m2 in enumerate(['Di', 'Li', 'Ri', 'Ui', 'Bi', 'Fi']):
            cube = Cube()
            if i != j and m1 != m2:
                print(f'{m1} {m2} Test')
                for k in range(105):
                    getattr(cube, m1).__getattribute__(m2)
                assert cube.is_solved()

def test_formula():
    cube = Cube()

    cube.F.R.U.Ri.Ui.Fi
    assert cube.layer2_solved()

    cube.F.U.R.Ui.Ri.Fi
    assert cube.layer2_solved()



if __name__ == "__main__":
    test105()
    test_formula()