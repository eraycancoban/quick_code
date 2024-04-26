import math

# Noktaların tanımlanması
points = []

# Kullanıcıdan noktaların girişi
while True:
    point_str = input("Noktayı girin (x y şeklinde, çıkmak için q): ")
    if point_str.lower() == 'q':
        break
    try:
        x, y = map(float, point_str.split())
        points.append((x, y))
    except ValueError:
        print("Geçersiz giriş! Tekrar deneyin.")

# Öklid mesafesi için fonksiyon tanımlama
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Mesafelerin ve noktaların hesaplanması
distances = []
min_distance = float('inf')
min_points = ()

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)
        if distance < min_distance:
            min_distance = distance
            min_points = (points[i], points[j])

# Minimum mesafenin ve noktaların bulunması ve yazdırılması
if min_points:
    print("Minimum mesafe:", min_distance)
    print("Bu mesafeyi sağlayan noktalar:", min_points)
else:
    print("Hesaplanacak mesafe bulunamadı. En az iki nokta girmelisiniz.")
