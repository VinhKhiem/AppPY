from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from saleapp import db, app


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(255))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
        # db.create_all()

        # c1 = Category(name='Mobile')
        # c2 = Category(name='Table')
        #
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()

        p1 = Product(name='iPhone 13', price=20000000, category_id=1,
                     image='https://vcdn-sohoa.vnecdn.net/2020/05/25/iPhone-12-Blue-2785-1590377566.jpg')
        p2 = Product(name='Galaxy SX', price=21000000, category_id=2,
                     image='https://vcdn-sohoa.vnecdn.net/2020/05/25/iPhone-12-Blue-2785-1590377566.jpg')
        p3 = Product(name='Oppo', price=22000000, category_id=1,
                     image='https://vcdn-sohoa.vnecdn.net/2020/05/25/iPhone-12-Blue-2785-1590377566.jpg')
        p4 = Product(name='Redmi', price=23000000, category_id=2,
                     image='https://vcdn-sohoa.vnecdn.net/2020/05/25/iPhone-12-Blue-2785-1590377566.jpg')
        p5 = Product(name='Apple', price=24000000, category_id=1,
                     image='https://vcdn-sohoa.vnecdn.net/2020/05/25/iPhone-12-Blue-2785-1590377566.jpg')

        db.session.add_all([p1, p2, p3, p4, p5])
        db.session.commit()
