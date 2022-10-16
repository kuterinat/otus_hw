import pytest
from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


@pytest.mark.parametrize('figure, exp_data',
                         [(Circle(10), {'name': 'Circle', 'perimeter': 62.83185307179586, 'area': 314.1592653589793}),
                          (Circle(3.6), {'name': 'Circle', 'perimeter': 22.61946710584651, 'area': 40.71504079052372}),
                          (Rectangle(3, 4), {'name': 'Rectangle', 'perimeter': 14, 'area': 12}),
                          (Rectangle(5.7, 2.444), {'name': 'Rectangle', 'perimeter': 16.288, 'area': 13.9308}),
                          (Triangle(3, 5, 4), {'name': 'Triangle', 'perimeter': 12, 'area': 6}),
                          (Triangle(1.75, 3.18, 4), {'name': 'Triangle', 'perimeter': 8.93, 'area': 2.691371745852846}),
                          (Square(5), {'name': 'Square', 'perimeter': 20, 'area': 25}),
                          (Square(5.333), {'name': 'Square', 'perimeter': 21.332, 'area': 28.440889000000002})
                          ])
def test_check_attributes(figure, exp_data):
    """
        This test checks that each type of geometric figure has expected attributes name, perimeter and area
    """

    for attribute, value in exp_data.items():
        assert getattr(figure, attribute) == value, f'Attribute {attribute} should be {value}, ' \
                                                    f'but now it is {getattr(figure, attribute)}'


@pytest.mark.parametrize('triangle_params',
                         [(1, 1, 2),
                          (1, 1, 3)
                          ])
def test_check_error_triangle(triangle_params):
    """
        This test checks that expected error appears if try to create a triangle with incorrect parameters
    """

    with pytest.raises(ValueError) as err:
        Triangle(*triangle_params)
    assert err.value.args[0] == "Can't define a triangle with sides {}, {}, {}".format(*triangle_params)


@pytest.mark.parametrize('figure, params',
                         [(Circle, (-5,)),
                          (Circle, (0,)),
                          (Rectangle, (-4, 1)),
                          (Rectangle, (3, -5)),
                          (Rectangle, (-2, -3)),
                          (Rectangle, (0, 10)),
                          (Rectangle, (5, 0)),
                          (Triangle, (3, -5, 4)),
                          (Triangle, (-3, 5, 4)),
                          (Triangle, (3, 5, -4)),
                          (Triangle, (-3, -5, -4)),
                          (Triangle, (3, -5, -4)),
                          (Triangle, (0, 0, 0)),
                          (Triangle, (3, 5, 0)),
                          (Square, (-2,)),
                          (Square, (0,))
                          ])
def test_check_error_negative_params(figure, params):
    """
        This test checks that expected error appears if try to create a figure with zero or negative parameters
    """

    with pytest.raises(ValueError) as err:
        figure(*params)
    assert err.value.args[0] == "All figure params should be positive"


@pytest.mark.parametrize('figure_1, figure_2',
                         [(Circle(3), Circle(12)),
                          (Circle(3), Rectangle(2, 4)),
                          (Circle(3), Triangle(20, 30, 40)),
                          (Circle(3), Square(8)),
                          (Rectangle(2, 8), Rectangle(3, 14)),
                          (Rectangle(2, 5), Triangle(2, 3, 4)),
                          (Rectangle(6, 12), Square(7)),
                          (Triangle(3, 5, 4), Triangle(11, 7, 5)),
                          (Triangle(6, 8, 11), Square(15)),
                          (Square(6), Square(10))
                          ])
def test_check_add_area(figure_1, figure_2):
    """
        This test checks that add_area method returns expected value for each types of geometric figure
    """

    sum_area = figure_1.area + figure_2.area
    assert figure_1.add_area(figure_2) == sum_area
    assert figure_2.add_area(figure_1) == sum_area


@pytest.mark.parametrize('figure_1, figure_2',
                         [(Circle(3), 'some string'),
                          (Rectangle(2, 8), 15),
                          (Triangle(3, 5, 4), True),
                          (Square(6), None)
                          ])
def test_check_add_area_error(figure_1, figure_2):
    """
        This test checks that expected error appears if try to pass a non-figure parameter in add_area method
    """

    with pytest.raises(ValueError) as err:
        figure_1.add_area(figure_2)
    assert err.value.args[0] == "It is non-geometric figure"
