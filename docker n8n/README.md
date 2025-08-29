# N8N Docker Setup

Hướng dẫn build và chạy N8N container sử dụng Docker.

## Yêu cầu

- Docker Desktop đã được cài đặt
- Docker Compose

## Cấu trúc thư mục

```
docker n8n/
├── Dockerfile
├── docker-compose.yml
├── docker-custom-entrypoint.sh
└── README.md
```

## Cách sử dụng

### 1. Build và chạy container

```bash
# Di chuyển vào thư mục docker n8n
cd "c:\Users\Admin\dsqt99\code\n8n\docker n8n"

# Build và chạy container
docker-compose up --build -d
```

### 2. Chỉ chạy container (không build lại)

```bash
# Chạy container đã build
docker-compose up -d
```

### 3. Dừng container

```bash
# Dừng container
docker-compose down
```

### 4. Xem logs

```bash
# Xem logs của container n8n
docker-compose logs -f n8n

# Xem logs của tất cả services
docker-compose logs -f
```

### 5. Rebuild container

```bash
# Dừng và xóa container cũ, sau đó build lại
docker-compose down
docker-compose up --build -d
```

## Truy cập N8N

Sau khi container chạy thành công, bạn có thể truy cập N8N tại:

- **Local**: http://localhost:5678
- **Ngrok URL**: https://funny-rattler-thankfully.ngrok-free.app

## Cấu hình môi trường

Các biến môi trường được cấu hình trong `docker-compose.yml`:

- `N8N_HOST`: Domain cho N8N
- `N8N_PORT`: Port của N8N (5678)
- `N8N_PROTOCOL`: Giao thức (https)
- `GENERIC_TIMEZONE`: Múi giờ (Asia/Ho_Chi_Minh)
- `NGROK_AUTHTOKEN`: Token xác thực Ngrok

## Dữ liệu lưu trữ

Dữ liệu N8N được lưu trong thư mục `./data` và được mount vào container tại `/home/node/.n8n`.

## Troubleshooting

### Container không khởi động được

```bash
# Kiểm tra logs để xem lỗi
docker-compose logs n8n

# Kiểm tra trạng thái container
docker-compose ps
```

### Port đã được sử dụng

```bash
# Kiểm tra process đang sử dụng port 5678
netstat -ano | findstr :5678

# Hoặc thay đổi port trong docker-compose.yml
```

### Rebuild hoàn toàn

```bash
# Xóa tất cả container, image và volume
docker-compose down -v
docker system prune -a
docker-compose up --build -d
```

## Lưu ý

- Đảm bảo Docker Desktop đang chạy trước khi thực hiện các lệnh
- Ngrok token cần được cấu hình đúng để truy cập từ bên ngoài
- Dữ liệu sẽ được lưu trữ persistent trong thư mục `./data`