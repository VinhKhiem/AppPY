from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from saleapp import db, app


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image =Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Table')
        #
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()
        # db.create_all()

        p1 = Product(name='iPhone 13', price=20000000, category_id=1,
                     image='https://genk.mediacdn.vn/139269124445442048/2023/1/28/photo-1-16748754960461027851510-1674879790185-16748797903831625207516.jpeg')
        p2 = Product(name='Galaxy SX', price=21000000, category_id=1,
                     image='https://genk.mediacdn.vn/139269124445442048/2023/1/28/photo-1-16748754960461027851510-1674879790185-16748797903831625207516.jpeg')
        p3 = Product(name='Oppo', price=22000000, category_id=1,
                     image='https://genk.mediacdn.vn/139269124445442048/2023/1/28/photo-1-16748754960461027851510-1674879790185-16748797903831625207516.jpeg')
        p4 = Product(name='Redmi', price=23000000, category_id=1,
                     image='https://genk.mediacdn.vn/139269124445442048/2023/1/28/photo-1-16748754960461027851510-1674879790185-16748797903831625207516.jpeg')
        p5 = Product(name='Apple', price=24000000, category_id=1,
                     image='https://genk.mediacdn.vn/139269124445442048/2023/1/28/photo-1-16748754960461027851510-1674879790185-16748797903831625207516.jpeg')

        db.session.add_all(p1, p2, p3, p4, p5)
        db.session.commit()