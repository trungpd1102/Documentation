#lấy đường dẫn tuyệt đối của file Python hiện tại
#Vì khi chạy chương trình sẽ không hiểu được đường dẫn tương đối mà chỉ hiểu được đường dẫn tuyệt đối

import os
current_directory = os.path.dirname(os.path.abspath(file))
