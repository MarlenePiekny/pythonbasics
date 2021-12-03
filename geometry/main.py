import math


def calculate_data_from_rectangle(height: float, width: float) -> dict:
    return {"area": height * width, "perimeter": (height + width) * 2}


def calculate_data_from_circle(radius: float):
    return {"area": math.pi * radius**2, "perimeter": 2 * math.pi * radius}


def calculate_data_from_cuboid(height: float, width: float, length: float) -> dict:
    return {"volume": calculate_data_from_rectangle(height, width)["area"] * length}


def calculate_data_from_cylinder(radius: float, height: float):
    return {"volume": calculate_data_from_circle(radius)["area"] * height}


def main():
    rectangle_data = calculate_data_from_rectangle(10, 20)
    assert rectangle_data["area"] == 200
    assert rectangle_data["perimeter"] == 60

    circle_data = calculate_data_from_circle(5)
    assert circle_data["area"] == math.pi * 5**2
    assert circle_data["perimeter"] == 2 * math.pi * 5

    cuboid_data = calculate_data_from_cuboid(10, 20, 30)
    assert cuboid_data["volume"] == 6000

    cylinder_data = calculate_data_from_cylinder(2.5, 10)
    assert cylinder_data["volume"] == math.pi * 2.5**2 * 10


if __name__ == '__main__':
    main()
