from haystack import indexes
from books.models import Books


# 指定对于某个类的某些数据建立索引, 一般类名:模型类名+Index
class BooksIndex(indexes.SearchIndex, indexes.Indexable):
    # 指定根据表中的哪些字段建立索引:比如:商品名字 商品描述
    text = indexes.CharField(document=True, use_template=True)  #

    # author = indexes.CharField(model_attr='user')  # 创建一个author字段
    # pub_date = indexes.DateTimeField(model_attr='pub_date')  # 创建一个pub_date字段

    def get_model(self): # 重载get_model方法，必须要有！
        return Books

    def index_queryset(self, using=None): # 重载index_..函数
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()