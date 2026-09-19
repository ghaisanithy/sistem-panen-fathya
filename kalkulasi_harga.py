{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMhXWuewwxhN+IbKmMkYz6I",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ghaisanithy/sistem-panen-fathya/blob/conflict-ghea/kalkulasi_harga.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# input_panen.py\n",
        "# Dikerjakan oleh: Anggota A (Branch: fitur-input)\n",
        "\n",
        "def input_data_panen():\n",
        "    \"\"\"\n",
        "    Fungsi untuk memasukkan data hasil panen dengan validasi sederhana.\n",
        "    Mengembalikan list of dictionary data panen.\n",
        "    \"\"\"\n",
        "    daftar_panen = []\n",
        "    print(\"=== PENCATATAN DATA PANEN ===\")\n",
        "\n",
        "    while True:\n",
        "        try:\n",
        "            jumlah = int(input(\"Masukkan jumlah jenis komoditas yang ingin dicatat: \"))\n",
        "            if jumlah > 0:\n",
        "                break\n",
        "            print(\"Jumlah harus lebih besar dari 0.\")\n",
        "        except ValueError:\n",
        "            print(\"Input tidak valid! Masukkan angka bulat.\")\n",
        "\n",
        "    for i in range(jumlah):\n",
        "        print(f\"\\nData Komoditas ke-{i + 1}:\")\n",
        "\n",
        "        while True:\n",
        "            nama = input(\"  Nama Komoditas (misal: Jagung, Padi): \").strip()\n",
        "            if nama:\n",
        "                break\n",
        "            print(\"  Nama komoditas tidak boleh kosong!\")\n",
        "\n",
        "        while True:\n",
        "            try:\n",
        "                berat = float(input(\"  Berat Hasil Panen (kg): \"))\n",
        "                if berat > 0:\n",
        "                    break\n",
        "                print(\"  Berat harus lebih dari 0 kg.\")\n",
        "            except ValueError:\n",
        "                print(\"  Input harus berupa angka desimal/bulat!\")\n",
        "\n",
        "        while True:\n",
        "            try:\n",
        "                kualitas = input(\"  Kualitas Panen (A/B/C): \").strip().upper()\n",
        "                if kualitas in ['A', 'B', 'C']:\n",
        "                    break\n",
        "                print(\"  Pilihan kualitas hanya A, B, atau C!\")\n",
        "            except Exception:\n",
        "                print(\"  Input kualitas tidak valid.\")\n",
        "\n",
        "        # Simpan dalam struktur data dictionary\n",
        "        daftar_panen.append({\n",
        "            \"komoditas\": nama,\n",
        "            \"berat_kg\": berat,\n",
        "            \"kualitas\": kualitas\n",
        "        })\n",
        "\n",
        "    print(\"\\n[INFO] Data panen berhasil dicatat!\\n\")\n",
        "    return daftar_panen\n",
        "\n",
        "# TAMBAHKAN BAGIAN INI UNTUK TESTING DI COLAB:\n",
        "if __name__ == \"__main__\":\n",
        "    hasil_input = input_data_panen()\n",
        "    print(\"Data yang tersimpan di memori:\")\n",
        "    print(hasil_input)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0SsXXm4cYuVC",
        "outputId": "baaceb67-edc1-41d5-9651-ae17609c9c51"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "=== PENCATATAN DATA PANEN ===\n",
            "Masukkan jumlah jenis komoditas yang ingin dicatat: 2\n",
            "\n",
            "Data Komoditas ke-1:\n",
            "  Nama Komoditas (misal: Jagung, Padi): Kentang\n",
            "  Berat Hasil Panen (kg): 100\n",
            "  Kualitas Panen (A/B/C): A\n",
            "\n",
            "Data Komoditas ke-2:\n",
            "  Nama Komoditas (misal: Jagung, Padi): Sorgum\n",
            "  Berat Hasil Panen (kg): 80\n",
            "  Kualitas Panen (A/B/C): A\n",
            "\n",
            "[INFO] Data panen berhasil dicatat!\n",
            "\n",
            "Data yang tersimpan di memori:\n",
            "[{'komoditas': 'Kentang', 'berat_kg': 100.0, 'kualitas': 'A'}, {'komoditas': 'Sorgum', 'berat_kg': 80.0, 'kualitas': 'A'}]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# kalkulasi_harga.py\n",
        "\n",
        "def hitung_total_pendapatan(berat_kg, komoditas):\n",
        "    # Penentuan harga satuan per kg oleh Anggota A\n",
        "    daftar_harga = {\n",
        "        \"Kentang\": 12000,\n",
        "        \"Sorgum\": 9000\n",
        "    }\n",
        "\n",
        "    harga_satuan = daftar_harga.get(komoditas, 0)\n",
        "    total = berat_kg * harga_satuan\n",
        "    return total\n",
        "\n",
        "print(\"Modul hitung pendapatan aktif (Versi Pasar Lokal)\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_PlY6rEBXclN",
        "outputId": "d204e7c7-79f0-42e8-de0a-03493dfe28f5"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Modul hitung pendapatan aktif (Versi Pasar Lokal)\n"
          ]
        }
      ]
    }
  ]
}