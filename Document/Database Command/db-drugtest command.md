# Cơ sở dữ liệu db.drugtest

by Thắng Đặng

***

## Tạo csdl
```sql
CREATE DATABASE "dbo.drugtest"
    WITH 
    OWNER = postgres
    TEMPLATE = postgres
    ENCODING = 'UTF8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

COMMENT ON DATABASE "dbo.drugtest"
    IS 'Cơ sở dữ liệu thử nghiệm thuốc
';
```

***

## Tạo table

**Bảng tbl_drug** - Lưu trữ dữ liệu  thuốc

```sql
-- Table: public.tbl_drug

-- DROP TABLE IF EXISTS public.tbl_drug;

CREATE TABLE IF NOT EXISTS public.tbl_drug
(
    id_drug integer NOT NULL,
    drug_code integer NOT NULL,
    drug_name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    drug_type character varying(1000) COLLATE pg_catalog."default" NOT NULL,
    drug_quatity integer,
    drug_price integer,
    drug_date date,
    drug_expire date,
    drug_status character varying(500) COLLATE pg_catalog."default",
    CONSTRAINT tbl_drug_pkey PRIMARY KEY (id_drug)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.tbl_drug
    OWNER to postgres;

COMMENT ON TABLE public.tbl_drug
    IS 'Bảng dữ liệu về thuốc';
```


**Bảng tbl_guest** - Lưu trữ dữ liệu  khách hàng 

```sql
-- Table: public.tbl_guest

-- DROP TABLE IF EXISTS public.tbl_guest;

CREATE TABLE IF NOT EXISTS public.tbl_guest
(
    id_guest integer NOT NULL,
    guest_name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    guest_age date,
    guest_sex integer NOT NULL,
    guest_address character varying(500) COLLATE pg_catalog."default",
    guest_email character varying(255) COLLATE pg_catalog."default" NOT NULL,
    guest_phone integer,
    type_of_disease character varying(255) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT tbl_guest_pkey PRIMARY KEY (id_guest)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.tbl_guest
    OWNER to postgres;

COMMENT ON TABLE public.tbl_guest
    IS 'Bảng dữ liệu bệnh nhân/khách hàng';
```

**Bảng tbl_staff** - Lưu trữ dữ liệu của nhân viên

```sql
-- Table: public.tbl_staff

-- DROP TABLE IF EXISTS public.tbl_staff;

CREATE TABLE IF NOT EXISTS public.tbl_staff
(
    id_staff integer NOT NULL,
    staff_name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    staff_dob date,
    staff_sex integer NOT NULL,
    staff_address character varying(500) COLLATE pg_catalog."default",
    staff_email character varying(255) COLLATE pg_catalog."default" NOT NULL,
    staff_phone integer,
    CONSTRAINT tbl_staff_pkey PRIMARY KEY (id_staff)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.tbl_staff
    OWNER to postgres;

COMMENT ON TABLE public.tbl_staff
    IS 'Bảng dữ liệu nhân viên';
```


**Bảng tbl_drugstore** - Dữ liệu cửa hàng bán thuốc

```sql
-- Table: public.tbl_drugstore

-- DROP TABLE IF EXISTS public.tbl_drugstore;

CREATE TABLE IF NOT EXISTS public.tbl_drugstore
(
    id_store integer NOT NULL,
    store_address character varying(1000) COLLATE pg_catalog."default" NOT NULL,
    store_phone integer NOT NULL,
    id_guest integer,
    id_staff integer,
    CONSTRAINT "Ten cua hang" PRIMARY KEY (id_store),
    CONSTRAINT "tbl_guest to tbl_drugstore" FOREIGN KEY (id_guest)
        REFERENCES public.tbl_guest (id_guest) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT "tbl_staff to tbl_drugstore" FOREIGN KEY (id_staff)
        REFERENCES public.tbl_staff (id_staff) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.tbl_drugstore
    OWNER to postgres;

COMMENT ON TABLE public.tbl_drugstore
    IS 'Bảng dữ liệu về cửa hàng bán thuốc';

COMMENT ON CONSTRAINT "tbl_guest to tbl_drugstore" ON public.tbl_drugstore
    IS 'connect table guest va drugstore';
COMMENT ON CONSTRAINT "tbl_staff to tbl_drugstore" ON public.tbl_drugstore
    IS 'connect table staff to table drugstore';
```

**Bảng tbl_guestcart** - Lưu trữ dữ liệu giỏ hàng của khách 

```sql
-- Table: public.tbl_guestcart

-- DROP TABLE IF EXISTS public.tbl_guestcart;

CREATE TABLE IF NOT EXISTS public.tbl_guestcart
(
    id_guestcart integer NOT NULL,
    id_drug integer,
    id_guest integer,
    quatity integer,
    CONSTRAINT tbl_guestcart_pkey PRIMARY KEY (id_guestcart),
    CONSTRAINT "table drug to table guestcart" FOREIGN KEY (id_drug)
        REFERENCES public.tbl_drug (id_drug) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT "table guest to table guestcart" FOREIGN KEY (id_guest)
        REFERENCES public.tbl_guest (id_guest) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.tbl_guestcart
    OWNER to postgres;

COMMENT ON TABLE public.tbl_guestcart
    IS 'Bảng giỏ hàng của khách';
```

**Bảng tbl_storestorage** - Lưu trữ dữ liệu kho chứa thuốc của mỗi cửa hàng

```sql
-- Table: public.tbl_storestorage

-- DROP TABLE IF EXISTS public.tbl_storestorage;

CREATE TABLE IF NOT EXISTS public.tbl_storestorage
(
    id_storage integer NOT NULL,
    id_store integer,
    id_drug integer,
    quatity integer,
    CONSTRAINT tbl_storestorage_pkey PRIMARY KEY (id_storage),
    CONSTRAINT "table drug to table storestorage" FOREIGN KEY (id_drug)
        REFERENCES public.tbl_drug (id_drug) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT "table store to table storestorage" FOREIGN KEY (id_store)
        REFERENCES public.tbl_drugstore (id_store) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.tbl_storestorage
    OWNER to postgres;

COMMENT ON TABLE public.tbl_storestorage
    IS 'bảng dữ liệu kho chứa thuốc (global)';
```

***

