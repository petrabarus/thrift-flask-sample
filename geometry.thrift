
namespace php petrabarus
namespace py petrabarus

struct Point {
    1: required double x;
    2: required double y;
}

service Geometry {
    double distance(1: Point a, 2: Point b);
}
