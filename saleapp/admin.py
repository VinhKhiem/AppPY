from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from saleapp.models import Category, Product
from saleapp import app, db

admin = Admin(app=app, name='QUẢN TRỊ BÁN HÀNG', template_mode='bootstrap4')


class MyProductView(ModelView):
    column_list = ['id', 'name', 'price']
    can_export = True
    column_searchable_list = ['name']
    column_filters = ['name', 'price']
    column_editable_list = ['name', 'price']
    edit_modal = True


class MyCategoryView(ModelView):
    column_list = ['name', 'products']


class MyStatsView(BaseView):
    @expose("/")
    def index(self):
        return self.render('admin/stats.html')


admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))
admin.add_view(MyStatsView(name='Thống kê báo cáo'))
