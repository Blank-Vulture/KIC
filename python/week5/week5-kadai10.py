# test_admin.py
from user_module import Admin

# Admin のインスタンスを作成
admin_user = Admin("V", "Merc", "不明", 30)

# メソッドの呼び出し
admin_user.describe_user()
admin_user.privileges.show_privileges()
