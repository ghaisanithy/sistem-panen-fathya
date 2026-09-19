{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNX1GbVyy2s7ibRB5bQbSov",
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
        "<a href=\"https://colab.research.google.com/github/ghaisanithy/sistem-panen-fathya/blob/conflict-olivia/kalkulasi_harga.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def tampilkan_laporan(daftar_panen):\n",
        "    \"\"\"\n",
        "    Fungsi untuk mengolah statistik dan menampilkan rekapitulasi data panen.\n",
        "    Menerima input berupa list of dictionary dari modul input_panen.\n",
        "    \"\"\"\n",
        "    if not daftar_panen:\n",
        "        print(\"\\n[PERINGATAN] Tidak ada data panen yang bisa dilaporkan.\")\n",
        "        return\n",
        "\n",
        "    # 1. Perhitungan Statistik\n",
        "    total_berat = sum(item[\"berat_kg\"] for item in daftar_panen)\n",
        "    rata_rata = total_berat / len(daftar_panen)\n",
        "    komoditas_terbanyak = max(daftar_panen, key=lambda x: x[\"berat_kg\"])\n",
        "\n",
        "    # Menghitung jumlah per kualitas\n",
        "    jumlah_kualitas_a = sum(1 for item in daftar_panen if item[\"kualitas\"] == \"A\")\n",
        "    jumlah_kualitas_b = sum(1 for item in daftar_panen if item[\"kualitas\"] == \"B\")\n",
        "    jumlah_kualitas_c = sum(1 for item in daftar_panen if item[\"kualitas\"] == \"C\")\n",
        "\n",
        "    # 2. Format Tabel Laporan\n",
        "    print(\"\\n\" + \"=\" * 54)\n",
        "    print(f\"{'REKAPITULASI HASIL PANEN':^54}\")\n",
        "    print(\"=\" * 54)\n",
        "    print(f\"{'No':<4} | {'Komoditas':<18} | {'Berat (kg)':<12} | {'Kualitas':<8}\")\n",
        "    print(\"-\" * 54)\n",
        "\n",
        "    for idx, item in enumerate(daftar_panen, start=1):\n",
        "        print(f\"{idx:<4} | {item['komoditas']:<18} | {item['berat_kg']:<12.1f} | {item['kualitas']:<8}\")\n",
        "\n",
        "    print(\"-\" * 54)\n",
        "    print(\"RINGKASAN STATISTIK:\")\n",
        "    print(f\" • Total Berat Panen    : {total_berat:.1f} kg\")\n",
        "    print(f\" • Rata-rata per Jenis  : {rata_rata:.1f} kg\")\n",
        "    print(f\" • Komoditas Tertinggi  : {komoditas_terbanyak['komoditas']} ({komoditas_terbanyak['berat_kg']:.1f} kg)\")\n",
        "    print(f\" • Distribusi Kualitas  : A={jumlah_kualitas_a}, B={jumlah_kualitas_b}, C={jumlah_kualitas_c}\")\n",
        "    print(\"=\" * 54 + \"\\n\")\n",
        "\n",
        "\n",
        "# BAGIAN INI UNTUK TESTING MANDIRI DI GOOGLE COLAB OLEH ANGGOTA B:\n",
        "if __name__ == \"__main__\":\n",
        "    # Menggunakan sampel data yang sama persis seperti hasil running Anggota A\n",
        "    data_testing_dari_a = [\n",
        "        {'komoditas': 'Kentang', 'berat_kg': 100.0, 'kualitas': 'A'},\n",
        "        {'komoditas': 'Sorgum', 'berat_kg': 80.0, 'kualitas': 'A'}\n",
        "    ]\n",
        "\n",
        "    print(\"Menjalankan modul laporan dengan data uji coba...\")\n",
        "    tampilkan_laporan(data_testing_dari_a)"
      ],
      "metadata": {
        "id": "QY70_Db4agCF",
        "outputId": "4d9e0033-f2ff-4bcf-b438-641a0eb56077",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Menjalankan modul laporan dengan data uji coba...\n",
            "\n",
            "======================================================\n",
            "               REKAPITULASI HASIL PANEN               \n",
            "======================================================\n",
            "No   | Komoditas          | Berat (kg)   | Kualitas\n",
            "------------------------------------------------------\n",
            "1    | Kentang            | 100.0        | A       \n",
            "2    | Sorgum             | 80.0         | A       \n",
            "------------------------------------------------------\n",
            "RINGKASAN STATISTIK:\n",
            " • Total Berat Panen    : 180.0 kg\n",
            " • Rata-rata per Jenis  : 90.0 kg\n",
            " • Komoditas Tertinggi  : Kentang (100.0 kg)\n",
            " • Distribusi Kualitas  : A=2, B=0, C=0\n",
            "======================================================\n",
            "\n"
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
        "    # Penentuan harga satuan per kg oleh Anggota B\n",
        "    daftar_harga = {\n",
        "        \"Kentang\": 15000,\n",
        "        \"Sorgum\": 11500\n",
        "    }\n",
        "\n",
        "    harga_satuan = daftar_harga.get(komoditas, 0)\n",
        "    total = berat_kg * harga_satuan\n",
        "    return total\n",
        "\n",
        "print(\"Modul hitung pendapatan aktif (Versi Pasar Ekspor)\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lfVRawOKXo-p",
        "outputId": "1d1d7c60-4e21-4f65-f107-b1d315364238"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Modul hitung pendapatan aktif (Versi Pasar Ekspor)\n"
          ]
        }
      ]
    }
  ]
}