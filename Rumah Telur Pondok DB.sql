CREATE TABLE "admin" (
  "id_admin" integer UNIQUE PRIMARY KEY,
  "nama_admin" varchar(100) NOT NULL,
  "password_admin" varchar(50) NOT NULL
);

CREATE TABLE "produk" (
  "id_produk" integer UNIQUE PRIMARY KEY,
  "nama_produk" varchar(50) NOT NULL,
  "satuan" varchar(10) NOT NULL,
  "harga_satuan" integer NOT NULL,
  "stok_tersedia" integer
);

CREATE TABLE "pembeli" (
  "id_pembeli" integer UNIQUE PRIMARY KEY,
  "nama_pembeli" varchar(255) NOT NULL
);

CREATE TABLE "penjualan" (
  "id_penjualan" integer UNIQUE PRIMARY KEY,
  "id_pembeli" integer,
  "id_produk" integer,
  "total_harga" integer NOT NULL,
  "tanggal_penjualan" datetime NOT NULL,
  "jam_penjualan" timestamp NOT NULL
);

CREATE TABLE "item_penjualan" (
  "id" integer UNIQUE PRIMARY KEY,
  "id_penjualan" integer NOT NULL,
  "id_produk" integer NOT NULL,
  "jumlah" integer NOT NULL,
  "harga_satuan" integer NOT NULL,
  "subtotal" integer NOT NULL
);

CREATE TABLE "pengeluaran" (
  "id_pegeluaran" integer UNIQUE,
  "jenis_pengeluaran" varchar(25),
  "jumlah_pengeluaran" integer,
  "tanggal_pengeluaran" datetime,
  "jam_pengeluaran" timestamp,
  "foto_struk" image
);

ALTER TABLE "pembeli" ADD FOREIGN KEY ("id_pembeli") REFERENCES "penjualan" ("id_pembeli") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "produk" ADD FOREIGN KEY ("id_produk") REFERENCES "penjualan" ("id_produk") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "item_penjualan" ADD FOREIGN KEY ("id_penjualan") REFERENCES "penjualan" ("id_penjualan") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "item_penjualan" ADD FOREIGN KEY ("id_produk") REFERENCES "produk" ("id_produk") DEFERRABLE INITIALLY IMMEDIATE;
