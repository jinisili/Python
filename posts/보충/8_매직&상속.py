# %%

# magic method
class Book:
    def __init__(self, title, author, pages):
        '''
        생성자 메서드 : 객체가 생성될 때 호출
        '''
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        '''
        문자열 표현 메서드 : 객체를 문자열로 표현할 때 호출
        ex) print(obj), str(obj)
        '''
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        '''
        문자열 표현 메서드 : 컬렉션 내의 객체를 문자열로 표현할 때 호출
        ex) __str__이 정의가 안 된 경우, print([obj, ])
        '''
        return f'({str(self)})'

    def __len__(self):
        '''
        길이 메서드 : len() 함수에 객체가 인자로 들어갈 때 호출
        '''
        return self.pages
    
    def __getitem__(self, page):
        '''
        인덱싱 메서드 : 객체에 대해 인덱싱 또는 슬라이싱이 수행될 때 호출
        '''
        if 1 <= page <= self.pages:
            return f'Content of page {page}'
        else:
            # 에러를 발생
            raise IndexError('페이지 범위를 벗어났습니다.')

    def __hash__(self) -> int:
        '''
        해시 메서드 : 책의 제목과 저자를 기반으로 해시값 생성
        '''
        return hash((self.title, self.author))

    def __eq__(self, other):
        '''
        동등성 비교 메서드 : 두 Book 객체가 동등한지 비교
        '''
        # other가 Book인지 확인
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author


book1 = Book('python', '홍길동', 200)
book2 = Book('python', '홍길동', 300)
book3 = Book('python3', '홍길동', 300)
print(book1)
print([book1, book2])
print(len(book1))
print(len(book2))
print(book1[10])
print(book1 == book2) # eq만 있어도 작동
print(hash(book1) == hash(book2))
print(set([book1, book2, book3])) # hash와 eq 모두 정의되어야 set 가능 (중복을 허용 안한다는 개념에서)

# %%

# 도형 클래스
class Shape:
    count = 0

    def __init__(self, color, material):
        self.color = color
        self.material = material
        Shape.count += 1

    def describe(self):
        return f'이 도형은 {self.color}이고 재질은 {self.material}입니다.'


# 2차원 도형
class TwoDShape(Shape):
    count = 0

    def __init__(self, color, material):
        super().__init__(color, material)
        TwoDShape.count += 1

    # 추상 메서드 : 구현을 하지 않고 메서드의 이름과 파라미터만 미리 정의한 메서드
    def area(self):
        # 면적
        pass

    def perimeter(self):
        # 둘레
        pass


# 3차원 도형
class ThreeDShape(Shape):
    count = 0

    def __init__(self, color, material):
        super().__init__(color, material)
        ThreeDShape.count += 1

    def volume(self):
        pass

    def surface_area(self):
        # 겉넓이
        pass

    @staticmethod
    def calculate_density(mass, volume):
        return mass / volume
    

class Rectangle(TwoDShape):
    count = 0

    def __init__(self, color, material, width, height):
        super().__init__(color, material)
        self.width = width
        self.height = height
        Rectangle.count += 1

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2*(self.width + self.height)
    
    def describe(self):
        return f'{super().describe()} 가로는 {self.width}, 세로는 {self.height}인 사각형입니다.'


class Circle(TwoDShape):
    count = 0
    PI = 3.141592

    def __init__(self, color, material, radius):
        super().__init__(color, material)
        self.radius = radius
        Circle.count += 1

    def area(self):
        return Circle.PI * self.radius**2
    
    def perimeter(self):
        return 2 * Circle.PI * self.radius
    
    def describe(self):
        return f'{super().describe()} 반지름이 {self.radius}인 원입니다.'
    
    @classmethod
    def create_default(cls):
        # default 원 객체 생성 (객체가 없어도 쓸 수 있는 메서드)
        return cls('흰색', '종이', 1)
    

def print_shape_info(shape: Shape):
    print(shape.describe())
    if isinstance(shape, TwoDShape):
        print(f'둘레 : {shape.perimeter():.2f}')
        print(f'면적 : {shape.area():.2f}')


# 도형 객체 생성
shapes = [
    Rectangle('빨간색','철', 3, 4),
    Rectangle('노란색','골판지', 2, 5),
    Circle('빨간색','나무', 5),
    Circle.create_default()
]

for shape in shapes:
    print_shape_info(shape)
    print()

# 도형의 개수
print(f'총 도형의 개수 : {Shape.count}')
print(f'2D 도형의 개수 : {TwoDShape.count}')
print(f'사각형 도형의 개수 : {Rectangle.count}')
print(f'원 도형의 개수 : {Circle.count}')

# %%

# 직육면체 클래스
class Cuboid(ThreeDShape):
    count = 0

    def __init__(self, color, material, width, depth, height):
        super().__init__(color, material)
        self.width = width
        self.depth = depth
        self.height = height
        Cuboid.count += 1

    def volume(self):
        return self.width * self.depth * self.height
    
    def surface_area(self):
        return 2 * ((self.width * self.depth) + \
                    (self.depth * self.height) + \
                    (self.height * self.width))
    
    def describe(self):
        return f'{super().describe()} 가로가 {self.width}, 세로가 {self.depth}, 높이가 {self.height}인 직육면체입니다.'
    

# 구 클래스
class Sphere(ThreeDShape):
    count = 0
    PI = 3.141592

    def __init__(self, color, material, radius):
        super().__init__(color, material)
        self.radius = radius
        Sphere.count += 1

    def volume(self):
        return 4/3 * Sphere.PI * self.radius**3
    
    def surface_area(self):
        return 4 * Sphere.PI * self.radius
    
    def describe(self):
        return f'{super().describe()} 반지름이 {self.radius}인 구입니다.'
    
    @classmethod
    def create_default(cls):
        return cls('흰색', '종이', 1)


def print_shape_info(shape: Shape):
    print(shape.describe())
    if isinstance(shape, ThreeDShape):
        print(f'부피 : {shape.volume():.2f}')
        print(f'겉넓이 : {shape.surface_area():.2f}')


shapes_3D = [
    Cuboid('빨간색','철', 3, 4, 5),
    Cuboid('노란색','골판지', 2, 5, 10),
    Sphere('빨간색','나무', 5),
    Sphere.create_default()
]

for shape in shapes_3D:
    print_shape_info(shape)
    print()

# 도형의 개수
print(f'총 도형의 개수 : {Shape.count}')
print(f'2D 도형의 개수 : {TwoDShape.count}')
print(f'3D 도형의 개수 : {ThreeDShape.count}')
print(f'사각형 도형의 개수 : {Rectangle.count}')
print(f'원 도형의 개수 : {Circle.count}')
print(f'직육면체 도형의 개수 : {Cuboid.count}')
print(f'구 도형의 개수 : {Sphere.count}')

# %%

#%%

# 강사님이 추가적으로 알려주신 부분
class ShapeMeta(type):
    def __new__(mcls, name, bases, class_dict):
        # 코드 실행시 바로 실행됨 (객체 생성과 관련 없음)
        # 새로운 클래스를 생성합니다.
        # 생성된 클래스에 count 속성을 추가하고 0으로 초기화합니다.
        # 이를 통해 모든 Shape 하위 클래스는 자동으로 count 클래스 변수를 가지게 됩니다.
        cls = super().__new__(mcls, name, bases, class_dict)
        cls.count = 0
        return cls

    def __call__(cls, *args, **kwargs):
        # 클래스로부터 새로운 인스턴스가 생성될 때마다 호출됩니다.
        # 인스턴스를 생성한 후, 해당 클래스의 count를 1 증가시킵니다.
        # 이를 통해 각 Shape 하위 클래스의 인스턴스 개수를 자동으로 추적할 수 있습니다.
        instance = super().__call__(*args, **kwargs)
        cls.count += 1
        return instance
    

class Shape(metaclass=ShapeMeta):
    def __init__(self, color, material):
        self._color = color
        self._material = material
        Shape.count += 1

    # @property 데코레이터는 메서드를 속성처럼 사용할 수 있게 해줍니다.
    # 이를 통해 getter 메서드를 정의할 수 있습니다.
    @property
    def color(self):
        return self._color 

    # @color.setter 데코레이터는 color 속성에 대한 setter 메서드를 정의합니다.
    # 이를 통해 속성 값을 설정할 때 추가적인 로직(예: 유효성 검사)을 수행할 수 있습니다.
    @color.setter
    def color(self, value):
        if not value:
            raise ValueError("색상은 비어 있을 수 없습니다.")
        self._color = value

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        if not value:
            raise ValueError("재질은 비어 있을 수 없습니다.")
        self._material = value

    def describe(self):
        return f"이 도형은 {self.color}색이고 재질은 {self.material}입니다."


class TwoDShape(Shape):
    def __init__(self, color, material):
        super().__init__(color, material)
        TwoDShape.count += 1

    def area(self):
        pass

    def perimeter(self):
        pass


class ThreeDShape(Shape):
    def __init__(self, color, material):
        super().__init__(color, material)
        ThreeDShape.count += 1

    def volume(self):
        pass

    def surface_area(self):
        pass

    @staticmethod
    def calculate_density(mass, volume):
        return mass / volume


class Rectangle(TwoDShape):
    def __init__(self, color, material, width, height):
        super().__init__(color, material)
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("너비는 0보다 커야 합니다.")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("높이는 0보다 커야 합니다.")
        self._height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def describe(self):
        return f"{super().describe()} 너비는 {self.width}, 높이는 {self.height}인 직사각형입니다."


class Circle(TwoDShape):
    PI = 3.141592

    def __init__(self, color, material, radius):
        super().__init__(color, material)
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("반지름은 0보다 커야 합니다.")
        self._radius = value

    def area(self):
        return Circle.PI * self.radius ** 2

    def perimeter(self):
        return 2 * Circle.PI * self.radius

    def describe(self):
        return f"{super().describe()} 반지름 {self.radius}인 원입니다."

    @classmethod
    def create_default(cls):
        return cls("흰색", "종이", 1)


class Cuboid(ThreeDShape):
    def __init__(self, color, material, width, height, depth):
        super().__init__(color, material)
        self.width = width
        self.height = height
        self.depth = depth

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("너비는 0보다 커야 합니다.")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("높이는 0보다 커야 합니다.")
        self._height = value

    @property
    def depth(self):
        return self._depth

    @depth.setter
    def depth(self, value):
        if value <= 0:
            raise ValueError("깊이는 0보다 커야 합니다.")
        self._depth = value

    def volume(self):
        return self.width * self.height * self.depth

    def surface_area(self):
        return 2 * (self.width * self.height + self.width * self.depth + self.height * self.depth)

    def describe(self):
        return f"{super().describe()}, 너비 {self.width}, 높이 {self.height}, 깊이 {self.depth}인 직육면체입니다."


class Sphere(ThreeDShape):
    def __init__(self, color, material, radius):
        super().__init__(color, material)
        self.radius = radius

    @property
    def radius(self):
        return self._radius*10

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("반지름은 0보다 커야 합니다.")
        self._radius = value

    def volume(self):
        return (4 / 3) * Circle.PI * self.radius ** 3

    def surface_area(self):
        return 4 * Circle.PI * self.radius ** 2

    def describe(self):
        return f"{super().describe()}, 반지름이 {self.radius}인 구입니다."


def print_shape_info(shape: Shape) :
    print(shape.describe())
    if isinstance(shape, TwoDShape) :
        print(f"둘레 : {shape.perimeter():.2f}")
        print(f"면적 : {shape.area():.2f}")
    elif isinstance(shape, ThreeDShape) :
        print(f"겉면적 : {shape.surface_area():.2f}")
        print(f"부피 : {shape.volume():.2f}")
        print(f"밀도(1kg 경우) : {ThreeDShape.calculate_density(1, shape.volume()):.2f}")

# 도형 객체 생성
shapes = [
    Rectangle("파란색", "철", 3, 4),
    Rectangle("노란색", "골판지", 2, 5),
    Circle("빨간색", "나무", 5),
    Circle.create_default(),
    Cuboid("주황색", "종이", 3,5,4),
    Sphere("하안색", "고무", 5)
]

for shape in shapes :
    print_shape_info(shape)
    print()

# 도형의 개수
print(f"총 도형의 개수: {Shape.count}")
print(f"2D 도형의 개수: {TwoDShape.count}")
print(f"3D 도형의 개수: {ThreeDShape.count}")
print(f"사각형의 개수: {Rectangle.count}")
print(f"원의 개수: {Circle.count}")
print(f"직육면체의 개수: {Cuboid.count}")
print(f"구의 개수: {Sphere.count}")

#%%

shapes[-1].radius = 9
print(shapes[-1].radius)
shapes[-1].radius = -10
