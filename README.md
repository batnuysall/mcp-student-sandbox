# mystery_module

Kısa açıklama
-------------
`mystery_module` basit bir kuadratik denklemi çözen yardımcı fonksiyon içerir.

Matematiksel özet
-----------------
Diskriminant:
$$d = b^2 - 4ac$$

Kökler (diskriminant ≥ 0 için):
$$x = \frac{-b \pm \sqrt{d}}{2a}$$

Installation
------------
1. Python 3.8+ kullanın.
2. Dosyayı proje dizinine kopyalayın:
```bash
cp path/to/mystery_module.py ./your_project/
```
3. (Opsiyonel) sanal ortam:
```bash
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
.venv\Scripts\activate     # Windows
```

Usage
-----
Basit kullanım:
```python
from mystery_module import fn_x

# Gerçek kökler
print(fn_x(1, -3, 2))   # örn. (2.0, 1.0) — (sıralama uygulanmamış olabilir)

# Negatif diskriminant (mevcut implementasyonda None döner)
print(fn_x(1, 0, 1))    # None  (mevcut davranış)
```

Functions
---------
fn_x(a, b, c)
- Açıklama: $ax^2 + bx + c = 0$ denkleminin köklerini hesaplamaya çalışır.
- Parametreler:
  - `a`, `b`, `c` — sayısal katsayılar.
- Dönen değer:
  - Eğer diskriminant negatifse: `None` (mevcut kod).
  - Aksi halde iki elemanlı tuple: iki kök (ör. `(x1, x2)`).
- Kenar durumlar / uyarılar:
  - `a == 0` için mevcut implementasyon ZeroDivisionError üretir — lineer denklem olarak ele alınmalı.
  - `math` modülü import edilmemiş; bu durum NameError ile sonuçlanır.
  - Negatif diskriminant için daha faydalı davranış: kompleks kök döndürmek (`cmath.sqrt`) veya açık bir hata fırlatmak.

Hızlı düzeltme önerisi
----------------------
Aşağıdaki kısa örnek daha sağlam bir davranış sağlar (lineer durum ve kompleks kökleri destekler):
```python
# filepath: mystery_module.py
# ...existing code...
import cmath
from typing import Optional, Tuple, Union

def fn_x(a: float, b: float, c: float) -> Optional[Tuple[complex, complex]]:
    if a == 0:
        if b == 0:
            return None
        root = -c / b
        return (root, root)
    d = b**2 - 4*a*c
    sqrt_d = cmath.sqrt(d)
    return ((-b + sqrt_d) / (2*a), (-b - sqrt_d) / (2*a))
# ...existing code...
```

Katkılar ve lisans
------------------
PR, issue ve birim testlere açığız. Projeye uygun lisans ekleyin.