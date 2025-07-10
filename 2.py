# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.offsetbox import AnchoredText
# def f(x, y):
#     return x**2 - np.cos(x)
# def rkf45(f, x0, y0, x_end, h_init=0.1, tol=1e-5):
#     x_vals = [x0]
#     y_vals = [y0]
#     h, x, y = h_init, x0, y0
#     while x < x_end:
#         if x + h > x_end:
#             h = x_end - x
#         k1 = h * f(x, y)
#         k2 = h * f(x + h/4, y + k1/4)
#         k3 = h * f(x + 3*h/8, y + 3*k1/32 + 9*k2/32)
#         k4 = h * f(x + 12*h/13,
#                    y + 1932*k1/2197 - 7200*k2/2197 + 7296*k3/2197)
#         k5 = h * f(x + h,
#                    y + 439*k1/216 - 8*k2 + 3680*k3/513 - 845*k4/4104)
#         k6 = h * f(x + h/2,
#                    y - 8*k1/27 + 2*k2 - 3544*k3/2565 + 1859*k4/4104 - 11*k5/40)
#         y4 = y + 25*k1/216 + 1408*k3/2565 + 2197*k4/4104 - k5/5
#         y5 = y + 16*k1/135 + 6656*k3/12825 + 28561*k4/56430 - 9*k5/50 + 2*k6/55
#         error = abs(y5 - y4)
#         if error < tol:
#             x += h
#             y = y5
#             x_vals.append(x)
#             y_vals.append(y)
#         s = 2 if error == 0 else 0.84 * (tol * h / error)**0.25
#         h = min(h * s, 0.5)
#     return np.array(x_vals), np.array(y_vals)
# if _name_ == "_main_":
#     x0, y0, x_end = 0.0, 1.0, 2.0
#     x_vals, y_vals = rkf45(f, x0, y0, x_end)
#     fig, ax = plt.subplots(figsize=(8, 5))
#     ax.plot(x_vals, y_vals, 'b.-',
#             label=r'RKF45: dy/dx = $x^2 - \cos(x)$')
#     ax.set_title("Solution of dy/dx = $x^2 - \cos(x)$ Using RKF45", fontsize=14, pad=12)
#     ax.set_xlabel("x", fontsize=12)
#     ax.set_ylabel("y", fontsize=12)
#     ax.grid(True, linestyle=':', alpha=0.7)
#     ax.legend(loc='lower right')
#     at = AnchoredText(
#         'Sumoon Byanjankar [NCE080BCT045]',
#         loc='upper left',
#         prop=dict(size=12),
#         frameon=True
#     )
#     at.patch.set_boxstyle("round,pad=0.4")
#     at.patch.set_facecolor("lightyellow")
#     at.patch.set_edgecolor("black")
#     ax.add_artist(at)
#     plt.tight_layout()
#     plt.show()



#--------------------------------------------------------------------------------


import numpy as np
import matplotlib.pyplot as plt
x = np.array([1,  3,  5,   7,   9])
y = np.array([2.0, 2.8, 3.8, 4.4, 5.2])
n      = len(x)
sum_x  = np.sum(x)
sum_y  = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x * x)
b = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
a = (sum_y - b*sum_x) / n
print(f"Best‑fit line: y = {a:.4f} + {b:.4f} x")
y_pred = a + b*x
plt.figure(figsize=(8, 5), facecolor='white')
plt.scatter(x, y, s=80, edgecolor='k', label='Data Points', zorder=5)
plt.plot(x, y_pred, linewidth=2.5, label='Least Squares Fit')
plt.title("Least Squares Linear Regression", fontsize=16, weight='bold', pad=12)
plt.xlabel("x", fontsize=14)
plt.ylabel("y", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.text(0.99, 0.01,
         'Bikash[NCE080BCT045]',
         ha='right', va='bottom',
         transform=plt.gca().transAxes,
         fontsize=12,
         bbox=dict(facecolor='white', edgecolor='black', pad=4))
plt.legend(fontsize=12, frameon=True, edgecolor='gray')
plt.tight_layout()
plt.show()
