# FastAPI

by Thắng Đặng

***

## Khái niệm ( ăn cắp từ doc )

logo khá đẹp, và bắt mắt =)))

![A brief introduction to FastAPI. A fast python framework to build APIs | by  Pedro Alvarado | Mar, 2022 | Dev Genius](https://miro.medium.com/max/1200/1*ChiWVYhwSZO3lzKEduFgrA.png)

​	Là 1 web framework dùng để xây dưng API với hiệu suất và hiệu năng cao, hỗ trợ tốt trong việc làm ứng dụng.

Theo như quảng cáo của nhà phát triển FastAPI doc thì nó các tính năng như sau:

- **Fast**: Hiệu năng cao, được so sánh là ngang với NodeJS và Go
- **Fast to code** : Code nhanh hơn, tăng tốc độ xử lý của các tính năng lên khoảng 200% tới 300%
- **Fewer bugs** : Số bug của các developer được giảm lên đến 40%
- **Intuitive** : Hỗ trợ viết code. Tự động gợi ý code. Ít thời gian debug hơn
- **Easy** : Thiết kế để dễ dàng sử dụng và học. Ít thời gian đọc docs hơn
- **Short** : Giảm thiểu trùng lặp code. Được thiết kế với nhiều tính năng từ mỗi tham số truyền vào. Ít bug hơn
- **Robust** : Có khả năng tương tác với API qua docs
- **Standards-based** : Dựa trên các tiêu chuẩn mở cho API như là OpenAPI và JSON Schema.

***

## Giờ đến phần cài đặt

Yêu cầu: 
	- Python từ 3.6 trở lên
	- [Starlette](https://www.starlette.io/) framework dành cho phần web
	- [pydantic (helpmanual.io)](https://pydantic-docs.helpmanual.io/) framework dành cho phần data

Cài đặt :
	Window sử dụng câu lệnh tại cửa sổ CMD/terminal

```
pip install fastapi
```

​	Tiếp theo chúng ta cần cài đặt server ASGI, cho việc thiết kế sản phẩm

```
pip install "uvicorn[standard]"
```

***

Còn tiếp (hướng dẫn sử dụng và một số thao tács)
