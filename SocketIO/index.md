1. Socket + Vuejs: Sau khi listen 1 event ở ```created()``` hoặc ```mounted()``` thì cần phai remove listener đó khi ```unmounted```
- Sử dụng callback(listener) là 1 hàm khai báo từ bên ngoài chứ không sử dụng hàm khai báo trực tiếp vì sẽ không thể remove
