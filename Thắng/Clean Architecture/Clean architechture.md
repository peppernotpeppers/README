## 																				Clean architechture

## Định nghĩa của "kiến trúc " là gì?

​	Vào thế kỷ thứ nhất trong cuốn sách kiến trúc, một kiến trúc sư thời La Mã có nói về 3 điều trong kiến trúc. Đó là:

		- Độ bền
		- Tiện ích
		- Vẻ đẹp

## Đối với "kiến trúc phần mềm" hiện nay

​	Định nghĩa của một "kiến trúc" máy tính được gọi là nghệ thuật và khoa học trong đó các thành phần của hệ thống máy tính được tổ chức và tích hợp.

Câu hỏi: 'Liệu phần mềm có cần kiến trúc không ?'

## Định nghĩa của "clean"

​	![5 bước sắp xếp dây điện gọn gàng cho bàn làm việc](https://vnreview.vn/image/16/59/04/1659041.jpg?t=1495169346286)

- rất khó để nhận biết dây nào là dây loa, dây chuột,........ bla bla
- khó khăn trong việc vệ sinh
- không có nhiều không gian
- .....

![5 thói quen nhỏ giúp mình có được một cuộc sống gọn gàng và ngăn nắp – KIRA](https://thehanoichamomile.files.wordpress.com/2019/11/2019-11-29-09.09.41-1.jpg)

- sẽ biết được đâu là dây nào
- dễ dàng vệ sinh, bảo trì
- ....

Câu hỏi: vậy đối với "clean" ở trong lập trình?

## Vậy "clean architecture" là gì?

​	![P2: Clean Architecture trong Android và ví dụ - Trang Chủ](https://itzone.com.vn/wp-content/uploads/2020/05/77cac2d9-56ee-4ed2-a55c-3a24a2ad83e3.png)

​	"Clean architecture" là "kiến trúc lớp" nó là một cách để tạo ra hệ thống dựa trên các layer (lớp)

Nếu bạn tạo ra "một thứ gì đó" ở trong hệ thống, bạn sẽ không được tự do đặt nó ở bất cứ đâu bạn muốn. Có 4 lớp layer sẽ được đề cập đến

- Entities : nơi chứa các Business Logic - nơi chứa các logic thực hiện giải quyết vấn đề (không chứa bất cứ framework nào)
- Use Cases : chứa các rule liên quan trực tiếp tới ứng dụng cục bộ (business rule)
- Interface Adapter : tập hợp các adapter phục vụ quá trình tương tác với các công nghệ.
- Framework : chứa các công cụ về cơ sở dữ liệu và các framework.