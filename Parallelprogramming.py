import time
import threading
import multiprocessing
from multiprocessing.pool import Pool

class Shape:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

def calculate_shape_area(shape):
    return shape.area()

def calculate_sum_areas(shapes):
    return sum([shape.area() for shape in shapes])

def calculate_difference_areas(shapes):
    return shapes[0].area() - shapes[1].area()

def calculate_area_fitting(shape1, shape2):
    return shape1.area() // shape2.area()

def perform_multithreading(shapes):
    start_time = time.time()
    with Pool() as pool:
        results = pool.map(calculate_shape_area, shapes)
    end_time = time.time()
    print("Multithreading Execution Time:", end_time - start_time)
    return results

def perform_multiprocessing(shapes):
    start_time = time.time()
    with Pool() as pool:
        results = pool.map(calculate_shape_area, shapes)
    end_time = time.time()
    print("Multiprocessing Execution Time:", end_time - start_time)
    return results

def perform_hybrid(shapes):
    start_time = time.time()
    processes = 5
    streams_per_process = 20
    chunksize = max(len(shapes) // processes, 1)  # Ensure chunksize is never zero

    def calculate_shape_area_multi(shapes):
        with Pool(processes=streams_per_process) as pool:
            return pool.map(calculate_shape_area, shapes)

    with Pool(processes=processes) as pool:
        results = pool.map(calculate_shape_area_multi, [shapes[i:i+chunksize] for i in range(0, len(shapes), chunksize)])

    end_time = time.time()
    print("Hybrid Execution Time:", end_time - start_time)
    return results


if __name__ == "__main__":
    shapes = [Shape("Rectangle", 3, 4), Shape("Square", 2, 2), Shape("Circle", 5, 5)]

    # Multithreading
    multithreading_results = perform_multithreading(shapes)

    # Multiprocessing
    multiprocessing_results = perform_multiprocessing(shapes)

    # Hybrid
    hybrid_results = perform_hybrid(shapes)

    print("Multithreading Results:", multithreading_results)
    print("Multiprocessing Results:", multiprocessing_results)
    print("Hybrid Results:", hybrid_results)
